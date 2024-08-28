# Construction Safety Detection

## Overview
The **Construction Safety Detection** project leverages the power of AI to enhance safety standards on construction sites. This system uses a YOLO-based object detection model to identify the presence or absence of essential safety equipment like helmets and vests in real-time video streams. When a safety violation is detected, an audible alarm is triggered, allowing for immediate corrective action.

## Features
- **Real-time Detection:** Monitors video footage to identify safety equipment.
- **Alarm System:** Plays an alert sound when violations are detected (e.g., missing helmets or vests).
- **High Accuracy:** Uses the YOLOv8 model for robust and accurate detection.
- **Scalable:** Can be adapted to various video sources, including live camera feeds.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/Construction-Safety.git
   cd Construction-Safety
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the pre-trained YOLO model:**
   - Download and place the `construction_safety.pt` model in the project directory.

4. **Prepare the alarm sound file:**
   - Place your alarm sound file in the specified path or update the path in the script.

## Usage
1. **Run the detection script:**
   ```bash
   python safety_detection.py
   ```

2. **Select video input:**
   - Modify the script to choose between live webcam feed or a video file.

3. **Monitor the output:**
   - The video will display bounding boxes around detected objects, with labels indicating the type of safety equipment detected.

4. **Alarm Management:**
   - The system will play an alarm sound if it detects a "No Helmet" or "No Vest" situation.

## Customization
- **Model Tuning:** Adjust the YOLO model parameters in the script for better performance based on your dataset.
- **Alarm Settings:** Customize the alarm sound file and conditions for triggering the alarm.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests with improvements.

## License
This project is licensed under the MIT License.
