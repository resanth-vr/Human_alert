from ultralytics import YOLO
import cv2

# ============================
# CONFIGURATION
# ============================
MODEL_PATH = "yolov8n-pose.pt"
CAMERA_INDEX = 0

# ============================
# LOAD MODEL
# ============================
model = YOLO(MODEL_PATH)

# ============================
# START CAMERA
# ============================
cap = cv2.VideoCapture(CAMERA_INDEX)

# Reduce resolution for performance
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

# ============================
# MAIN LOOP
# ============================
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Frame not received")
        break

    # Run YOLO pose detection
    results = model(frame)
    annotated_frame = results[0].plot()

    human_detected = False
    right_hand_up = False
    left_hand_up = False

    # ============================
    # POSE ANALYSIS
    # ============================
    if results[0].keypoints is not None:
        for person in results[0].keypoints.xy:
            human_detected = True

            # Keypoints
            left_shoulder = person[5]
            right_shoulder = person[6]
            left_wrist = person[9]
            right_wrist = person[10]

            # Check hand positions
            if right_wrist[1] < right_shoulder[1]:
                right_hand_up = True

            if left_wrist[1] < left_shoulder[1]:
                left_hand_up = True

    # ============================
    # DISPLAY ALERTS
    # ============================
    height, width, _ = annotated_frame.shape
    y_position = height - 60

    if human_detected:
        cv2.putText(
            annotated_frame,
            "HUMAN DETECTED",
            (width - 300, y_position),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )
        y_position += 30

        if right_hand_up:
            cv2.putText(
                annotated_frame,
                "RIGHT HAND LIFTED",
                (width - 300, y_position),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
            y_position += 30

        if left_hand_up:
            cv2.putText(
                annotated_frame,
                "LEFT HAND LIFTED",
                (width - 300, y_position),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2
            )

    # Show output
    cv2.imshow("YOLOv8 Human Alert System", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ============================
# CLEANUP
# ============================
cap.release()
cv2.destroyAllWindows()
