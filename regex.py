import sys

bracket_pair = { "(": ")", "[": "]"}
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
groups = {"A-Z": set(capital_alphabet), "a-z": set(small_alphabet), "0-9": set(digits)}
special_pattern = {"(": "solve_parentheese", "[": "solve_square_bracket"}



def find_closing_bracket(string: str, opening_loc: int) -> int:
	stack = 1
	open_brack = string[opening_loc]
	for i, char in  enumerate(string[opening_loc+1:], start = opening_loc+1):
		if char == open_brack:
			stack += 1
		if char == bracket_pair[open_brack]:
			stack -= 1
		if stack == 0:
			return i
	if stack != 0:
		raise ValueError("invalid pattern")


def simplify_square_bracket(pattern: str) -> set():
	if len(pattern) == 0:
		return set()
	i = 0
	if pattern[0] == "^":
		i = 1
	t = False
	chars = set()
	while i < len(pattern):
		if i+2 < len(pattern) and pattern[i:i+3] in groups:
			chars.update(groups[pattern[i:i+3]])
			i = i+3
		else:
			chars.add(pattern[i])
			i += 1

	return chars


def solve_square_bracket(pattern: str, text: str) -> tuple:
	ending_brack =find_closing_bracket(pattern, 0)
	chars = simplify_square_bracket(pattern[1:ending_brack])
	if pattern[1] == "^":
		if text[0] not in chars:
			return True, (1, ending_brack+1)
		
	else:
		if text[0] in chars:
			return True, (1, ending_brack+1)

	return False, (-1, -1)


def solve_special_pattern(pattern: str, text: str) -> tuple:
	if pattern[0] == "[":
		return solve_square_bracket(pattern, text)
	return solve_parentheese[pattern[0]](pattern, text)

def find_pattern(pattern: str, text: str) -> int:
	i = 0
	j = 0
	while i < len(pattern) and j < len(text):
		if pattern[i] in special_pattern:
			is_match, indexes = solve_special_pattern(pattern[i:], text[j:])
			if not is_match:
				return -1
			i += indexes[1]
			j += indexes[0]
		elif pattern[i] == text[j]:
			i += 1
			j += 1
		else:
			break

	if i != len(pattern):
		return -1
	return j - 1



def match_pattern(pattern: str, text: str) -> list:
	result = set()
	for i in range(len(text)):
		index = find_pattern(pattern, text[i:])
		if index != -1:
			result.add(text[i:i+index+1])
	return result


























# if __name__ == "__main__":
# 	length_of_args = len(sys.argv)
# 	args_list = str(sys.argv)
# 	result = match_pattern(args_list[0], args_list[1])
# 	print(result)

