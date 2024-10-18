import os
import sys

import cv2

from behave import when, then

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
import face_recognition


@when("The image {filename} is sent to the server")
def input_image_from_file(context, filename):
    context.image = cv2.imread(os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "resources",
        "data_analysis",
        filename
    ))


@then("The element at ({x},{y}) is detected")
def check_element_in_image(context, x, y):
    x = int(x)
    y = int(y)

    faces = face_recognition.get_faces(context.image)

    found = False
    for (start_x, start_y, width, height) in faces:
        if (
            (
                start_x <= x and
                (start_x + width) >= x
            ) and (
                start_y <= y and
                (start_y + height) >= y
            )
        ):
            found = True
            break
    
    assert found
