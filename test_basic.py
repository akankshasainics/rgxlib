import unittest
import regex as rx
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'

class TestBasic(unittest.TestCase):
	def test_break_regex(self):
		self.assertEqual(rx.break_regex(r"\s+(as+)+[a-z]+"), ["\s+", "(as+)+", "[a-z]+"])
		self.assertEqual(rx.break_regex(r"a.+"), ["a", ".+"])

	def test_find_pattern(self):
		self.assertEqual(rx.find_pattern(r"[\d]+(([\a]))+\w*", r"67aa7a 5a7"), ["67aa7a", "5a7"])
		self.assertEqual(rx.find_pattern(r"((b)*(a)+c)+", r"baacbacac"), ["baacbacac"])
		self.assertEqual(rx.find_pattern(r"(([^a-z])*(\w+))", "ak9Agh"), ["ak9Agh"])
		self.assertEqual(rx.find_pattern(r"[0-4]*.+", r"740abcd12ba"), ["740abcd12ba"])
		self.assertEqual(rx.find_pattern(r"\S\W+\D", r"!?a#a"), ["!?a"])
		self.assertEqual(rx.find_pattern(r"[a-z\d]+\w+", r"asdf6 a"), ["asdf6"])


if __name__ == "__main__":
	unittest.main()


