# Real-Time Emotion Detection

This project demonstrates real-time emotion detection from a webcam feed using Python. The implementation leverages the `DeepFace` library for emotion analysis and `OpenCV` for video capture and display.

## Features

- Real-time emotion detection from a webcam feed.
- Display detected emotions over the video feed.
- Supports various emotions such as happiness, sadness, anger, surprise, and more.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.6 or later
- `DeepFace`
- `TensorFlow` (version 2.17.0 recommended)
- `OpenCV`

You can install the required packages using pip:

```bash
pip install deepface tensorflow==2.17.0 opencv-python
```

## Usage

1. **Run the Script**

   Execute the `emotion_detection.py` script to start the real-time emotion detection:

   ```bash
   python emotion_detection.py
   ```

2. **View Results**

   The webcam feed will open, displaying the detected emotion on the video. Press 'q' to exit the application.

## Code Overview

- **`emotion_detection.py`**: Main script for real-time emotion detection. It captures frames from the webcam, analyzes emotions using `DeepFace`, and displays the results.
