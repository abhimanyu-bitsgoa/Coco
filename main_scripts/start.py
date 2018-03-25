#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import listen
# obtain audio from the microphone
r = sr.Recognizer()
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
        message='###'
        message=r.recognize_google(audio)
        # print(message)
        if message=='coco':
            listen.listenCommands()
    except sr.UnknownValueError:
        print("")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

