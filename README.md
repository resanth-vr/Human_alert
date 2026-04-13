# YOLOv8 Human Detection & Hand Raise Alert System

Overview
  This project is a real-time computer vision application built using **YOLOv8 Pose Estimation** and OpenCV. It detects human presence through a webcam and identifies hand-raise gestures (left and right hands) by analyzing body keypoints.
  The system is designed as a foundational AI-based monitoring solution that can be extended into security systems, smart classrooms, and gesture-based interaction systems.

Features
* Real-time human detection
* Right-hand raise detection
* Left-hand raise detection
* Live webcam video processing 
* Fast and lightweight using YOLOv8n-pose model
* Keypoint-based pose analysis

Technologies Used
* Python
* Ultralytics YOLOv8
* OpenCV
* NumPy (internally used)

Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/yolo-human-alert.git
cd yolo-human-alert
```
2. Create virtual environment 
```bash
python -m venv vijay
source vijay/bin/activate   # Linux/Mac
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

Usage
Run the main script:

```bash
python main.py

```
How It Works
* The YOLOv8 Pose model detects human keypoints (shoulders, elbows, wrists).
* The system checks if wrist positions are above shoulder positions.
* If detected:
  * Displays **"HUMAN DETECTED"**
  * Displays **"RIGHT HAND LIFTED"** or **"LEFT HAND LIFTED"**

Model Used
* YOLOv8n Pose (pretrained model)
* Automatically downloaded on first run

imitations
* Works best when the person is visible to the camera
* Accuracy may drop in low light or occluded views
* Not optimized for multi-person tracking

Future Enhancements
* Audio alert system
* Mobile notifications
* Video recording on detection
* Web-based live streaming
* Multi-person tracking support

Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.

License
This project is open-source and available under the MIT License.
