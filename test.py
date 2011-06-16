#!/usr/bin/env python
import os, unittest;
from lib import get;

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.seq = range(10);

	def test_single_part(self):
		expected = {
			'one': 1,
			'two': 2,
			'three': 3,
			'four': 4,
			'five': 5,
			'six': 6,
			'seven': 7,
			'eight': 8,
			'nine': 9,
			'ten': 10,
			'eleven': 11,
			'twelve': 12,
			'thirteen': 13,
			'fourteen': 14,
			'fifteen': 15,
			'sixteen': 16,
			'seventeen': 17,
			'eighteen': 18,
			'nineteen': 19,
			'twenty': 20,
			'thirty': 30,
			'forty': 40,
			'fifty': 50,
			'sixty': 60,
			'seventy': 70,
			'eighty': 80,
			'ninety': 90
		};
		for test in expected:
			self.assertEqual(get(test), '"' + test + '" parses to ' + str(expected[test]));

	def test_double_part(self):
		expected = {
			'twenty-one': 21,
			'twenty-two': 22,
			'twenty-three': 23,
			'twenty-four': 24,
			'twenty-five': 25,
			'twenty-six': 26,
			'twenty-seven': 27,
			'twenty-eight': 28,
			'twenty-nine': 29,
			'thirty-one': 31,
			'thirty-two': 32,
			'thirty-three': 33,
			'thirty-four': 34,
			'thirty-five': 35,
			'thirty-six': 36,
			'thirty-seven': 37,
			'thirty-eight': 38,
			'thirty-nine': 39,
			'forty-one': 41,
			'forty-two': 42,
			'forty-three': 43,
			'forty-four': 44,
			'forty-five': 45,
			'forty-six': 46,
			'forty-seven': 47,
			'forty-eight': 48,
			'forty-nine': 49,
			'fifty-one': 51,
			'fifty-two': 52,
			'fifty-three': 53,
			'fifty-four': 54,
			'fifty-five': 55,
			'fifty-six': 56,
			'fifty-seven': 57,
			'fifty-eight': 58,
			'fifty-nine': 59,
			'sixty-one': 61,
			'sixty-two': 62,
			'sixty-three': 63,
			'sixty-four': 64,
			'sixty-five': 65,
			'sixty-six': 66,
			'sixty-seven': 67,
			'sixty-eight': 68,
			'sixty-nine': 69,
			'seventy-one': 71,
			'seventy-two': 72,
			'seventy-three': 73,
			'seventy-four': 74,
			'seventy-five': 75,
			'seventy-six': 76,
			'seventy-seven': 77,
			'seventy-eight': 78,
			'seventy-nine': 79,
			'eighty-one': 81,
			'eighty-two': 82,
			'eighty-three': 83,
			'eighty-four': 84,
			'eighty-five': 85,
			'eighty-six': 86,
			'eighty-seven': 87,
			'eighty-eight': 88,
			'eighty-nine': 89,
			'ninety-one': 91,
			'ninety-two': 92,
			'ninety-three': 93,
			'ninety-four': 94,
			'ninety-five': 95,
			'ninety-six': 96,
			'ninety-seven': 97,
			'ninety-eight': 98,
			'ninety-nine': 99,
		};
		for test in expected:
			self.assertEqual(get(test), '"' + test + '" parses to ' + str(expected[test]));

	def test_complex_nums(self):
		expected = {
			'two billion, seven hundred and three thousand, two hundred and forty-seven': 2000703247,
			'two million billion': 2000000000000000,
			'two million billion and seven': 2000000000000007,
			'forty-seven thousand': 47000,
			'forty-two million, forty-three thousand': 42043000,
			'twenty-seven thousand, four hundred and twenty-two': 27422,
			'seven million, four hundred thousand': 7400000,
			'two hundred thousand, four hundred and twenty-seven': 200427,
			'three hundred and forty-seven million, three hundred and forty-seven thousand, three hundred and forty-seven': 347347347,
			'three hundred and eighty-three': 383,
			'one million, seven hundred and thirteen thousand, nine hundred and eighty-two': 1713982,
			'seven hundred and two vigintillion': 702000000000000000000000000000000000000000000000000000000000000000,
			'one novemdecillion, three quintillion sextillion': 1000000000000000000003000000000000000000000000000000000000000,
			'four million, two hundred and seven thousand trillion': 4207000000000000000
		};
		for test in expected:
			self.assertEqual(get(test), '"' + test + '" parses to ' + str(expected[test]));

if __name__ == '__main__':
	os.system(['clear','cls'][os.name == 'nt']);
	print('\033[1mStarting tests:\033[0;0m\n');
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions);
	unittest.TextTestRunner(verbosity=2).run(suite);