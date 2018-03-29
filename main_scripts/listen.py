import speech_recognition as sr
import speak as sp
from recognize import scanFace
from read_card import scanCard
from jokes import joke
from demo_gps import getAddress, getTimestamp
from send_data import sendDb 

def recordAttendance(emplid):
	address=getAddress()
	time=getTimestamp()
	sendDb(emplid,address,time)

def listenCommands():
		# obtain audio from the microphone
		sp.say("How can I help you?")
		print("How can I help you?")
		r = sr.Recognizer()
		message='#'
		while True:
				with sr.Microphone(None,48000,1024) as source:
					# print("How can I help you?")
					audio = r.listen(source,None,3,None)
				try:
					message=r.recognize_google(audio)
					print(message)
					if message=='read face':
						sp.say("Starting Camera, please wait")
						print("Read face!")
						emplid=scanFace()
						recordAttendance(emplid)
						break
					elif message=='read card':
						sp.say("Starting card reader, please wait")
						print("Read card!")
						emplid=scanCard()
						recordAttendance(emplid)
						break
					elif message=='joke':
						jokeText=joke()
						print(jokeText)
						sp.say(jokeText)
					elif message=='exit':
						sp.say("Bye")
						print("Bye!")
						return
					else:
						sp.say("Invalid command")
						print("Invalid command")
				except sr.UnknownValueError:
						sp.say("I beg your pardon!")
						print("I beg your pardon!")
				except sr.RequestError as e:
						sp.say("Problem with network")
						print("Problem with network")
