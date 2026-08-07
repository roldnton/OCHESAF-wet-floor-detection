import cv2
from ultralytics import YOLO

# 1. Load your newly trained custom model
# YOLO26
# model = YOLO('runs/detect/wet_floor_yolo26/weights/best.pt')
# YOLO11
model = YOLO('runs/detect/wet_floor_yolo11/weights/best.pt')
# RT-DETR-L
#model = YOLO('runs/detect/wet_floor_rtdetr/weights/best.pt')

# 2. Open the camera feed (0 for webcam, or provide a video file path)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    # 3. Run the AI engine on the current frame
    # conf=0.5 means it will only trigger if it is 50%+ confident it is a wet floor
    results = model(frame, conf=0.5)

    # 4. Process outputs (Alert Notifications & Risk Prediction)
    for result in results:
        # If the model detects a bounding box, it found a hazard
        if len(result.boxes) > 0:
            print("⚠️ ALERT: Wet Floor Detected!")
            # Here you could add code to send an email, text, or sound an alarm

    # 5. Draw the bounding boxes and labels on the video frame
    annotated_frame = results[0].plot()

    # 6. Display the dashboard/live feed
    cv2.imshow("Occupational Safety System: Hazard Detection", annotated_frame)

    # Press 'q' to quit the system
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()