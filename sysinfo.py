#!/usr/bin/python

# Script: sysinfo.py
# Author: { GrayCatWhiz }
# Last Update: December 28, 2016
# Description: Tells a bit of information about your Operating System.

import os

OS = os.name
OS_INFO = os.uname() 
OS_HEADER = ['Operating System','Hostname','Kernel Version','Version','Architechture']

if(OS != "posix"):
	print '\tPlease Run Linux.' 
else:
	for index in range(len(OS_INFO)):
			print '\t' + OS_HEADER[index] + ': ' + OS_INFO[index]
