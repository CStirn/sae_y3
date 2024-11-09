import os
import time

import cv2

import face_recognition2


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

FPS = 30


def render(fps = FPS):
    for filename in os.listdir(f"{ROOT_PATH}{os.sep}out"):
        timestamp = time.time()
        img = cv2.imread(f"{ROOT_PATH}{os.sep}out{os.sep}{filename}")
        cv2.imshow("", img)
        keycode = cv2.waitKey(max(1,
            int(1000 / fps) - int((time.time() - timestamp) * 1000)
        ))
        if keycode == 27:
            exit()
        elif keycode == 32:
            keycode = cv2.waitKey()
            while (keycode != 32):
                if keycode == 27:
                    exit()
                keycode = cv2.waitKey()
        

if __name__ == "__main__":
    cam = cv2.VideoCapture(f"{face_recognition2.FILE_PATH}{os.sep}{face_recognition2.FILE_NAME}")
    fps = cam.get(cv2.CAP_PROP_FPS)
    render(fps)
