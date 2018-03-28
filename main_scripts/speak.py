from subprocess import call
from gtts import gTTS
import pygame
#espeak -vmb-us1+f2 "Hi! welcome to Espeak"

def sayRobot(message):

	vocals=["espeak", "-vmb-us1+f3","-s170", message]
	call(vocals) 
def say(message):
	tts = gTTS(text=message, lang='en-us', slow=False)
	tts.save("response.mp3")
	pygame.mixer.init()
	pygame.mixer.music.load("response.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

if __name__ == '__main__':
    say("This is a sample sentence")
