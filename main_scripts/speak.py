from subprocess import call
#espeak -vmb-us1+f2 "Hi! welcome to Espeak"

def say(message):

	vocals=["espeak", "-vmb-us1+f3","-s170", message]
	call(vocals) 
