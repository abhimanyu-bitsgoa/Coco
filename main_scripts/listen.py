import speech_recognition as sr
import speak as sp
from recognize import scanFace
from read_card import scanCard
from scan_user import startScan
def listenCommands():
		# obtain audio from the microphone
		sp.say("How can I help you?")
		print("How can I help you?")
		r = sr.Recognizer()
		while True:
				with sr.Microphone(None,48000,1024) as source:
					# print("How can I help you?")
					audio = r.listen(source,None,3,None)
				try:
					message='#'
					message=r.recognize_google(audio)
					if message=='read face':
						sp.say("Starting Camera, please wait")
						print("Read face!")
						scanFace()
					elif message=='read card':
						sp.say("Starting card reader, please wait")
						print("Read card!")
						scanCard()
					elif message=='read':
						sp.say("starting modules")
						print("starting modules please wait")
						startScan()
					elif message=='exit':
						sp.say("Bye")
						print("Bye!")
						return
					else:
						sp.say("Invalid command")
						# sp.say("Available commands: add user, scanning, entertainment, exit")
						print("Invalid command")
				except sr.UnknownValueError:
						sp.say("I don't understand!")
						print("I could not understand audio")
				except sr.RequestError as e:
						sp.say("Problem with network")
						print("Could not request results from service; {0}".format(e))
