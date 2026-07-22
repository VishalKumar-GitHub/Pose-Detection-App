import io
import os
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import tempfile
import threading
import urllib.request

# Import mediapipe components with error handling
try:
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision
    print("✓ MediaPipe imported successfully")
except ImportError as e:
    print(f"✗ Error importing mediapipe: {e}")
    st.error(f"❌ Failed to import MediaPipe: {str(e)}\n\nPlease check if mediapipe is properly installed on the system.")
    st.stop()

try:
    import av
    print("✓ PyAV imported successfully")
except ImportError as e:
    print(f"✗ Error importing av: {e}")
    st.error(f"❌ Failed to import PyAV: {str(e)}")
    st.stop()

try:
    from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
    print("✓ streamlit-webrtc imported successfully")
except ImportError as e:
    print(f"✗ Error importing streamlit_webrtc: {e}")
    st.error(f"❌ Failed to import streamlit-webrtc: {str(e)}")
    st.stop()

# ---------- Page config ----------
st.set_page_config(page_title="Pose Detection & Analysis", layout="wide")

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


def hex_to_rgb(hex_color):
    return tuple(int(hex_color.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def build_cfg():
    return {
        "text_size": text_size,
        "text_thickness": text_thickness,
        "text_rgb": hex_to_rgb(text_color),
        "circle_radius": circle_radius,
        "line_thickness": line_thickness,
        "circle_rgb": hex_to_rgb(circle_color),
        "line_rgb": hex_to_rgb(line_color),
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


def draw_landmarks_pil(frame, landmarks, cfg):
    if not landmarks:
        return frame
    
    pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil)
    width, height = pil.size
    
    # Draw connections
    for connection in POSE_CONNECTIONS:
        if connection[0] < len(landmarks) and connection[1] < len(landmarks):
            start = landmarks[connection[0]]
            end = landmarks[connection[1]]
            
            # Skip if confidence is too low
            if hasattr(start, 'presence') and start.presence < 0.5:
                continue
            if hasattr(end, 'presence') and end.presence < 0.5:
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
        if hasattr(landmark, 'presence') and landmark.presence < 0.5:
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
    
    return np.array(pil)


def draw_and_analyze(frame, landmarks, cfg):
    if landmarks:
        frame = draw_landmarks_pil(frame, landmarks, cfg)
        info = analyze_pose(landmarks)
        frame = draw_text_overlay(frame, info, cfg)
    return frame


def process_static(img, landmarks, cfg):
    pil = Image.fromarray(img)
    pil = pil.resize((width, height), Image.Resampling.LANCZOS)
    rgb = np.array(pil)
    return draw_and_analyze(rgb, landmarks, cfg)


# ---------- Download and load pose landmarker model ----------
@st.cache_resource
@st.cache_resource
def get_pose_landmarker():
    model_path = os.path.expanduser("~/.mediapipe/pose_landmarker.tflite")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    if not os.path.exists(model_path):
        st.info("📥 Downloading pose detection model (50MB)...")
        
        # Multiple model variants with fallback options
        urls = [
            "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float32/pose_landmarker_full.tflite",
            "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float32/pose_landmarker_heavy.tflite",
        ]
        
        downloaded = False
        last_error = None
        
        for url in urls:
            try:
                print(f"Attempting to download from: {url}")
                with st.spinner(f"Downloading from {url.split('/')[-1]}..."):
                    urllib.request.urlretrieve(url, model_path, timeout=60)
                    print(f"✓ Successfully downloaded model from {url}")
                    downloaded = True
                    st.success("✓ Model downloaded successfully!")
                    break
            except urllib.error.HTTPError as e:
                last_error = f"HTTP {e.code}: {e.reason}"
                print(f"✗ HTTP Error from {url}: {last_error}")
            except urllib.error.URLError as e:
                last_error = f"Connection error: {e.reason}"
                print(f"✗ Connection error for {url}: {last_error}")
            except Exception as e:
                last_error = str(e)
                print(f"✗ Unexpected error for {url}: {last_error}")
        
        if not downloaded:
            error_msg = f"Failed to download model. Last error: {last_error}"
            print(f"✗ {error_msg}")
            st.error(f"❌ {error_msg}\n\nTroubleshooting:\n- Check internet connection\n- Try reloading the page\n- Check firewall/proxy settings")
            return None
    
    try:
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.PoseLandmarkerOptions(base_options=base_options)
        landmarker = vision.PoseLandmarker.create_from_options(options)
        print("✓ PoseLandmarker initialized successfully")
        return landmarker
    except Exception as e:
        st.error(f"❌ Failed to initialize pose landmarker: {str(e)}")
        print(f"✗ Initialization error: {str(e)}")
        return None


# ---------- Live camera processor ----------
class PoseProcessor(VideoProcessorBase):
    def __init__(self):
        self.pose_landmarker = get_pose_landmarker()
        self.cfg = build_cfg()
        self.lock = threading.Lock()
        self.snapshot = None

    def recv(self, frame):
        img = frame.to_ndarray(format="rgb24")
        
        if self.pose_landmarker:
            try:
                # Create MediaPipe Image - pass numpy array directly
                mp_image = vision.Image(image_format=vision.ImageFormat.SRGB, data=img)
                detection_result = self.pose_landmarker.detect(mp_image)
                
                with self.lock:
                    cfg = self.cfg
                
                if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                    img = draw_and_analyze(img, detection_result.pose_landmarks[0], cfg)
                
                with self.lock:
                    self.snapshot = img.copy()
            except Exception as e:
                print(f"Error in pose detection: {e}")
        
        return av.VideoFrame.from_ndarray(img, format="rgb24")


RTC_CONFIG = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# ---------- Main ----------
st.title("Pose Detection and Analysis App")
st.write("Upload an image or video, or use your live camera to detect and analyze human poses.")

input_type = st.selectbox("Choose input type", ["Live Camera", "Upload Image", "Upload Video"])

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
        image = np.array(Image.open(file).convert("RGB"))
        pose_landmarker = get_pose_landmarker()
        
        if pose_landmarker:
            try:
                mp_image = vision.Image(image_format=vision.ImageFormat.SRGB, data=image)
                detection_result = pose_landmarker.detect(mp_image)
                
                if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                    out = process_static(image, detection_result.pose_landmarks[0], build_cfg())
                else:
                    st.warning("No pose detected in the image")
                    out = image
            except Exception as e:
                st.error(f"Detection error: {e}")
                out = image
        else:
            out = image
        
        st.image(out, channels="RGB")
        buffer = io.BytesIO()
        Image.fromarray(out).save(buffer, format="PNG")
        st.download_button("⬇️ Download Result", buffer.getvalue(),
                           file_name="pose_result.png", mime="image/png")

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
            pose_landmarker = get_pose_landmarker()
            
            if pose_landmarker:
                for packet in container.demux(video=0):
                    for frame in packet.decode():
                        img = frame.to_ndarray(format="rgb24")
                        try:
                            mp_image = vision.Image(image_format=vision.ImageFormat.SRGB, data=img)
                            detection_result = pose_landmarker.detect(mp_image)
                            
                            if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                                out = process_static(img, detection_result.pose_landmarks[0], cfg)
                            else:
                                out = img
                        except Exception as e:
                            print(f"Frame detection error: {e}")
                            out = img
                        
                        stframe.image(out, channels="RGB")
            container.close()
        finally:
            os.unlink(tfile.name)
