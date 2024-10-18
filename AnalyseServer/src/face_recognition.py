import pathlib
import time

import cv2


FILE_PATH = f"{pathlib.Path().resolve()}\\AnalyseServer\\src"
FILE_NAME = "test.mp4"
PRECISION = 10
SCALE = 1.1  # <target_scale>.<original_scale>
MIN_SIZE = 40


def get_faces(
        img,
        face_recognition = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml"),
        scale = SCALE,
        precision = PRECISION,
        min_size = MIN_SIZE
):
    return face_recognition.detectMultiScale(
            cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
            scaleFactor=scale,
            minNeighbors=precision,
            minSize=(min_size, min_size)
        )



def test():
    vid = cv2.VideoCapture(f"{FILE_PATH}\\{FILE_NAME}")
        
    c_frame = 1
    t_frame = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    ok, img = vid.read()
    face_recognition = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while ok:
        timestamp1 = time.time()
        faces = get_faces(img, face_recognition)
        timestamp2 = time.time()

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
            f"Total: {round((timestamp2 - timestamp1) * 1000, 2)}ms",
            (50, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (64, 64, 192),
            2
        )
        cv2.imshow("", img)
        cv2.waitKey(100)

        c_frame += 1
        ok, img = vid.read()
        

if __name__ == "__main__":
    test()
