# ls_output = subprocess.check_output(['python3', 'recognize.py'])
# print("Output is  = ",ls_output) 

# Python program to illustrate the concept
# of threading
import subprocess
import threading
import os
empl_id='$' 
def task1():
	global empl_id
	ls_output = subprocess.check_output(['python3', 'recognize.py'])
	print("Output is  = ",ls_output) 
	empl_id=ls_output
 
def task2():
	global empl_id
	ls_output = subprocess.check_output(['python3', 'read_card.py'])
	print("Output is  = ",ls_output) 
	empl_id=ls_output
 
# if __name__ == "__main__":
 
    # print ID of current process
    # print("ID of process running main program: {}".format(os.getpid()))
 
    # # print name of main thread
    # print("Main thread name: {}".format(threading.main_thread().name))
 
    # creating threads
def startScan():
	t1 = threading.Thread(target=task1,)
	t2 = threading.Thread(target=task2,)  
	t1.setDaemon(True)
	t2.setDaemon(True)
	# starting threads
	t1.start()
	t2.start()

	# wait until all threads finish
	# t1.join()
	# t2.join()
	while empl_id=='$':
		print("!")
	print("I am printing",empl_id)
	return empl_id
startScan()