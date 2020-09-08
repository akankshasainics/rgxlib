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
		self.assertEqual(rx.find_pattern(r"[^a-z]*\w+", "ak9Agh"), ["ak9Agh"])
		self.assertEqual(rx.find_pattern(r"([\a-z])\w+", "Tree kdfg 7gh"), ["ree", "kdfg", "gh"])
		self.assertEqual(rx.find_pattern(r"a[.]+b", r"a.b "), ["a.b"])




























	# def test_find_pattern(self):
	# 	self.assertEqual(rx.find_pattern("abc", "bc"), -1)
	# 	self.assertEqual(rx.find_pattern("[a-z][0-9]c", "a5ccs"), 2)
	# 	self.assertEqual(rx.find_pattern("abc", "abc"), 2)
	# 	self.assertEqual(rx.find_pattern("[]c", "acsdf"), -1)
	# 	self.assertEqual(rx.find_pattern("xyfggh", "xyz"), -1)

	# def test_match_pattern(self):
	# 	self.assertEqual(rx.match_pattern(r"[\\a-z]", r"\he"), {"h", "e", "\\"})
	# 	self.assertEqual(rx.match_pattern(r"x[^s3+][a-z]", "7xas4-"), {"xas"})
	# 	self.assertEqual(rx.match_pattern(r"\w+\a\6\5\7", "baaa657"), {"baaa657"})
	# 	self.assertEqual(rx.match_pattern(r"[\da]e\w", "7ee8 2emaec"), {"2em", "7ee", "aec"})
	# 	self.assertEqual(rx.match_pattern(r"[a-z\d\\\]]", "[]6\e"), {"6", "e", "]", "\\"})
	# 	self.assertEqual(rx.match_pattern(r"[A-Z][a-z]+", "+eAh+fKa+"), {"Ka+", "Ah+"})
	# 	self.assertEqual(rx.match_pattern(r"\d+", "klsd6fsl"), {"6"})

	# def test_find_closing_bracket(self):
	# 	self.assertEqual(rx.find_closing_bracket("(\())", 0), 3)
	# 	self.assertEqual(rx.find_closing_bracket("([(())])", 1), 6)
	# 	self.assertEqual(rx.find_closing_bracket("[(()]", 0), 4)
	# 	self.assertEqual(rx.find_closing_bracket("(([))", 1), 3)

	# def test_simply_square_bracket(self):
	# 	self.assertEqual(rx.simplify_square_bracket("A-Z"), set(capital_alphabet))
	# 	self.assertEqual(rx.simplify_square_bracket("a+/a-z"), set(small_alphabet + '+' + '/'))
	# 	self.assertEqual(rx.simplify_square_bracket("0-9A-Z"), set(digits+capital_alphabet))
                                                    

if __name__ == "__main__":
	unittest.main()


