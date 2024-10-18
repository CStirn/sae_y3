import pathlib
import time

import cv2


def test():
    file_path = f"{pathlib.Path().resolve()}\\AnalyseServer\\src"
    file_name = "test.mp4"
    vid = cv2.VideoCapture(f"{file_path}\\{file_name}")
        
    c_frame = 1
    t_frame = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    ok, img = vid.read()
    face_recognition = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while ok:
        timestamp1 = time.time()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        timestamp2 = time.time()
        faces = face_recognition.detectMultiScale(
            img_gray, scaleFactor=1.1, minNeighbors=10, minSize=(40, 40)
        )
        timestamp3 = time.time()

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

        cv2.putText(
            img,
            f"Frame {c_frame}/{t_frame}",
            (50, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (64, 64, 192),
            4
        )
        cv2.putText(
            img,
            f"Total: {round((timestamp3 - timestamp1) * 1000, 2)}ms",
            (50, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (64, 64, 192),
            2
        )
        cv2.putText(
            img,
            f"Grayscale: {round((timestamp2 - timestamp1) * 1000, 2)}ms",
            (50, 175),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (64, 64, 192),
            2
        )
        cv2.putText(
            img,
            f"Recognition: {round((timestamp3 - timestamp2) * 1000, 2)}ms",
            (50, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (64, 64, 192),
            2
        )
        cv2.imshow("", img)
        cv2.waitKey(100)

        c_frame += 1
        ok, img = vid.read()
        

test()