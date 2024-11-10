import os
import time

import cv2

import face_recognition


COLOR_TEXT = (64, 64, 192)
COLOR_FACES = (0, 255, 0)


def show_detections(frame,
    current_frame="-",
    total_frames="-"
):
    # Apply every detection
    timestamp1 = time.time()
    faces = face_recognition.get_faces(frame)
    timestamp2 = time.time()

    # Clone the image to keep the initial image
    frame = frame.copy()

    # Draw rectangles for every detected element
    for (x1, y1, x2, y2) in faces:
        cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_FACES, 3)

    # Put texts in the image
    cv2.putText(
        frame,
        f"Frame {current_frame}/{total_frames}",
        (50, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (64, 64, 192),
        4
    )
    cv2.putText(
        frame,
        f"Done in {round((timestamp2 - timestamp1) * 1000, 2)}ms",
        (50, 135),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (64, 64, 192),
        2
    )
    
    return frame


if __name__ == "__main__":
    import flask_server
    flask_server.run()
