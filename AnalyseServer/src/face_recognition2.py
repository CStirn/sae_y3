import os
import pathlib
import time

import cv2
import dlib


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = f"{ROOT_PATH}"
FILE_NAME = "test.mp4"
START_AT = 1

SCALE = 0.5


def get_faces(
        img,
        detector = dlib.cnn_face_detection_model_v1(f"{ROOT_PATH}{os.sep}mmod_human_face_detector.dat")
):
    res = []
    faces = detector(img, 1)
    for face in faces:
        res.append((
            int(face.rect.left() / SCALE),
            int(face.rect.top() / SCALE),
            int(face.rect.right() / SCALE) - int(face.rect.left() / SCALE),
            int(face.rect.bottom() / SCALE) - int(face.rect.top() / SCALE)
        ))
    return res


def test():
    face_recognition = dlib.cnn_face_detection_model_v1(f"{ROOT_PATH}{os.sep}mmod_human_face_detector.dat")

    vid = cv2.VideoCapture(f"{FILE_PATH}{os.sep}{FILE_NAME}")
        
    c_frame = 1
    t_frame = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    avg_time = 0
    skipped_first = False

    ok, img = vid.read()
    for _ in range(START_AT - 1):
        c_frame += 1
        ok, img = vid.read()

    while ok:
        timestamp1 = time.time()
        if SCALE != 1:
            p_img = cv2.resize(img, (
                int(img.shape[1] * SCALE),
                int(img.shape[0] * SCALE)
            ))
        else:
            p_img = img.copy()
        faces = get_faces(p_img, face_recognition)
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

        if not skipped_first:
            skipped_first = True
        else:
            avg_time += timestamp2 - timestamp1
        print(f"\rFrame {c_frame}/{t_frame}", end="")
        os.makedirs(f"{ROOT_PATH}{os.sep}out", exist_ok=True)
        cv2.imwrite(f"{ROOT_PATH}{os.sep}out{os.sep}out-{(len(str(t_frame)) - len(str(c_frame))) * '0'}{c_frame}.jpg", img)
        """cv2.imshow("", img)
        cv2.waitKey(100)"""

        c_frame += 1
        ok, img = vid.read()

    avg_time /= (t_frame - START_AT) / 1000
    print(f"\rAverage time: {round(avg_time, 2)}ms ({round(1000 / avg_time, 2)} fps)")
        

if __name__ == "__main__":
    test()
