import os
import time
import traceback

import cv2
import numpy as np
from flask import Flask, request, send_from_directory

import analyse_server


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


# Méthode initialement générée par IA
@app.route("/")
def server_html():
    return send_from_directory("static", "index.html")


# Méthode initialement générée par IA
@app.route("/analyse-server/process", methods=["POST"])
def upload_image():
    # Vérifier si une image est bien envoyée
    if "image" not in request.files:
        return "No image part", 400

    file = request.files["image"]
    if file.filename == "":
        return "No selected file", 400

    try:
        # Lire l'image en mémoire
        in_memory_image = file.read()
        # Convertir l'image en un tableau numpy
        np_img = np.frombuffer(in_memory_image, np.uint8)
        # Décoder l'image avec OpenCV
        frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        
        # Applique les changements nécessaires à l'image
        frame = analyse_server.show_detections(frame)
        
        # Sauvegarder l'image
        path = os.path.join(ROOT_PATH, "static", "out")
        filename = f"{int(time.time_ns() * 10000000)}.png"
        os.makedirs(path, exist_ok=True)
        cv2.imwrite(os.path.join(path, filename), frame)
        
        # Renvoi du lien vers l'image modifiée
        return f"static/out/{filename}"

    except Exception as e:
        print(traceback.format_exc())
        return str(e), 500


def run():
    app.run(debug=True, host="0.0.0.0", port=5000)