import os

import cv2
import dlib


_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

PROCESS_SCALE = 1


# Various pre-processing functions to make the face detection faster
def _pre_process(frame):
    # Resize the image
    frame = cv2.resize(frame, (
                int(frame.shape[1] * PROCESS_SCALE),
                int(frame.shape[0] * PROCESS_SCALE)
            ))
    # Make the image black and white
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame


# Used if CUDA support isn't enabled
def _get_faces_cpu(frame):
    # Pre-process the image
    frame = _pre_process(frame)

    # Get the faces
    faces = _DETECTOR(frame)

    # Normalize the output [(x1, y1, x2, y2)]
    res = []
    for face in faces:
        res.append((
            int(face.left() / PROCESS_SCALE),
            int(face.top() / PROCESS_SCALE),
            int(face.right() / PROCESS_SCALE),
            int(face.bottom() / PROCESS_SCALE)
        ))

    # Return the faces
    return res


# Used if CUDA support is enabled
def _get_faces_gpu(frame):
    # Pre-process the image
    frame = _pre_process(frame)

    # Get the faces
    faces = _DETECTOR(frame)

    # Normalize the output [(x1, y1, x2, y2)]
    res = []
    for face in faces:
        res.append((
            int(face.rect.left() / PROCESS_SCALE),
            int(face.rect.top() / PROCESS_SCALE),
            int(face.rect.right() / PROCESS_SCALE),
            int(face.rect.bottom() / PROCESS_SCALE)
        ))

    # Return the faces
    return res


# Select the right get_faces function depending on if CUDA support is enabled
if dlib.DLIB_USE_CUDA:
    _DETECTOR = dlib.cnn_face_detection_model_v1(os.path.join(_ROOT_PATH, "models", "mmod_human_face_detector.dat"))
    get_faces = _get_faces_gpu
else:
    _DETECTOR = dlib.get_frontal_face_detector()
    get_faces = _get_faces_cpu
