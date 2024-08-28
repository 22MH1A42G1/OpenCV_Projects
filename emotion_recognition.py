import cv2
from deepface import DeepFace
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

def analyze_emotion(frame):
    # Convert the frame from BGR (OpenCV format) to RGB (DeepFace format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        # Analyze the image to detect emotions
        emotion_analysis = DeepFace.analyze(frame_rgb, actions=['emotion'])
        # Get the dominant emotion
        dominant_emotion = emotion_analysis[0]['dominant_emotion']
        return dominant_emotion
    except Exception as e:
        print(f"Error during emotion detection: {e}")
        return "Unknown"

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Analyze emotion
    emotion = analyze_emotion(frame)

    # Display the resulting frame with emotion
    cv2.putText(frame, f'Emotion: {emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Emotion Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
