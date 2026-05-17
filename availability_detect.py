import cv2
import time
import os

# Open camera
cap = cv2.VideoCapture(0)

# Face detector
face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

last_seen = time.time()
shutdown_started = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror effect (selfie view)
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    # =========================
    # FACE DETECTED
    # =========================
    if len(faces) > 0:

        last_seen = time.time()
        shutdown_started = False

        text1 = "WELCOME BACK BOSS"
        text2 = "Face verified. System unlocked."

        color = (0, 255, 0)

    # =========================
    # FACE NOT DETECTED
    # =========================
    else:

        elapsed = time.time() - last_seen

        # After 2 sec
        if elapsed > 2 and elapsed <= 5:

            text1 = "BOSS LEFT WORKSTATION"
            text2 = "Initiating shutdown..."

            color = (0, 0, 255)

        # After 5 sec
        elif elapsed > 5:

            text1 = "SYSTEM LOCKED"
            text2 = "Goodbye Boss."

            color = (0, 0, 255)

            # Prevent repeated shutdown commands
            if not shutdown_started:

                shutdown_started = True

                # Shutdown after 3 seconds
                os.system("shutdown /s /t 3")

        else:

            text1 = "SCANNING..."
            text2 = "Waiting for authorized user"

            color = (0, 255, 255)

    # =========================
    # DISPLAY TEXT
    # =========================
    cv2.putText(
        frame,
        text1,
        (40, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    cv2.putText(
        frame,
        text2,
        (40, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    # Optional face rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    # Show window
    cv2.imshow("AI Security System", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()