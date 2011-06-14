import os, sys

if sys.version_info[0] < 3:
	print('This application was designed to run for Python3. Get out')
	exit()

os.system(['clear','cls'][os.name == 'nt'])

print('Welcome to numbers.py!\n')
print('This script attempts to convert numbers from word form to proper numbers.')
print('It is an experiment, so don\'t expect it to work properly.\n')

nums = {
	'quarter': 0.25,
	'half': 0.5,
	'one': 1,
	'two': 2,
	'three': 3,
	'thir': 3,
	'four': 4,
	'five': 5,
	'fif': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'eigh': 8,
	'nine': 9,
	'ten': 10,
	'eleven': 11,
	'twelve': 12,
	'twenty': 20,
	'hundred': 100,
	'thousand': 1000,
	'million': 1000000
};

def parse(string):
	if (string in nums):
		return nums[string]
	return -1

try:
	while True:
		string = input('Please enter a string to convert to a number: ')
		if (string == 'exit'):
			print('\nThanks for using numbers.py\n\n')
			exit()

		try:
			float(string)
			print('That\'s already an int!\n')
			continue
		except(ValueError):
			while(0):
				print('what?')

		parsed_string = parse(string)
		if (parsed_string == -1):
			print('Failed to parse string.')
		else:
			print('"' + string + '" parses to ' + str(parsed_string))

		print() #new line

except(KeyboardInterrupt):
	print('\n\nThanks for using numbers.py\n\n')