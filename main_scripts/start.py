#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import speak as sp
import listen as ls
#from scan_user import createLock
# obtain audio from the microphone
r = sr.Recognizer()
sp.say("Wake me up by saying coco")
#createLock()
while True:
    with sr.Microphone(None,48000,1024) as source:
        audio = r.listen(source,None,3,None)
    # recognize speech using Google Speech Recognition
    try:
        # or testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

        # print("Processing")
        message='#'
        message=r.recognize_google(audio)
        if message=='coco':
            ls.listenCommands()
            break
    except sr.UnknownValueError:
        sp.say("I beg your pardon")
        print("I beg your pardon")
        
    except sr.RequestError as e:
        sp.say("There is some problem with the internet connection")
        print("There is some problem with the internet connection")

