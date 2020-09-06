import sys

bracket_pair = { "(": ")", "[": "]"}
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
groups = {"A-Z": set(capital_alphabet), "a-z": set(small_alphabet), "0-9": set(digits)}
backward_slash_group = {"\d": set(digits), "\w": set(alpha_numeric)}
special_pattern = {"(": "solve_parentheese", "[": "solve_square_bracket", "\\": "solve_backward_slash"}
operators = {"+", "*"}


# def set_for_operators(pattern, text):
# 	chars = set()
# 	pattern_ind = 2
# 	if pattern[0] == "\\":
# 		pattern_ind = 3
# 		if pattern[:2] in backward_slash_group:
# 			chars.update(backward_slash_group[pattern[:2]])
# 		else:
# 			chars.update(pattern[1])
# 	else:
# 		chars.add(pattern[0])
# 	return pattern_ind, chars


# def solve_plus_operator(pattern, text):
# 	pointer = 0
# 	pattern_ind, chars = set_for_operators(pattern, text)
	
# 	while pointer < len(text) and text[pointer] in chars:
# 		pointer += 1
# 	index = pointer

# 	if pointer == len(text) and pattern_ind+1 == len(pattern):
# 		return True, (pointer, pattern_ind)

# 	while pointer != -1:
# 		if find_pattern(pattern[pattern_ind:], text[pointer:]) != -1:
# 			return True, (pointer, pattern_ind)
# 		pointer -= 1

# 	if index >= 1:
# 		return True, (index, pattern_ind)	
# 	return False, (-1, -1)




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


# def solve_parenthese(pattern: str, text: str) -> set:
# 	ending_brack = find_closing_bracket(pattern, 0)
# 	new_pattern = pattern[1:ending_brack]
# 	index = find_pattern(new_pattern, text)
# 	if index == -1:
# 		return False, (-1, -1)
# 	return True, (index+1, ending_brack+1)


# def simplify_square_bracket(pattern: str) -> set:
# 	if len(pattern) == 0:
# 		return set()
# 	i = 0
# 	chars = set()
# 	if pattern[0] == "^":
# 		i = 1
	
# 	while i < len(pattern):
# 		if i+2 < len(pattern) and pattern[i:i+3] in groups:
# 			chars.update(groups[pattern[i:i+3]])
# 			i = i+3
# 		elif pattern[i] == "\\":
# 			if i+1 == len(pattern):
# 				raise ValueError("Dangling backslash")
# 			if pattern[i:i+2] in backward_slash_group:
# 				chars.update(backward_slash_group[pattern[i:i+2]])
# 				i += 2
# 			elif i+3 < len(pattern) and pattern[i+1: i+4] in groups:
# 				chars.update(groups[pattern[i+1: i+4]])
# 				i += 4
# 			else:
# 				chars.update({pattern[i+1]})
# 				i += 2
			
# 		else:
# 			chars.add(pattern[i])
# 			i += 1

# 	return chars


# def solve_square_bracket(pattern: str, text: str) -> tuple:
# 	ending_brack =find_closing_bracket(pattern, 0)
# 	if ending_brack+1 < len(pattern) and pattern[ending_brack+1] in operators:
# 		return solve_operators(pattern, text)
# 	chars = simplify_square_bracket(pattern[1:ending_brack])
# 	if pattern[1] == "^":
# 		if text[0] not in chars:
# 			return True, (1, ending_brack+1)
		
# 	else:
# 		if text[0] in chars:
# 			return True, (1, ending_brack+1)

# 	return False, (-1, -1)



# def solve_backward_slash(pattern, text):
# 	if len(pattern) == 1:
# 		raise ValueError("Dangling backslash")
# 	if len(pattern) >= 3 and pattern[2] in operators:
# 		return solve_operators(pattern, text)
# 	elif (pattern[:2] in backward_slash_group) and (text[0] in backward_slash_group[pattern[:2]]):
# 		return True, (1, 2)
# 	elif text[0] == pattern[1]:
# 		return True, (1, 2)
# 	return False, (-1, -1)
	


# def solve_special_pattern(pattern: str, text: str) -> tuple:
# 	if pattern[0] == "[":
# 		return solve_square_bracket(pattern, text)
# 	elif pattern[0] == "(":
# 		return solve_parenthese(pattern, text)
# 	elif pattern[0] == "\\":
# 		return solve_backward_slash(pattern, text)


# def find_pattern(pattern: str, text: str) -> int:
# 	i = 0
# 	j = 0
# 	while i < len(pattern) and j < len(text):
# 		if pattern[i] in special_pattern:
# 			is_match, indexes = solve_special_pattern(pattern[i:], text[j:])
# 			if not is_match:
# 				return -1
# 			i += indexes[1]
# 			j += indexes[0]

# 		elif i+1 < len(pattern) and pattern[i+1] in operators:
# 			is_match, indexes = solve_operators(pattern[i:], text[j:])
# 			if not is_match:
# 				return -1
# 			i += indexes[1]
# 			j += indexes[0]


# 		elif pattern[i] == ")":
# 			raise ValueError("Unmatched closing bracket")

# 		elif pattern[i] == text[j]:
# 			i += 1
# 			j += 1

# 		else:
# 			break

# 	if i != len(pattern):
# 		return -1
# 	return j - 1



def solve_operators(pattern: str, text: str) -> list:
	index = 0
	match_indexes = []
	while index < len(text):
		match_index = match_regex(pattern, text[index:])
		if match_index == -1:
			break
		match_indexes.append(match_index + index)
		index += match_index 
	return match_indexes



def solve_repetative_pattern(i: int, groups: list, text: str) -> int:

	pattern = groups[i]
	is_parenthese = int(pattern[0] == "(")
	is_plus = (pattern[-1] == "+")
	match_indexes = solve_operators(pattern[is_parenthese: -1-is_parenthese], text)
	l = (len(match_indexes) == 0)
	if l and is_plus:
		return -1, -1
	for index in reversed(match_indexes):
		if i+1 == len(groups) and index == len(text):
			return len(text), len(groups) - i 
		j = match_regex_groups(groups[i+1:], text[index:])
		if j == len(text[index:]):
			return len(text), len(groups) - i

	return match_indexes[-1], 1


def match_regex_groups(groups: list, text: str) -> int:
	text_pointer = 0
	i = 0
	while i < len(groups) and text_pointer < len(text):
		pattern = groups[i]
		if pattern[-1] in operators:
			text_inc, pattern_inc = solve_repetative_pattern(i, groups, text[text_pointer:])
			if text_inc == -1:
				return -1
			text_pointer += text_inc
			i += pattern_inc
			
		elif pattern == text[text_pointer]:
			text_pointer += 1
			i += 1

		else:
			break
	
	if i != len(groups) or text_pointer == 0:
		return -1

	return text_pointer 




def check_for_operator(pattern: str, i: int) -> int:
	if i+1 == len(pattern) or pattern[i+1] not in operators:
		return 0
	return 1



def break_regex(pattern: str) -> list:
	i = 0
	groups = []
	while i < len(pattern):
		if pattern[i] in bracket_pair:
			closing_bracket = find_closing_bracket(pattern, i)
			is_operator = check_for_operator(pattern, closing_bracket)
			if is_operator:
				groups.append(pattern[i: closing_bracket+1+is_operator])
			else:
				groups.append(pattern[i+1: closing_bracket])
			i = (closing_bracket+1+is_operator)

		elif pattern[i] == "\\":
			if i+1 == len(pattern):
				raise ValueError("Dangling backslash.")
			is_operator = check_for_operator(pattern, i+1)
			groups.append(pattern[i: i+2+is_operator])
			i += (2 + is_operator)

		elif pattern[i] == ")":
			raise ValueError("Unmatched closing bracket.")

		else:
			is_operator = check_for_operator(pattern, i)
			groups.append(pattern[i: i+1+is_operator])
			i += (1 + is_operator)

	return groups


def match_regex(pattern: str, text: str) -> int:
	groups = break_regex(pattern)
	return match_regex_groups(groups, text)


def find_pattern(pattern: str, text: str) -> list:
	groups = break_regex(pattern)
	result = []
	i = 0
	while i < len(text):
		index = match_regex_groups(groups, text[i:])
		if index != -1:
			result.append(text[i:i+index])
			i += index
		else:
			i += 1

	return result



























# if __name__ == "__main__":
# 	length_of_args = len(sys.argv)
# 	args_list = str(sys.argv)
# 	result = match_pattern(args_list[0], args_list[1])
# 	print(result)

