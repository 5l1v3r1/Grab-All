#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# ---------------------------------------------
#           A N R O I D   G R A B             |
# - - -  - - -   - - -   - - -  - - -  - - -  |
#                                             |
#  * https://github.com/CRO-THEHACKER         |
#  * http://thedarkarmy.ml/                   |
#                                             |
# - - -  - - -   - - -   - - -  - - -  - - -  |
#                                             |
#   AndroidGrab.py is an script for grabbing  |
#  All info about an android phone.           |
#                                             |
#  1.) to start you must just type in all t-  |
#  he info in the command line.               |
#                                             |
#  2.) Allow access on the phone. Make sure   |
#  to have it as `This Phone :: Tranferring   |
#  files` on the android devise.              |
#                                             |
#  3.) Done. Just wait and everything will    |
#  just load and make an CSV & JSON file on   |
#  the PC.                                    |
#----------------------------------------------

import re, os, csv, sys, time, json, subprocess
from sys import platform
import usb.core

if platform == "linux" or platform == "linux2":
    theos = 'linux'
elif platform == "darwin":
    theos = 'osx'
elif platform == "win32":
    theos = 'windows'

def clearscr():
    if theos == 'win':
        os.system('cls')
    elif theos == 'osx':
        os.system('clear')
    elif theos == 'lin':
        os.system('clear')
    else:
        print("AG: Couldnt find OS.. '{}', isn't found..".format(theos))

if sys.version_info <= (3, 0):
    sys.stdout.write("Sorry, requires Python 3.x, not Python 2.x\n")
    sys.exit(1)

#  - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -  - - -   - - -   - - -   - - -

def fphone():

	print("Make sure to put on 'USB-Debugging' under DEV settings on the phone...")
	if theos == 'win':
		print("windows")
	elif theos == 'lin':
		print("linux")
#  - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -  - - -   - - -   - - -   - - -

print("[!] AG: Starting Android Grab...\n\n")
time.sleep(2)

print(theos)
print('''
            - - - USB :: Phone [?] - - -
    
    1.)  Find Phone
    2.)  
    3.)  Exit
''')

#while True:
#    usbdev = input("AG$> ")
#    if usbdev == '1':
#        fphone()
#    if usbdev == '2':
#        pass
#    if usbdev == '3':
#        sys.exit(1)
#    else:
#        print("AG: Unknown input {}".format(usbdev))

usbdev = 'data123'
data = b{
	'{"usbhost":"{0}"}}'.format(usbdev),
	'{"OS":"
}

with open('.rb/vars.json', 'w') as outfile:
    json.dump(data, outfile)
