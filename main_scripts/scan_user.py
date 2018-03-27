#!/usr/bin/python
import read_card as scn
import recognize as re
import _thread as thread
import time


# Create two threads as follows
try:
   thread.start_new_thread( re.scanFace())
   thread.start_new_thread( scn.scanCard())
except:
   print ("Error: unable to start thread")

print ("Starting card reader")
scn.scanCard()