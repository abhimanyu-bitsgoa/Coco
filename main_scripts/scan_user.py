import subprocess
ls_output = subprocess.check_output(['bash', 'person_scan.sh'])
print("Output is  = ",ls_output) 