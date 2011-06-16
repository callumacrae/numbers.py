#!/usr/bin/env python
import os, sys;
from lib import get;

if sys.version_info[0] < 3:
	print('This application was designed to run for Python3. Get out');
	exit();

#if specified in argv, print and exit
if (len(sys.argv) > 1):
	if (sys.argv[1] == 'test'):
		os.system('./test.py');
		exit();
	print(get(sys.argv[1]));
	exit();

#else print welcome stuff and start the loop
os.system(['clear','cls'][os.name == 'nt']);
print('\033[1mWelcome to numbers.py!\033[0;0m\n');
print('This script attempts to convert numbers from word form to proper numbers.');
print('It is an experiment, so don\'t expect it to work properly.\n');


try:
	while True:
		string = input('Please enter a string to convert to a number: ');
		if (string == 'exit'):
			print('\nThanks for using numbers.py\n\n');
			exit();

		print(get(string) + '\n');

except(KeyboardInterrupt):
	print('\n\nThanks for using numbers.py\n\n');