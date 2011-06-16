if __name__ == '__main__':
	print('This is a library. Get out.');
	exit();

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

#uses the american system of powers of ten
tens = [
	['vigintillion', 63],
	['novemdecillion', 60],
	['octodecillion', 57],
	['septendecillion', 54],
	['sexdecillion', 51],
	['quindecillion', 48],
	['quattuordecillion', 45],
	['tredecillion', 42],
	['duodecillion', 39],
	['undecillion', 36],
	['decillion', 33],
	['nonillion', 30],
	['octillion', 27],
	['septillion', 24],
	['sextillion', 21],
	['quintillion', 18],
	['quadrillion', 15],
	['trillion', 12],
	['billion', 9],
	['million', 6],
	['thousand', 3],
	['hundred', 2]
];

def parse(string):
	if (string in nums):
		return nums[string];

	if (string.find(' ')  == -1): #single word
		if (string.replace('ty', '') in nums):
			return nums[string.replace('ty', '')] * 10;

		if (string.replace('teen', '') in nums):
			return nums[string.replace('teen', '')] + 10;

		parts = string.partition('-');
		if (parts[1] == '-'):
			return parse(parts[0]) + parse(parts[2]);

	end = 0;

	for ten in tens:
		parts = string.partition(' ' + ten[0]);
		if (parts[1] == ' ' + ten[0]):
			end += parse(parts[0]) * 10 ** ten[1];
			string = parts[2];
			if (string.find(', ') == 0):
				string = string.replace(', ', '', 1);

	parts = string.rpartition(' and ');
	if (parts[1] == ' and '):
		end += parse(parts[2]);

	return end;

def get(string):
	try:
		float(string);
		return 'That\'s already an int!';
	except(ValueError):
		cont = 1;

	parsed_string = parse(string);
	if (parsed_string == -1):
		return 'Failed to parse string.';
	else:
		return '"' + string + '" parses to ' + str(parsed_string);