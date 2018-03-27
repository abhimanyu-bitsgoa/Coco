#!/usr/bin/python
import face_recognition
import picamera
import numpy as np
import os

ENCODING_PATH="../imageEncodings/"

def loadDataset(dataset,nameset):
    directory = os.fsencode(ENCODING_PATH)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".npy"):
            dataset.append(np.load(os.path.join(ENCODING_PATH, filename)))
            nameset.append(filename[:-4])




def scanFace():
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    output = np.empty((240, 320, 3), dtype=np.uint8)
    print("Loading known face image(s)")
    # obama_image = face_recognition.load_image_file("abhi.jpg")
    # obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    # npar=np.frombuffer(obama_face_encoding)
    # np.save('test3.npy',npar)
    # d = np.load('test3.npy')

    # Initialize some variables
    face_locations = []
    face_encodings = []
    dataset=[]
    nameset=[]
    loadDataset(dataset,nameset)
    print("Please face the camera")
    while True:
        # Grab a single frame of video from the RPi camera as a numpy array
        camera.capture(output, format="rgb")

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(output)
        # print("Found {} faces in image.".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(output, face_locations)
        # Loop over each face found in the frame to see if it's someone we know.
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(dataset, face_encoding)
            scannedName = "#"
            for name,status in zip(nameset,match):
                if status==True:
                    scannedName = name
                    break

            if scannedName!='#':
                print(scannedName)
                return scannedName
            # print("I see someone named {}!".format(name))
scanFace()
