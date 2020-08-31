import unittest
import regex as rx
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'

class TestBasic(unittest.TestCase):

	def test_find_pattern(self):
		self.assertEqual(rx.find_pattern("abc", "bc"), -1)
		self.assertEqual(rx.find_pattern("[a-z][0-9]c", "a5ccs"), 2)
		self.assertEqual(rx.find_pattern("abc", "abc"), 2)
		self.assertEqual(rx.find_pattern("[]c", "acsdf"), -1)
		self.assertEqual(rx.find_pattern("xyfggh", "xyz"), -1)

	def test_match_pattern(self):
		self.assertEqual(rx.match_pattern("x[^s3+][a-z]", "7xas4-"), {"xas"})
		self.assertEqual(rx.match_pattern("[7]x","77x"), {"7x"})
		self.assertEqual(rx.match_pattern("de", "ydealdxe"), {"de"})
		self.assertEqual(rx.match_pattern("((a)[^a-z])", "abcaL"), {"aL"})
		self.assertEqual(rx.match_pattern("[^a-z]+", "A+a+b+"), {"A+"})
		self.assertEqual(rx.match_pattern("[A-Z][a-z]+", "+eAh+fKa+"), {"Ka+", "Ah+"})


	def test_find_closing_bracket(self):
		self.assertEqual(rx.find_closing_bracket("(())", 0), 3)
		self.assertEqual(rx.find_closing_bracket("([(())])", 1), 6)
		self.assertEqual(rx.find_closing_bracket("[(()]", 0), 4)
		self.assertEqual(rx.find_closing_bracket("(([))", 1), 3)

	def test_simply_square_bracket(self):
		self.assertEqual(rx.simplify_square_bracket("A-Z"), set(capital_alphabet))
		self.assertEqual(rx.simplify_square_bracket("a+/a-z"), set(small_alphabet + '+' + '/'))
		self.assertEqual(rx.simplify_square_bracket("0-9A-Z"), set(digits+capital_alphabet))


if __name__ == "__main__":
	unittest.main()


