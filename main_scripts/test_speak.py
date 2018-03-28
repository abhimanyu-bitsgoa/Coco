from subprocess import call
#espeak -vmb-us1+f2 "Hi! welcome to Espeak"
vocals=["espeak", "-vmb-us1+f3","-s170", "Hello, I am espeak"]
call(vocals) 
