#!/usr/bin/python
import face_recognition
import picamera
import numpy as np

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)
print(" I have just intialized all the camera")
# print ("printing array before")
# print (output)
# Load a sample picture and learn how to recognize it.
# print("Loading known face image(s)")
# obama_image = face_recognition.load_image_file("abhi.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
# npar=np.frombuffer(obama_face_encoding)

# print("Obama raw image")
# print(obama_image)

# print("Obama face encoding")
# print(obama_face_encoding)
# print("Numpy encoding of Obama")
# print(npar)
# np.save('test3.npy',npar)
d = np.load('test3.npy')
print("I have loaded the array")

# Initialize some variables
face_locations = []
face_encodings = []

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    print("live face encodings")
    print(face_encodings)
    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([d], face_encoding)
        name = "<Unknown Person>"

        if match[0]:
            name = "Barack Obama"

        print("I see someone named {}!".format(name))