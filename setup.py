import os
import time

try:
	os.system("pip install secrets && pip install colorama && pip install requests && pip install pyfiglet")
	time.sleep(1)
	print("Successfuly installed!")
except Exception as e:
	print("Somethings Went Wrong")
	print(e)
