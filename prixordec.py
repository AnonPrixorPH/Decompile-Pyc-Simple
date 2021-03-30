##### Uncompyle #####
# Author: AnonPrixor
# This is a Public and Simple Script

import os
import sys
import time

def logo():
	print("""
[+]==========================[+]
 #     Pyc > Py Decompiler    #
 # Author: AnonPrixor         #
 # Team: PureXploit           #
[+]==========================[+]
	""")
def uncompyle():
	uncom = input("Enter file to Decompile: ")
	out = input("Outfile: ")
	os.system("uncompyle6 " + uncom + "> " + out)
def report():
	os.system("xdg-open mbasic.facebook.com/botnetmaster1337")
def menu():
	logo()
	print("""
1. Uncompyle pyc > py
2. Report Bug
	""")
	choice1 = input("Choose [1/2]: > ")
	if (choice1 == "1"):
		uncompyle()
	if (choice1 == "2"):
		report()
	
menu()
