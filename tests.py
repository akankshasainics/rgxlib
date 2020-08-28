import unittest
import regex as rx
small_alphabet = "abcdefgjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
s = set()
for c in range(ord("A"), ord("Z")+1):
	s.add(chr(c))

class TestBasic(unittest.TestCase):
	def test_find_bracket(self):
		self.assertEqual(rx.find_closing_bracket("(())"), 3)
		self.assertEqual(rx.find_closing_bracket("([(())])"), 7)
		self.assertEqual(rx.find_closing_bracket("[(()]"), 4)
		self.assertEqual(rx.find_closing_bracket("(([))"), 4)

	def test_exapnd_group(self):
		self.assertEqual(rx.expand_group("A-Z"), s)

	def test_simply_square_bracket(self):
		# self.assertEqual(rx.simplify_square_bracket("/"), "invalid pattern")
		self.assertEqual(rx.simplify_square_bracket("A-Z"), set(capital_alphabet))
		self.assertEqual(rx.simplify_square_bracket("A-Z0-9"), set(capital_alphabet+digits))
		self.assertEqual(rx.simplify_square_bracket("/w"), set(capital_alphabet+small_alphabet+digits+'_'))
		self.assertEqual(rx.simplify_square_bracket("a9Z[()]"), {'a', '9', 'Z', '[', ']', '(', ')'})
		self.assertEqual(rx.simplify_square_bracket("^03z!+"), {'0', '3', 'z', '!', '+', '^'})

	def test_square_bracket_pattern(self):
		self.assertEqual(rx.match_square_bracket_pattern("^azgh", "hey you"),[[1,1], [2,2], [3, 3], [4,4], [5,5],[6,6]])
		self.assertEqual(rx.match_square_bracket_pattern("7-+", "15-8=7"), [[2,2], [5, 5]])
		self.assertEqual(rx.match_square_bracket_pattern("0-9", "7a4sdkj"), [[0,0], [2,2]])
		self.assertEqual(rx.match_square_bracket_pattern("5a-zA-Z", "5a9S"), [[0,0], [1,1], [3,3]])
		self.assertEqual(rx.match_square_bracket_pattern("^", "7a"), [[0,0], [1,1]])
		self.assertEqual(rx.match_square_bracket_pattern("", "4dds"), [])


if __name__ == "__main__":
	unittest.main()


