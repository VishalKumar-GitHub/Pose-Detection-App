# Pose Detection and Analysis App

A real-time human pose detection and analysis application built with **Streamlit**, **MediaPipe**, and **OpenCV**. Upload an image or video, or stream your live webcam, to detect body landmarks and get instant posture analysis.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

- **Three input modes**: live camera (via WebRTC), image upload, and video upload
- **Real-time pose landmark detection** using MediaPipe Pose
- **Posture analysis** — reports arm bend, leg bend, and back alignment on each frame
- **Live customization** — adjust text size, colors, circle radius, and line thickness while the camera streams
- **Snapshot & download** — capture and save any analyzed frame as PNG
- **Cloud-deployable** — live camera works on Streamlit Community Cloud because capture happens client-side

---

## Demo

Choose an input type from the dropdown, then:

| Mode | What it does |
|------|--------------|
| **Live Camera** | Streams your webcam and overlays pose + analysis in real time |
| **Upload Image** | Detects pose on a single image, with a download button |
| **Upload Video** | Plays through the video frame by frame with pose overlay |

---

## Tech Stack

- [Streamlit](https://streamlit.io/) — web UI
- [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc) — browser webcam streaming
- [MediaPipe](https://google.github.io/mediapipe/) — pose estimation (pinned to `mediapipe==0.10.35`)
- [OpenCV](https://opencv.org/) — image processing and drawing
- NumPy, Pillow, PyAV

---

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/pose-detection-app.git
cd pose-detection-app

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
streamlit run app.py
```

The app opens at `http://localhost:8501`. Live camera works locally because `localhost` is treated as a secure origin.

---

## Deployment (Streamlit Community Cloud)

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, select your repo, branch `main`, and main file `app.py`.
4. Click **Deploy**.

The repo includes:
- `requirements.txt` — Python dependencies
- `packages.txt` — no system libraries are required for this app
- `runtime.txt` — pins Python 3.14 for Streamlit Cloud compatibility

Live camera works on the deployed app because Streamlit Cloud serves over HTTPS and WebRTC captures the webcam in the browser.

---

## How Live Camera Works

The webcam is captured client-side in the browser and streamed to the server over WebRTC. Each frame is processed by a `VideoProcessor` that runs MediaPipe pose detection, draws landmarks, overlays analysis text, and streams the result back. A thread-safe config lets the sidebar sliders update the running stream live.

---

## Posture Analysis

For each detected pose, the app computes joint angles and reports:

- **Arms** — straight / bent / highly bent (elbow angle)
- **Legs** — straight / bent (knee angle)
- **Back** — straight / bent posture (shoulder–hip horizontal alignment)

Thresholds are defined in `analyze_pose()` and can be tuned to your needs.

---

## Project Structure

```
pose-detection-app/
├── app.py              # main application
├── requirements.txt    # Python dependencies
├── packages.txt        # system libraries for deployment
├── runtime.txt         # Python version pin
├── .gitignore
└── README.md
```

---

## License

MIT — free to use, modify, and distribute.

---

## Author

**Vishal Kumar** — ML/AI Engineer
Built as a computer-vision portfolio project.
