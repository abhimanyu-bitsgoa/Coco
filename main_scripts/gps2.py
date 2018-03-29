#! /usr/bin/python

import os
from gps import *
from time import *
import time
import threading
import geocoder

gpsd = None #seting the global variable

#s.system('clear') #clear the terminal (optional)

street='None'
city='None'
zipcode='None'

class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd #bring it in scope
		gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
		self.current_value = None
		self.running = True #setting the thread running to true

	def run(self):
		global gpsd
		while gpsp.running:
			gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
	gpsp = GpsPoller() # create the thread
	try:
		gpsp.start() # start it up
		while True:
			#It may take a second or two to get good data
			#print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
			os.system('clear')
			latitude=float(gpsd.fix.latitude)
			longitude=float(gpsd.fix.longitude)
			if latitude!=0 and longitude!=0:
				g=geocoder.google([latitude,longitude],method='reverse')
				street=str(g.street_long)
				city=str(g.city)
				zipcode=str(g.postal)
			time.sleep(5) #set to whatever
			#print street+', '+ city+', '+zipcode
			if city == 'None' or city == 'None' or zipcode == 'None':
				continue
			else:
				break

		print street+', '+ city+', '+zipcode
	gpsp.join()
	except:
		print "Error!"
