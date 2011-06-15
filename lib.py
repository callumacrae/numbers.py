if __name__ == '__main__':
	print('This is a library. Get out.')
	exit()

nums = {
	'quarter': 0.25,
	'half': 0.5,
	'one': 1,
	'two': 2,
	'three': 3,
	'thir': 3,
	'for': 4,
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

	if (string.find(' ')  == -1): #single word
		if (string.replace('ty', '') in nums):
			return nums[string.replace('ty', '')] * 10

		if (string.replace('teen', '') in nums):
			return nums[string.replace('teen', '')] + 10

	return -1

def get(string):
	try:
		float(string)
		return 'That\'s already an int!'
	except(ValueError):
		cont = 1

	parsed_string = parse(string)
	if (parsed_string == -1):
		return 'Failed to parse string.'
	else:
		return '"' + string + '" parses to ' + str(parsed_string)