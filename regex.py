import sys

bracket_pair = { "(": ")", "[": "]"}
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
groups = {"A-Z": set(capital_alphabet), "a-z": set(small_alphabet), "0-9": set(digits)}
backward_slash_group = {"\d": set(digits), "\w": set(alpha_numeric)}
special_pattern = {"(": "solve_parentheese", "[": "solve_square_bracket", "\\": "solve_backward_slash"}



def find_closing_bracket(string: str, opening_loc: int) -> int:
	stack = 1
	open_brack = string[opening_loc]
	backslash = 0
	for i, char in  enumerate(string[opening_loc+1:], start = opening_loc+1):
		if char == open_brack and backslash%2 == 0:
			stack += 1
		if char == bracket_pair[open_brack] and backslash%2 == 0:
			stack -= 1
		if stack == 0:
			return i
		if char == "\\":
			backslash += 1
		else:
			backslash = 0

	if stack != 0:
		raise ValueError("Unmatched opening bracket.")


def solve_parenthese(pattern: str, text: str) -> set:
	ending_brack = find_closing_bracket(pattern, 0)
	new_pattern = pattern[1:ending_brack]
	index = find_pattern(new_pattern, text)
	if index == -1:
		return False, (-1, -1)
	return True, (index+1, ending_brack+1)


def simplify_square_bracket(pattern: str) -> set:
	if len(pattern) == 0:
		return set()
	i = 0
	chars = set()
	if pattern[0] == "^":
		i = 1
	
	while i < len(pattern):
		if i+2 < len(pattern) and pattern[i:i+3] in groups:
			chars.update(groups[pattern[i:i+3]])
			i = i+3
		elif pattern[i] == "\\":
			if i+1 == len(pattern):
				raise ValueError("Dangling backslash")
			if pattern[i:i+2] in backward_slash_group:
				chars.update(backward_slash_group[pattern[i:i+2]])
			else:
				chars.update({pattern[i+1]})
			i += 2
			
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



def solve_backward_slash(pattern, text):
	if len(pattern) == 1:
		raise ValueError("Dangling backslash")
	if (pattern[:2] in backward_slash_group) and (text[0] in backward_slash_group[pattern[:2]]):
		return True, (1, 2)
	elif text[0] == pattern[1]:
		return True, (1, 2)
	return False, (-1, -1)
	


def solve_special_pattern(pattern: str, text: str) -> tuple:
	if pattern[0] == "[":
		return solve_square_bracket(pattern, text)
	elif pattern[0] == "(":
		return solve_parenthese(pattern, text)
	elif pattern[0] == "\\":
		return solve_backward_slash(pattern, text)


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

