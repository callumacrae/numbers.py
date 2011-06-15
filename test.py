import os, unittest
from lib import get

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.seq = range(10)

	def test_simple_nums(self):
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
		}
		for test in expected:
			self.assertEqual(get(test), '"' + test + '" parses to ' + str(expected[test]))

if __name__ == '__main__':
	os.system(['clear','cls'][os.name == 'nt'])
	print('\033[1mStarting tests:\033[0;0m\n')
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
	unittest.TextTestRunner(verbosity=2).run(suite)