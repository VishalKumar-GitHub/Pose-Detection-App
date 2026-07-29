import io
import os
import hmac
import importlib
import streamlit as st
import numpy as np
import mediapipe as mp
from PIL import Image, ImageDraw, ImageFont, ImageOps
import tempfile
import threading
import urllib.request
import time

os.environ.setdefault("GLOG_minloglevel", "2")
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

# Import mediapipe components with error handling
try:
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision
except ImportError as e:
    print(f"✗ Error importing mediapipe: {e}")
    st.error(f"❌ Failed to import MediaPipe: {str(e)}\n\nPlease check if mediapipe is properly installed on the system.")
    st.stop()

try:
    import av
except ImportError as e:
    print(f"✗ Error importing av: {e}")
    st.error(f"❌ Failed to import PyAV: {str(e)}")
    st.stop()

try:
    from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
except ImportError as e:
    print(f"✗ Error importing streamlit_webrtc: {e}")
    st.error(f"❌ Failed to import streamlit-webrtc: {str(e)}")
    st.stop()

# ---------- Page config ----------
st.set_page_config(page_title="Pose Detection & Analysis", layout="wide")


def get_secret_value(name):
    try:
        value = st.secrets.get(name, "")
    except Exception:
        value = ""
    return str(value).strip() if value is not None else ""


def require_app_access():
    # Optional gate: only active when APP_ACCESS_KEY is configured.
    expected = get_secret_value("APP_ACCESS_KEY") or os.getenv("APP_ACCESS_KEY", "").strip()
    if not expected:
        return

    if "auth_ok" not in st.session_state:
        st.session_state.auth_ok = False

    if st.session_state.auth_ok:
        return

    st.title("Private App Access")
    st.write("Enter access key to continue.")
    entered = st.text_input("Access key", type="password")
    if st.button("Unlock"):
        st.session_state.auth_ok = hmac.compare_digest(entered, expected)
        if st.session_state.auth_ok:
            st.rerun()
        st.error("Invalid access key")
    st.stop()


require_app_access()

# ---------- Page background ----------
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
  background: linear-gradient(135deg, #8BC34A 0%, #FFEB3B 100%);
}
[data-testid="stHeader"] {
  background: transparent;
}
[data-testid="stSidebar"] {
  background: rgba(255, 255, 255, 0.8);
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Pose landmark indices for the new API
class PoseLandmark:
    NOSE = 0
    LEFT_EYE_INNER = 1
    LEFT_EYE = 2
    LEFT_EYE_OUTER = 3
    RIGHT_EYE_INNER = 4
    RIGHT_EYE = 5
    RIGHT_EYE_OUTER = 6
    LEFT_EAR = 7
    RIGHT_EAR = 8
    LEFT_MOUTH_CORNER = 9
    RIGHT_MOUTH_CORNER = 10
    LEFT_SHOULDER = 11
    RIGHT_SHOULDER = 12
    LEFT_ELBOW = 13
    RIGHT_ELBOW = 14
    LEFT_WRIST = 15
    RIGHT_WRIST = 16
    LEFT_PINKY = 17
    RIGHT_PINKY = 18
    LEFT_INDEX = 19
    RIGHT_INDEX = 20
    LEFT_THUMB = 21
    RIGHT_THUMB = 22
    LEFT_HIP = 23
    RIGHT_HIP = 24
    LEFT_KNEE = 25
    RIGHT_KNEE = 26
    LEFT_ANKLE = 27
    RIGHT_ANKLE = 28
    LEFT_HEEL = 29
    RIGHT_HEEL = 30
    LEFT_FOOT_INDEX = 31
    RIGHT_FOOT_INDEX = 32

# Pose connections
POSE_CONNECTIONS = [
    (11, 13), (13, 15), (12, 14), (14, 16),  # Arms
    (11, 12), (11, 23), (12, 24),  # Shoulders to hips
    (23, 25), (25, 27), (24, 26), (26, 28),  # Legs
    (27, 29), (29, 31), (28, 30), (30, 32),  # Feet
]

_POSE_SOLUTION_MODULE = None


def get_pose_solution_module():
    global _POSE_SOLUTION_MODULE
    if _POSE_SOLUTION_MODULE is not None:
        return _POSE_SOLUTION_MODULE

    for module_name in ("mediapipe.solutions.pose", "mediapipe.python.solutions.pose"):
        try:
            _POSE_SOLUTION_MODULE = importlib.import_module(module_name)
            return _POSE_SOLUTION_MODULE
        except Exception:
            continue

    _POSE_SOLUTION_MODULE = False
    return None


def create_fallback_pose(static_image_mode, cfg):
    pose_module = get_pose_solution_module()
    if not pose_module:
        return None

    return pose_module.Pose(
        static_image_mode=static_image_mode,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=cfg.get("det_conf", 0.35),
        min_tracking_confidence=cfg.get("track_conf", 0.30),
    )

# ---------- Sidebar ----------
st.sidebar.title("Customization Options")
text_size = st.sidebar.slider("Text Size", 0.5, 3.0, 1.0)
text_thickness = st.sidebar.slider("Text Thickness", 1, 5, 2)
text_color = st.sidebar.color_picker("Text Color", "#0000FF")
circle_radius = st.sidebar.slider("Circle Radius", 1, 10, 2)
line_thickness = st.sidebar.slider("Line Thickness", 1, 5, 2)
circle_color = st.sidebar.color_picker("Circle Color", "#FF5733")
line_color = st.sidebar.color_picker("Line Color", "#FF5733")
width = st.sidebar.slider("Width", 300, 1920, 640)
height = st.sidebar.slider("Height", 300, 1080, 480)

st.sidebar.subheader("Workout Coach")
workout_mode = st.sidebar.selectbox("Exercise Mode", ["Off", "Squat Counter"])
show_debug_logs = st.sidebar.checkbox("Show Debug Logs", value=False)
show_detection_diagnostics = st.sidebar.checkbox("Show Detection Diagnostics", value=True)

st.sidebar.subheader("Detection Tuning")
det_conf = st.sidebar.slider("Detection Confidence", 0.1, 0.9, 0.35, 0.05)
presence_conf = st.sidebar.slider("Presence Confidence", 0.1, 0.9, 0.30, 0.05)
track_conf = st.sidebar.slider("Tracking Confidence", 0.1, 0.9, 0.30, 0.05)
landmark_presence_draw = st.sidebar.slider("Landmark Draw Threshold", 0.0, 0.9, 0.20, 0.05)
performance_mode = st.sidebar.selectbox(
    "Performance Mode",
    ["Eco", "Balanced", "High Accuracy"],
    index=1,
    help="Balanced is recommended for Streamlit Cloud.",
)


def hex_to_rgb(hex_color):
    return tuple(int(hex_color.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def build_cfg():
    mode_config = {
        "Eco": {"detect_every_n": 3, "detect_max_side": 448},
        "Balanced": {"detect_every_n": 2, "detect_max_side": 512},
        "High Accuracy": {"detect_every_n": 1, "detect_max_side": 640},
    }
    perf = mode_config.get(performance_mode, mode_config["Balanced"])

    return {
        "text_size": text_size,
        "text_thickness": text_thickness,
        "text_rgb": hex_to_rgb(text_color),
        "circle_radius": circle_radius,
        "line_thickness": line_thickness,
        "circle_rgb": hex_to_rgb(circle_color),
        "line_rgb": hex_to_rgb(line_color),
        "workout_mode": workout_mode,
        "debug_logs": show_debug_logs,
        "show_detection_diagnostics": show_detection_diagnostics,
        "performance_mode": performance_mode,
        "detect_every_n": perf["detect_every_n"],
        "detect_max_side": perf["detect_max_side"],
        "det_conf": det_conf,
        "presence_conf": presence_conf,
        "track_conf": track_conf,
        "landmark_presence_draw": landmark_presence_draw,
    }


# ---------- Angle / posture helpers ----------
def calc_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    rad = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    ang = np.abs(rad * 180.0 / np.pi)
    return 360 - ang if ang > 180 else ang


def analyze_pose(landmarks):
    lm = PoseLandmark
    info = {}

    def pt(l):
        if l < len(landmarks):
            return [landmarks[l].x, landmarks[l].y]
        return [0, 0]

    l_arm = calc_angle(pt(lm.LEFT_SHOULDER), pt(lm.LEFT_ELBOW), pt(lm.LEFT_WRIST))
    r_arm = calc_angle(pt(lm.RIGHT_SHOULDER), pt(lm.RIGHT_ELBOW), pt(lm.RIGHT_WRIST))
    info["Left Arm"] = "straight" if l_arm > 150 else ("highly bent" if l_arm < 60 else "bent")
    info["Right Arm"] = "straight" if r_arm > 150 else ("highly bent" if r_arm < 60 else "bent")

    l_leg = calc_angle(pt(lm.LEFT_HIP), pt(lm.LEFT_KNEE), pt(lm.LEFT_ANKLE))
    r_leg = calc_angle(pt(lm.RIGHT_HIP), pt(lm.RIGHT_KNEE), pt(lm.RIGHT_ANKLE))
    info["Left Leg"] = "straight" if l_leg > 160 else "bent"
    info["Right Leg"] = "straight" if r_leg > 160 else "bent"

    l_sh, l_hip = pt(lm.LEFT_SHOULDER), pt(lm.LEFT_HIP)
    info["Back"] = "straight posture" if abs(l_sh[0] - l_hip[0]) < 0.05 else "bent posture"

    return info


def get_landmark_xy(landmarks, index):
    if index < len(landmarks):
        return np.array([landmarks[index].x, landmarks[index].y], dtype=float)
    return np.array([0.0, 0.0], dtype=float)


def get_squat_metrics(landmarks):
    lm = PoseLandmark
    l_sh = get_landmark_xy(landmarks, lm.LEFT_SHOULDER)
    r_sh = get_landmark_xy(landmarks, lm.RIGHT_SHOULDER)
    l_hip = get_landmark_xy(landmarks, lm.LEFT_HIP)
    r_hip = get_landmark_xy(landmarks, lm.RIGHT_HIP)
    l_knee = get_landmark_xy(landmarks, lm.LEFT_KNEE)
    r_knee = get_landmark_xy(landmarks, lm.RIGHT_KNEE)
    l_ankle = get_landmark_xy(landmarks, lm.LEFT_ANKLE)
    r_ankle = get_landmark_xy(landmarks, lm.RIGHT_ANKLE)

    left_knee_angle = calc_angle(l_hip, l_knee, l_ankle)
    right_knee_angle = calc_angle(r_hip, r_knee, r_ankle)
    avg_knee_angle = float((left_knee_angle + right_knee_angle) / 2.0)

    left_torso_angle = calc_angle(l_sh, l_hip, l_knee)
    right_torso_angle = calc_angle(r_sh, r_hip, r_knee)
    avg_torso_angle = float((left_torso_angle + right_torso_angle) / 2.0)

    ankle_dist = abs(l_ankle[0] - r_ankle[0]) + 1e-6
    knee_dist = abs(l_knee[0] - r_knee[0])
    knee_to_ankle_ratio = float(knee_dist / ankle_dist)

    return {
        "avg_knee_angle": avg_knee_angle,
        "avg_torso_angle": avg_torso_angle,
        "knee_to_ankle_ratio": knee_to_ankle_ratio,
    }


def get_squat_warnings(metrics):
    warnings = []
    if metrics["avg_knee_angle"] > 120:
        warnings.append("Go deeper")
    if metrics["knee_to_ankle_ratio"] < 0.75:
        warnings.append("Push knees out")
    if metrics["avg_torso_angle"] < 125:
        warnings.append("Chest up")
    return warnings


def get_font(size):
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size=size)
    except OSError:
        return ImageFont.load_default()


def draw_text_overlay(frame, info, cfg):
    pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil)
    font = get_font(int(20 * cfg["text_size"]))
    y = 10
    for key, value in info.items():
        text = f"{key}: {value}"
        draw.text((10, y), text, font=font, fill=cfg["text_rgb"])
        y += 30
    return np.array(pil)


def get_named_landmarks():
    lm = PoseLandmark
    return [
        (lm.NOSE, "Nose"),
        (lm.LEFT_EYE, "Left Eye"),
        (lm.RIGHT_EYE, "Right Eye"),
        (lm.LEFT_EAR, "Left Ear"),
        (lm.RIGHT_EAR, "Right Ear"),
        (lm.LEFT_SHOULDER, "Left Shoulder"),
        (lm.RIGHT_SHOULDER, "Right Shoulder"),
        (lm.LEFT_ELBOW, "Left Elbow"),
        (lm.RIGHT_ELBOW, "Right Elbow"),
        (lm.LEFT_WRIST, "Left Hand"),
        (lm.RIGHT_WRIST, "Right Hand"),
        (lm.LEFT_HIP, "Left Hip"),
        (lm.RIGHT_HIP, "Right Hip"),
        (lm.LEFT_KNEE, "Left Knee"),
        (lm.RIGHT_KNEE, "Right Knee"),
        (lm.LEFT_ANKLE, "Left Ankle"),
        (lm.RIGHT_ANKLE, "Right Ankle"),
    ]


def draw_landmarks_pil(frame, landmarks, cfg):
    if not landmarks:
        return frame

    pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil)
    width, height = pil.size
    label_font = get_font(max(10, int(12 * cfg["text_size"])))

    def lm_confidence(landmark):
        scores = []
        if hasattr(landmark, "presence") and landmark.presence is not None:
            scores.append(float(landmark.presence))
        if hasattr(landmark, "visibility") and landmark.visibility is not None:
            scores.append(float(landmark.visibility))
        return max(scores) if scores else 1.0

    def xy(idx):
        lm = landmarks[idx]
        vis = lm_confidence(lm)
        return [lm.x, lm.y], (int(lm.x * width), int(lm.y * height)), vis

    def draw_angle_label(a_idx, b_idx, c_idx, label):
        if max(a_idx, b_idx, c_idx) >= len(landmarks):
            return
        a, _, a_vis = xy(a_idx)
        b, (bx, by), b_vis = xy(b_idx)
        c, _, c_vis = xy(c_idx)
        if min(a_vis, b_vis, c_vis) < cfg.get("landmark_presence_draw", 0.2):
            return
        angle = calc_angle(a, b, c)
        text = f"{label}: {angle:.0f} deg"
        tx = min(max(bx + 8, 0), width - 1)
        ty = min(max(by + 8, 0), height - 1)
        draw.text((tx, ty), text, fill=cfg["text_rgb"], font=label_font)

    # Draw connections (with confidence threshold)
    for connection in POSE_CONNECTIONS:
        if connection[0] < len(landmarks) and connection[1] < len(landmarks):
            start = landmarks[connection[0]]
            end = landmarks[connection[1]]

            if lm_confidence(start) < cfg.get("landmark_presence_draw", 0.2):
                continue
            if lm_confidence(end) < cfg.get("landmark_presence_draw", 0.2):
                continue

            x1, y1 = int(start.x * width), int(start.y * height)
            x2, y2 = int(end.x * width), int(end.y * height)

            # Clamp to frame bounds
            x1, y1 = max(0, min(width-1, x1)), max(0, min(height-1, y1))
            x2, y2 = max(0, min(width-1, x2)), max(0, min(height-1, y2))

            draw.line([(x1, y1), (x2, y2)], fill=cfg["line_rgb"], width=cfg["line_thickness"])

    # Draw circles for landmarks
    for landmark in landmarks:
        # Skip if confidence is too low
        if lm_confidence(landmark) < cfg.get("landmark_presence_draw", 0.2):
            continue

        x, y = int(landmark.x * width), int(landmark.y * height)

        # Clamp to frame bounds
        x = max(0, min(width-1, x))
        y = max(0, min(height-1, y))

        radius = cfg["circle_radius"]
        draw.ellipse(
            [(x - radius, y - radius), (x + radius, y + radius)],
            fill=cfg["circle_rgb"], outline=cfg["circle_rgb"],
        )

    for idx, name in get_named_landmarks():
        if idx >= len(landmarks):
            continue
        landmark = landmarks[idx]
        if lm_confidence(landmark) < cfg.get("landmark_presence_draw", 0.2):
            continue

        x, y = int(landmark.x * width), int(landmark.y * height)
        label_x = min(max(x + 6, 0), width - 1)
        label_y = min(max(y - 18, 0), height - 1)
        draw.text((label_x, label_y), name, fill=cfg["text_rgb"], font=label_font)

    lm = PoseLandmark
    draw_angle_label(lm.LEFT_SHOULDER, lm.LEFT_ELBOW, lm.LEFT_WRIST, "L Elbow")
    draw_angle_label(lm.RIGHT_SHOULDER, lm.RIGHT_ELBOW, lm.RIGHT_WRIST, "R Elbow")
    draw_angle_label(lm.LEFT_HIP, lm.LEFT_KNEE, lm.LEFT_ANKLE, "L Knee")
    draw_angle_label(lm.RIGHT_HIP, lm.RIGHT_KNEE, lm.RIGHT_ANKLE, "R Knee")

    return np.array(pil)


def draw_and_analyze(frame, landmarks, cfg):
    if landmarks:
        frame = draw_landmarks_pil(frame, landmarks, cfg)
        info = analyze_pose(landmarks)
        frame = draw_text_overlay(frame, info, cfg)
    return frame


def draw_and_analyze_with_extra(frame, landmarks, cfg, extra_info):
    if landmarks:
        frame = draw_landmarks_pil(frame, landmarks, cfg)
        info = analyze_pose(landmarks)
        if extra_info:
            info.update(extra_info)
        frame = draw_text_overlay(frame, info, cfg)
    return frame


def detect_with_fallback(fallback_pose, image_rgb):
    if fallback_pose is None:
        return None
    result = fallback_pose.process(image_rgb)
    if result and result.pose_landmarks:
        return result.pose_landmarks.landmark
    return None


def process_static(img, landmarks, cfg):
    pil = Image.fromarray(img)
    pil = pil.resize((width, height), Image.Resampling.LANCZOS)
    rgb = np.array(pil)
    return draw_and_analyze(rgb, landmarks, cfg)


def resize_for_detection(image, max_side=512):
    h, w = image.shape[:2]
    largest = max(h, w)
    if largest <= max_side:
        return image
    scale = max_side / float(largest)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    pil = Image.fromarray(image)
    resized = pil.resize((new_w, new_h), Image.Resampling.BILINEAR)
    return np.array(resized)


def build_image_candidates(image):
    candidates = [("original", image)]

    pil = Image.fromarray(image)
    mirrored = np.array(pil.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
    candidates.append(("mirrored", mirrored))

    enhanced = pil.convert("L")
    enhanced = Image.eval(enhanced, lambda px: 255 if px > 180 else int(px * 1.25))
    enhanced_rgb = np.array(enhanced.convert("RGB"))
    candidates.append(("enhanced", enhanced_rgb))

    enhanced_mirrored = np.array(Image.fromarray(enhanced_rgb).transpose(Image.Transpose.FLIP_LEFT_RIGHT))
    candidates.append(("enhanced_mirrored", enhanced_mirrored))

    rot90 = np.array(Image.fromarray(image).transpose(Image.Transpose.ROTATE_90))
    rot270 = np.array(Image.fromarray(image).transpose(Image.Transpose.ROTATE_270))
    candidates.append(("rot90", rot90))
    candidates.append(("rot270", rot270))

    enhanced_rot90 = np.array(Image.fromarray(enhanced_rgb).transpose(Image.Transpose.ROTATE_90))
    enhanced_rot270 = np.array(Image.fromarray(enhanced_rgb).transpose(Image.Transpose.ROTATE_270))
    candidates.append(("enhanced_rot90", enhanced_rot90))
    candidates.append(("enhanced_rot270", enhanced_rot270))

    # Multi-scale and padded variants improve small-subject detection.
    for target in (384, 512, 640):
        scaled = resize_for_detection(image, max_side=target)
        candidates.append((f"scaled_{target}", scaled))

    h, w = image.shape[:2]
    side = max(h, w)
    square = np.zeros((side, side, 3), dtype=np.uint8)
    y0 = (side - h) // 2
    x0 = (side - w) // 2
    square[y0:y0 + h, x0:x0 + w] = image
    candidates.append(("square_padded", square))

    # Deduplicate candidates that may end up identical.
    unique = []
    seen = set()
    for name, item in candidates:
        key = hash(item.tobytes())
        if key in seen:
            continue
        seen.add(key)
        unique.append((name, item))
    return unique


def detect_landmarks_from_image(image, cfg):
    det_levels = [
        float(cfg.get("det_conf", 0.35)),
        0.25,
        0.15,
        0.05,
    ]
    presence_levels = [
        float(cfg.get("presence_conf", 0.30)),
        0.20,
        0.10,
        0.05,
    ]
    det_levels = sorted(set(max(0.05, min(0.9, x)) for x in det_levels), reverse=True)
    presence_levels = sorted(set(max(0.05, min(0.9, x)) for x in presence_levels), reverse=True)

    candidates = build_image_candidates(image)
    diagnostics = {
        "det_levels": det_levels,
        "presence_levels": presence_levels,
        "model_variants": ["full", "heavy", "lite"],
        "attempts": [],
        "status": "no_pose",
    }

    for det_conf_try in det_levels:
        for presence_conf_try in presence_levels:
            for model_variant in ("full", "heavy", "lite"):
                pose_landmarker = get_pose_landmarker(
                    det_conf_try,
                    presence_conf_try,
                    cfg.get("track_conf", 0.30),
                    "IMAGE",
                    model_variant,
                    3,
                )
                fallback_cfg = dict(cfg)
                fallback_cfg["det_conf"] = det_conf_try
                fallback_cfg["track_conf"] = cfg.get("track_conf", 0.30)
                fallback_pose = create_fallback_pose(static_image_mode=True, cfg=fallback_cfg)

                try:
                    for variant_name, candidate in candidates:
                        landmarks = None
                        task_hit = False
                        fallback_hit = False
                        if pose_landmarker:
                            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=candidate)
                            detection_result = pose_landmarker.detect(mp_image)
                            if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                                landmarks = detection_result.pose_landmarks[0]
                                task_hit = True

                        if landmarks is None:
                            landmarks = detect_with_fallback(fallback_pose, candidate)
                            fallback_hit = landmarks is not None

                        diagnostics["attempts"].append(
                            {
                                "model_variant": model_variant,
                                "variant": variant_name,
                                "det_conf": round(det_conf_try, 3),
                                "presence_conf": round(presence_conf_try, 3),
                                "task_hit": task_hit,
                                "fallback_hit": fallback_hit,
                                "success": landmarks is not None,
                            }
                        )

                        if landmarks is not None:
                            diagnostics["status"] = "pose_detected"
                            diagnostics["winner"] = {
                                "model_variant": model_variant,
                                "variant": variant_name,
                                "det_conf": round(det_conf_try, 3),
                                "presence_conf": round(presence_conf_try, 3),
                                "source": "task" if task_hit else "fallback",
                            }
                            return landmarks, candidate, diagnostics
                finally:
                    if fallback_pose is not None:
                        fallback_pose.close()

    return None, image, diagnostics


# ---------- Download and load pose landmarker model ----------
@st.cache_resource
def get_pose_landmarker(
    det_conf=0.35,
    presence_conf=0.30,
    track_conf=0.30,
    running_mode="IMAGE",
    model_variant="full",
    num_poses=1,
):
    variant = str(model_variant).strip().lower()
    if variant not in {"full", "heavy", "lite"}:
        variant = "full"

    model_path = os.path.expanduser(f"~/.mediapipe/pose_landmarker_{variant}.task")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    if not os.path.exists(model_path):
        print(f"[INFO] Downloading pose detection model ({variant})...")

        model_urls = {
            "full": "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task",
            "heavy": "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/1/pose_landmarker_heavy.task",
            "lite": "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task",
        }
        url = model_urls[variant]

        try:
            if build_cfg().get("debug_logs"):
                print(f"Attempting to download from: {url}")
            with urllib.request.urlopen(url, timeout=60) as response:
                with open(model_path, "wb") as out_file:
                    out_file.write(response.read())
            if build_cfg().get("debug_logs"):
                print(f"✓ Successfully downloaded model from {url}")
        except urllib.error.HTTPError as e:
            print(f"✗ HTTP Error from {url}: HTTP {e.code}: {e.reason}")
            return None
        except urllib.error.URLError as e:
            print(f"✗ Connection error for {url}: {e.reason}")
            return None
        except Exception as e:
            print(f"✗ Unexpected error for {url}: {e}")
            return None
    
    try:
        mode = vision.RunningMode.IMAGE
        if str(running_mode).upper() == "VIDEO":
            mode = vision.RunningMode.VIDEO

        base_options = python.BaseOptions(
            model_asset_path=model_path,
            delegate=python.BaseOptions.Delegate.CPU,
        )
        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            running_mode=mode,
            num_poses=max(1, int(num_poses)),
            min_pose_detection_confidence=float(det_conf),
            min_pose_presence_confidence=float(presence_conf),
            min_tracking_confidence=float(track_conf),
            output_segmentation_masks=False,
        )
        landmarker = vision.PoseLandmarker.create_from_options(options)
        print("✓ PoseLandmarker initialized successfully")
        return landmarker
    except Exception as e:
        print(f"✗ Initialization error: {str(e)}")
        return None


# ---------- Live camera processor ----------
class PoseProcessor(VideoProcessorBase):
    def __init__(self):
        self.cfg = build_cfg()
        self.pose_landmarker = get_pose_landmarker(
            self.cfg.get("det_conf", 0.35),
            self.cfg.get("presence_conf", 0.30),
            self.cfg.get("track_conf", 0.30),
            "VIDEO",
        )
        # Fallback detector is more tolerant on noisy webcam streams.
        self.pose_fallback = create_fallback_pose(static_image_mode=False, cfg=self.cfg)
        self.lock = threading.Lock()
        self.last_ts_ms = 0
        self.frame_index = 0
        self.detect_every_n = max(1, int(self.cfg.get("detect_every_n", 2)))
        self.detect_max_side = max(256, int(self.cfg.get("detect_max_side", 512)))
        self.last_landmarks = None
        self.snapshot = None
        self.rep_count = 0
        self.bad_rep_count = 0
        self.squat_phase = "up"
        self.rep_depth_hit = False
        self.rep_flags = set()
        self.last_feedback = "Ready"
        self.set_active = True
        self.set_start_time = time.time()
        self.rep_timestamps = []
        self.rep_depths = []
        self.current_rep_min_knee = 180.0

    def reset_set_stats(self):
        self.rep_count = 0
        self.bad_rep_count = 0
        self.squat_phase = "up"
        self.rep_depth_hit = False
        self.rep_flags = set()
        self.last_feedback = "Ready"
        self.rep_timestamps = []
        self.rep_depths = []
        self.current_rep_min_knee = 180.0
        self.set_start_time = time.time()

    def get_analytics(self):
        elapsed = max(1.0, time.time() - self.set_start_time)
        total_attempts = self.rep_count + self.bad_rep_count
        valid_rate = (self.rep_count / total_attempts * 100.0) if total_attempts > 0 else 0.0
        avg_depth = (sum(self.rep_depths) / len(self.rep_depths)) if self.rep_depths else 0.0
        reps_per_min = self.rep_count / (elapsed / 60.0)

        avg_tempo = 0.0
        if len(self.rep_timestamps) >= 2:
            diffs = [self.rep_timestamps[i] - self.rep_timestamps[i - 1] for i in range(1, len(self.rep_timestamps))]
            avg_tempo = sum(diffs) / len(diffs)

        form_score = max(0.0, min(100.0, valid_rate))
        return {
            "elapsed_sec": elapsed,
            "valid_rate": valid_rate,
            "avg_depth": avg_depth,
            "reps_per_min": reps_per_min,
            "avg_tempo": avg_tempo,
            "form_score": form_score,
            "set_active": self.set_active,
        }

    def update_squat_state(self, landmarks):
        metrics = get_squat_metrics(landmarks)
        warnings = get_squat_warnings(metrics)
        knee_angle = metrics["avg_knee_angle"]

        if not self.set_active:
            analytics = self.get_analytics()
            warning_text = "none" if not warnings else ", ".join(warnings)
            return {
                "Exercise": "Squat Counter",
                "Set Status": "paused",
                "Reps": str(self.rep_count),
                "No-Reps": str(self.bad_rep_count),
                "RPM": f"{analytics['reps_per_min']:.1f}",
                "Avg Depth": (f"{analytics['avg_depth']:.1f}" if analytics["avg_depth"] > 0 else "n/a"),
                "Form Score": f"{analytics['form_score']:.0f}/100",
                "Knee Angle": f"{knee_angle:.1f}",
                "Form Warnings": warning_text,
                "Rep Feedback": "Set paused",
            }

        if self.squat_phase == "up" and knee_angle < 140:
            self.squat_phase = "down"
            self.rep_depth_hit = False
            self.rep_flags = set()
            self.current_rep_min_knee = knee_angle

        if self.squat_phase == "down":
            self.current_rep_min_knee = min(self.current_rep_min_knee, knee_angle)
            if knee_angle < 120:
                self.rep_depth_hit = True
            for warning in warnings:
                self.rep_flags.add(warning)

            if knee_angle > 150:
                reasons = []
                if not self.rep_depth_hit or "Go deeper" in self.rep_flags:
                    reasons.append("depth too shallow")
                if "Push knees out" in self.rep_flags:
                    reasons.append("knees caving in")
                if "Chest up" in self.rep_flags:
                    reasons.append("excessive forward lean")

                if reasons:
                    self.bad_rep_count += 1
                    self.last_feedback = "No rep: " + ", ".join(reasons)
                else:
                    self.rep_count += 1
                    self.rep_timestamps.append(time.time())
                    self.rep_depths.append(self.current_rep_min_knee)
                    self.last_feedback = "Good rep"

                self.squat_phase = "up"
                self.rep_depth_hit = False
                self.rep_flags = set()
                self.current_rep_min_knee = 180.0

        analytics = self.get_analytics()
        warning_text = "none" if not warnings else ", ".join(warnings)
        return {
            "Exercise": "Squat Counter",
            "Set Status": "active",
            "Reps": str(self.rep_count),
            "No-Reps": str(self.bad_rep_count),
            "RPM": f"{analytics['reps_per_min']:.1f}",
            "Avg Depth": (f"{analytics['avg_depth']:.1f}" if analytics["avg_depth"] > 0 else "n/a"),
            "Form Score": f"{analytics['form_score']:.0f}/100",
            "Phase": self.squat_phase,
            "Knee Angle": f"{knee_angle:.1f}",
            "Form Warnings": warning_text,
            "Rep Feedback": self.last_feedback,
        }

    def recv(self, frame):
        img = frame.to_ndarray(format="rgb24")

        # Ensure image is correct format for MediaPipe and PIL.
        if img.dtype != np.uint8:
            img = (img * 255).astype(np.uint8)

        with self.lock:
            cfg = self.cfg
            self.detect_every_n = max(1, int(cfg.get("detect_every_n", self.detect_every_n)))
            self.detect_max_side = max(256, int(cfg.get("detect_max_side", self.detect_max_side)))
            detect_every_n = self.detect_every_n
            detect_max_side = self.detect_max_side

        self.frame_index += 1
        run_detection = (self.frame_index % detect_every_n) == 0

        out = img
        landmarks = self.last_landmarks if not run_detection else None
        try:
            if run_detection:
                detect_img = resize_for_detection(img, max_side=detect_max_side)
                if self.pose_landmarker:
                    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=detect_img)
                    ts_ms = int(time.time() * 1000)
                    if ts_ms <= self.last_ts_ms:
                        ts_ms = self.last_ts_ms + 1
                    self.last_ts_ms = ts_ms
                    detection_result = self.pose_landmarker.detect_for_video(mp_image, ts_ms)
                    if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                        landmarks = detection_result.pose_landmarks[0]

                if landmarks is None:
                    landmarks = detect_with_fallback(self.pose_fallback, detect_img)

                self.last_landmarks = landmarks

            if landmarks is not None:
                if cfg.get("workout_mode") == "Squat Counter":
                    extra_info = self.update_squat_state(landmarks)
                    out = draw_and_analyze_with_extra(img, landmarks, cfg, extra_info)
                else:
                    out = draw_and_analyze(img, landmarks, cfg)
            elif cfg.get("debug_logs"):
                print("[DEBUG] No pose detected in frame")
        except Exception as e:
            if cfg.get("debug_logs"):
                print(f"[ERROR] Pose detection error: {e}")

        # Always keep the most recent frame so snapshot works even without a pose.
        with self.lock:
            self.snapshot = out.copy()

        return av.VideoFrame.from_ndarray(out, format="rgb24")


RTC_CONFIG = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# ---------- Main ----------
st.title("Pose Detection and Analysis App")
st.write("Upload an image or video, or use your live camera to detect and analyze human poses.")

input_type = st.selectbox(
    "Choose input type",
    ["Live Camera", "Camera Snapshot (Stable)", "Upload Image", "Upload Video"],
)

if input_type == "Live Camera":
    st.info("Allow camera access when your browser prompts. Sliders update the stream live.")
    ctx = webrtc_streamer(
        key="pose",
        video_processor_factory=PoseProcessor,
        rtc_configuration=RTC_CONFIG,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )

    if ctx.video_processor:
        with ctx.video_processor.lock:
            ctx.video_processor.cfg = build_cfg()

    if ctx.video_processor and workout_mode == "Squat Counter":
        controls1, controls2, controls3 = st.columns(3)
        if controls1.button("Start Set"):
            with ctx.video_processor.lock:
                ctx.video_processor.set_active = True
                if ctx.video_processor.set_start_time is None:
                    ctx.video_processor.set_start_time = time.time()
        if controls2.button("Pause Set"):
            with ctx.video_processor.lock:
                ctx.video_processor.set_active = False
        if controls3.button("Reset Set"):
            with ctx.video_processor.lock:
                ctx.video_processor.reset_set_stats()

        with ctx.video_processor.lock:
            rep_count = ctx.video_processor.rep_count
            bad_rep_count = ctx.video_processor.bad_rep_count
            phase = ctx.video_processor.squat_phase
            feedback = ctx.video_processor.last_feedback
            analytics = ctx.video_processor.get_analytics()

        c1, c2, c3 = st.columns(3)
        c1.metric("Reps", rep_count)
        c2.metric("No-Reps", bad_rep_count)
        c3.metric("Phase", phase)
        c4, c5, c6 = st.columns(3)
        c4.metric("Form Score", f"{analytics['form_score']:.0f}/100")
        c5.metric("Rep Pace", f"{analytics['reps_per_min']:.1f} rpm")
        c6.metric("Avg Depth", (f"{analytics['avg_depth']:.1f} deg" if analytics["avg_depth"] > 0 else "n/a"))
        st.progress(int(analytics["form_score"]) / 100.0)
        st.caption(f"Feedback: {feedback}")

    if ctx.video_processor and st.button("📸 Take Snapshot"):
        with ctx.video_processor.lock:
            snap = ctx.video_processor.snapshot
        if snap is not None:
            st.image(snap, channels="RGB", caption="Snapshot")
            buffer = io.BytesIO()
            Image.fromarray(snap).save(buffer, format="PNG")
            st.download_button("⬇️ Download Snapshot", buffer.getvalue(),
                               file_name="pose_snapshot.png", mime="image/png")
        else:
            st.warning("No frame captured yet — wait a moment and try again.")

elif input_type == "Upload Image":
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file:
        image = np.array(ImageOps.exif_transpose(Image.open(file)).convert("RGB"))
        st.info(f"📊 Image shape: {image.shape}, dtype: {image.dtype}")
        
        cfg = build_cfg()
        try:
            landmarks, used_image, diagnostics = detect_landmarks_from_image(image, cfg)

            if landmarks is not None:
                st.success("✓ Pose detected")
                out = process_static(used_image, landmarks, cfg)
            else:
                st.warning("❌ No pose detected in the image. Try a clearer photo with your full body visible.")
                out = image

            if cfg.get("show_detection_diagnostics"):
                st.caption("Detection diagnostics")
                st.json(diagnostics, expanded=False)
        except Exception as e:
            st.error(f"❌ Detection error: {e}")
            if cfg.get("debug_logs"):
                print(f"[ERROR] Image upload detection: {e}")
            out = image
        
        st.image(out, channels="RGB")
        buffer = io.BytesIO()
        Image.fromarray(out).save(buffer, format="PNG")
        st.download_button("⬇️ Download Result", buffer.getvalue(),
                           file_name="pose_result.png", mime="image/png")

elif input_type == "Camera Snapshot (Stable)":
    st.info("This mode is recommended on Streamlit Cloud if Live Camera is unstable.")
    shot = st.camera_input("Take a photo")
    if shot is not None:
        image = np.array(Image.open(shot).convert("RGB"))
        cfg = build_cfg()
        try:
            landmarks, used_image, diagnostics = detect_landmarks_from_image(image, cfg)
            if landmarks is not None:
                st.success("✓ Pose detected")
                out = process_static(used_image, landmarks, cfg)
            else:
                st.warning("❌ No pose detected in snapshot. Keep full body visible and improve lighting.")
                out = image

            if cfg.get("show_detection_diagnostics"):
                st.caption("Detection diagnostics")
                st.json(diagnostics, expanded=False)
        except Exception as e:
            st.error(f"❌ Detection error: {e}")
            if cfg.get("debug_logs"):
                print(f"[ERROR] Camera snapshot detection: {e}")
            out = image

        st.image(out, channels="RGB")
        buffer = io.BytesIO()
        Image.fromarray(out).save(buffer, format="PNG")
        st.download_button(
            "⬇️ Download Snapshot Result",
            buffer.getvalue(),
            file_name="pose_snapshot_result.png",
            mime="image/png",
        )

elif input_type == "Upload Video":
    file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    if file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())
        tfile.flush()
        tfile.close()
        try:
            container = av.open(tfile.name)
            stframe = st.empty()
            cfg = build_cfg()
            pose_landmarker = get_pose_landmarker(
                cfg.get("det_conf", 0.35),
                cfg.get("presence_conf", 0.30),
                cfg.get("track_conf", 0.30),
                "VIDEO",
            )
            fallback_pose = create_fallback_pose(static_image_mode=False, cfg=cfg)
            frame_idx = 0
            last_landmarks = None
            detect_every_n = max(1, int(cfg.get("detect_every_n", 2)))
            detect_max_side = max(256, int(cfg.get("detect_max_side", 512)))
            
            for packet in container.demux(video=0):
                for frame in packet.decode():
                    img = frame.to_ndarray(format="rgb24")
                    try:
                        frame_idx += 1
                        run_detection = (frame_idx % detect_every_n) == 0
                        landmarks = last_landmarks if not run_detection else None

                        if run_detection:
                            detect_img = resize_for_detection(img, max_side=detect_max_side)
                            if pose_landmarker:
                                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=detect_img)
                                ts_ms = int((frame.time or (frame_idx / 30.0)) * 1000)
                                detection_result = pose_landmarker.detect_for_video(mp_image, ts_ms)
                                if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                                    landmarks = detection_result.pose_landmarks[0]

                            if landmarks is None:
                                landmarks = detect_with_fallback(fallback_pose, detect_img)

                            last_landmarks = landmarks

                        if landmarks is not None:
                            out = process_static(img, landmarks, cfg)
                        else:
                            out = img
                    except Exception as e:
                        if cfg.get("debug_logs"):
                            print(f"Frame detection error: {e}")
                        out = img

                    stframe.image(out, channels="RGB")
            if fallback_pose is not None:
                fallback_pose.close()
            container.close()
        finally:
            os.unlink(tfile.name)
