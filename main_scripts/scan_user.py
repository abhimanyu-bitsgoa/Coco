# ls_output = subprocess.check_output(['python3', 'recognize.py'])
# print("Output is  = ",ls_output) 

# Python program to illustrate the concept
# of threading
import subprocess
import threading
import os
empl_id='$'

def createLock():
	try:
		f= open("lock","w+")
		f.write("1")
		f.close()
		print("Granting module access")
	except:
		print("File writing failed")
def stopModules():
	try:
		f=open("lock","w")
		f.write("0")
		f.close()
	except:
		print("File writing while stopping failed")
def task1():
	global empl_id
	try:
		ls_output = subprocess.check_output(['python3', 'recognize.py'])
		print("Output is  = ",ls_output) 
		empl_id=ls_output
	except:
		print("camera is happy!")
 
def task2():
	global empl_id
	try:
		ls_output = subprocess.check_output(['python3', 'read_card.py'])
		print("Output is  = ",ls_output) 
		empl_id=ls_output
	except:
		print("RFID is happy!")
 
# if __name__ == "__main__":
 
    # print ID of current process
    # print("ID of process running main program: {}".format(os.getpid()))
 
    # # print name of main thread
    # print("Main thread name: {}".format(threading.main_thread().name))
 
    # creating threads
def startScan():
	createLock()
	t1 = threading.Thread(target=task1)
	t2 = threading.Thread(target=task2)  
	t1.setDaemon(True)
	t2.setDaemon(True)
	# starting threads
	t1.start()
	t2.start()

	# wait until all threads finish
	#t1.join()
	#t2.join()
	while empl_id=='$':
		#print("!")
		pass

	print("I am printing",empl_id)
	stopModules()
	return empl_id
#startScan()
