import speech_recognition as sr

def listenCommands():
	# obtain audio from the microphone
	print("I am listening!")
	r = sr.Recognizer()
	while True:
		with sr.Microphone(None,48000,1024) as source:
		    print("What do you want me to do?")
		    audio = r.listen(source,None,3,None)
		try:
		    message='###'
		    message=r.recognize_google(audio)
		    if message=='add user':
		        print ("Adding user!")
		    elif message=='scan':
		    	print("Scanning!")
		    elif message=='entertainment':
		        print("Are you having fun :P ")
		    elif message=='exit':
		    	print("Bye!")
		    	return
		    else:
		    	print("I can't hear you!")
		    	 
		except sr.UnknownValueError:
		    print("Google Speech Recognition could not understand audio")
		    
		except sr.RequestError as e:
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))

