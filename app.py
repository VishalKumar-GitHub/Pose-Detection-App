import io
import os
import streamlit as st
import numpy as np
from mediapipe.solutions import pose as mp_pose
from mediapipe.solutions import pose_connections as mp_pose_connections
from PIL import Image, ImageDraw, ImageFont
import tempfile
import av
import threading
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

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

# ---------- MediaPipe setup ----------

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
    lm = mp_pose.PoseLandmark
    info = {}

    def pt(l):
        return [landmarks[l].x, landmarks[l].y]

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
    pil_img = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_img)
    font = get_font(int(16 * cfg["text_size"]))
    y = 10
    for k, v in info.items():
        draw.text((10, y), f"{k}: {v}", fill=cfg["text_rgb"], font=font)
        y += int(24 * cfg["text_size"])
    return np.array(pil_img)


def draw_and_analyze(frame, results, cfg):
    if results.pose_landmarks:

        frame = draw_landmarks_pil(frame, results.pose_landmarks.landmark, cfg)

        info = analyze_pose(results.pose_landmarks.landmark)
        frame = draw_text_overlay(frame, info, cfg)
    return frame


def draw_landmarks_pil(frame, landmarks, cfg):
    pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil)
    width, height = pil.size
    for connection in mp_pose_connections.POSE_CONNECTIONS:
        start = landmarks[connection[0]]
        end = landmarks[connection[1]]
        x1, y1 = int(start.x * width), int(start.y * height)
        x2, y2 = int(end.x * width), int(end.y * height)
        draw.line([(x1, y1), (x2, y2)], fill=cfg["line_rgb"], width=cfg["line_thickness"])
    for landmark in landmarks:
        x, y = int(landmark.x * width), int(landmark.y * height)
        radius = cfg["circle_radius"]
        draw.ellipse(
            [(x - radius, y - radius), (x + radius, y + radius)],
            fill=cfg["circle_rgb"], outline=cfg["circle_rgb"],
        )
    return np.array(pil)


def process_static(frame, pose, cfg):
    pil = Image.fromarray(frame)
    pil = pil.resize((width, height), Image.Resampling.LANCZOS)
    rgb = np.array(pil)
    results = pose.process(rgb)
    return draw_and_analyze(rgb, results, cfg)


# ---------- Live camera processor ----------
class PoseProcessor(VideoProcessorBase):
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.cfg = build_cfg()          # updated live from the main thread
        self.lock = threading.Lock()
        self.snapshot = None            # last processed frame, for download

    def recv(self, frame):
        img = frame.to_ndarray(format="rgb24")
        results = self.pose.process(img)
        with self.lock:
            cfg = self.cfg
        img = draw_and_analyze(img, results, cfg)
        with self.lock:
            self.snapshot = img.copy()
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

    # push current slider values into the running processor every rerun
    if ctx.video_processor:
        with ctx.video_processor.lock:
            ctx.video_processor.cfg = build_cfg()

    # snapshot / download
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
        with mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5) as pose:
            out = process_static(image, pose, build_cfg())
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
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                for packet in container.demux(video=0):
                    for frame in packet.decode():
                        img = frame.to_ndarray(format="rgb24")
                        out = process_static(img, pose, cfg)
                        stframe.image(out, channels="RGB")
            container.close()
        finally:
            os.unlink(tfile.name)
