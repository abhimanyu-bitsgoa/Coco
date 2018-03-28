#!/usr/bin/python
import face_recognition
import numpy as np
import os

ENCODING_PATH="../imageEncodings/"
IMAGES_PATH="../images/"
def saveEncoding(filename):
    currentImage = face_recognition.load_image_file(IMAGES_PATH+filename)
    currentImageEncoding = face_recognition.face_encodings(currentImage)[0] #Considering there is only 1 face in the image.
    npar=np.frombuffer(currentImageEncoding)
    np.save(os.path.join(ENCODING_PATH, filename[:-4]),npar)


directory = os.fsencode(IMAGES_PATH)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        saveEncoding(filename)


