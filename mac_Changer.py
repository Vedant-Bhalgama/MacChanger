import subprocess
import re
import pyfiglet
import sys
import time

result = pyfiglet.figlet_format("Mac-Changer", font = "slant"  ) 
print(result) 

print("[+] Mac Address Changer for Linux OS")
print("[+] Version 1.1.0")
print("[+] Build Date : 21/7/2020")
print("[+] Last Updated : 21/7/2020")
time.sleep(5)

def clear_output():
	# for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def mac_changer():
	try:
		net_int = raw_input("[+] Please select the network interface (eg. eth0) >> ")
		new_mac = raw_input("[+] Please enter new Mac Address >> ")
		subprocess.call(["ifconfig " + net_int + "down"])
		subprocess.call(["ifconfig " + net_int + "hw " + "ether " + new_mac])
		subprocess.call(["ifconfig " + net_int + "up"])
		print("[+] New Mac Address has been changed successfully to " + new_mac)
		print_output = raw_input("[+] Do you want to print the result of the new mac y/n >> ")
		clear()
		try:
			if "y" in print_output:
				subprocess.call("ifconfig", shell=True)
				sys.exit
			if "n" in print_output:
				sys.exit()
		except:
			print("[+] Please type the correct choice y/n")
	except:
		print("[+] Error while changing Mac Address, Please run again the script")


mac_changer()
