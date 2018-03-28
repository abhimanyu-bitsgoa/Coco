#!/usr/bin/env python3

import speech_recognition as sr
from speak import say
from jokes import joke
import face_recognition
import picamera
import numpy as np
import os
import RPi.GPIO as GPIO
import MFRC522
import signal
ENCODING_PATH="../imageEncodings/"



continue_reading = True


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    #print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

def scanCard():
    global continue_reading
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # Welcome message
    #print("Welcome to the MFRC522 data read example")
    #print("Press Ctrl-C to stop.")

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:
        #checkLock()
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        #if status == MIFAREReader.MI_OK:
            #print("Card detected")
        
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            #print("Card read UID: %s,%s,%s,%s",uid[0], uid[1], uid[2], uid[3])
        
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                emp_id = MIFAREReader.MFRC522_Read(8)
                MIFAREReader.MFRC522_StopCrypto1()
                if(len(emp_id)==6):
                    continue_reading = False
                    print(emp_id)
                    return emp_id

            else:
                print("Authentication error")
                return '#'
    return '#'


def loadDataset(dataset,nameset):
    directory = os.fsencode(ENCODING_PATH)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".npy"):
            dataset.append(np.load(os.path.join(ENCODING_PATH, filename)))
            nameset.append(filename[:-4])




def scanFace():
    flag="1"
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
    say("Please face the camera")
    scannedName="#"
    while flag=="1":
        #checkLock()
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
            for name,status in zip(nameset,match):
                if status==True:
                    scannedName = name
                    break

            if scannedName!='#':
                print(scannedName)
                flag="0"
                break
    camera.close()
    say(scannedName)
    return scannedName

def listenCommands():
        # obtain audio from the microphone
        say("How can I help you?")
        print("How can I help you?")
        r = sr.Recognizer()
        message='#'
        while message=='#':
                with sr.Microphone(None,48000,1024) as source:
                    # print("How can I help you?")
                    audio = r.listen(source,None,3,None)
                try:
                    message=r.recognize_google(audio)
                    if message=='read face':
                        say("Starting Camera, please wait")
                        print("Read face!")
                        print(" Face is ",scanFace())
                    elif message=='read card':
                        say("Starting card reader, please wait")
                        print("Read card!")
                        ans=scanCard()
                        print(" this is my data ", ans)
                    elif message=='joke':
                        jokeText=joke()
                        print(jokeText)
                        say(jokeText)
                    elif message=='exit':
                        say("Bye")
                        print("Bye!")
                        return
                    else:
                        say("Invalid command")
                        message='#'
                        print("Invalid command")
                except sr.UnknownValueError:
                        say("I don't understand!")
                        print("I could not understand audio")
                except sr.RequestError as e:
                        say("Problem with network")
                        print("Could not request results from service; {0}".format(e))











r = sr.Recognizer()
say("Wake me up by saying coco")
while True:
    with sr.Microphone(None,48000,1024) as source:
        audio = r.listen(source,None,3,None)
    try:
        message='#'
        message=r.recognize_google(audio)
        if message=='coco':
            listenCommands()
    except sr.UnknownValueError:
        say("I beg your pardon")
        print("I can't hear you properly")
        
    except sr.RequestError as e:
        say("There is no internet connection")
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


