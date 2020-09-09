import sys
import typing as t

bracket_pair = { "(": ")", "[": "]"}
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
white_spaces = {" ", "	", "\n"}
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
set_of_ranges = {"A-Z": set(capital_alphabet), "a-z": set(small_alphabet), "0-9": set(digits)}
backward_slash_group = {"\d": set(digits), "\w": set(alpha_numeric), "\s" : white_spaces}
operators = {"+", "*"}


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



def solve_range(pattern: str) -> t.Set[chr]:
	if pattern in set_of_ranges:
		return set_of_ranges[pattern]
	if pattern[0] > pattern[-1]:
		raise ValueError("Range value reversed. Start char code is greater than end char code.")
	s = set()
	for c in range(ord(pattern[0]), ord(pattern[2])+1):
		s.add(chr(c))

	return s



def parse_chars_class(pattern: str) -> t.Set[chr]:
	if len(pattern) == 0:
		return set()
	i = 0
	chars = set()
	if pattern[0] == "^":
		i = 1
	while i < len(pattern):
		if i+2 < len(pattern) and pattern[i+1] == "-":
			chars.update(solve_range(pattern[i:i+3]))
			i = i+3
		elif pattern[i:i+2] in backward_slash_group:
			chars.update(backward_slash_group[pattern[i:i+2]])
			i += 2

		elif pattern[i] == "\\":
			if i+1 == len(pattern):
				raise ValueError("Dangling backslash")
			
			elif i+3 < len(pattern) and pattern[i+2] == "-":
				chars.update(solve_range(pattern[i+1: i+4]))
				i += 4
			else:
				chars.update({pattern[i+1]})
				i += 2
		else:
			chars.add(pattern[i])
			i += 1

	return chars


def solve_square_bracket(pattern: str, text: str) -> t.Tuple[int]:
	ending_brack =find_closing_bracket(pattern, 0)
	chars = parse_chars_class(pattern[1:ending_brack])
	if pattern[1] == "^":
		if text[0] not in chars:
			return 1
		
	else:
		if text[0] in chars:
			return 1

	return -1



def solve_backward_slash(pattern: str, text: str) -> int:
	if len(pattern) == 3:
		 return solve_repetative_pattern(pattern[:-1], text)
	if (pattern[:2] in backward_slash_group) and (text[0] in backward_slash_group[pattern[:2]]):
		return 1
	elif (pattern[:2] == "\S") and (text[0] not in white_spaces):
		return 1
	elif (pattern[:2] == "\D") and (text[0] not in set(digits)):
		return 1
	elif (pattern[:2] == "\W") and (text[0] not in set(alpha_numeric)):
		return 1
	elif text[0] == pattern[1]:
		return 1
	return -1


def match_indexes_for_operators(pattern: str, text: str) -> t.List[int]:
	index = 0
	match_indexes = []
	while index < len(text):
		match_index = match_regex(pattern, text[index:])
		if match_index == -1:
			break
		match_indexes.append(match_index + index)
		index += match_index 

	return match_indexes



def solve_repetative_pattern(i: int, groups: t.List[str], text: str) -> t.Tuple[int, int]:
	pattern = groups[i]
	is_parenthese = int(pattern[0] == "(")
	is_plus = (pattern[-1] == "+")
	match_indexes = match_indexes_for_operators(pattern[is_parenthese: -1-is_parenthese], text)
	l = (len(match_indexes) == 0)
	if l and is_plus:
		return -1, -1
	elif l and not is_plus:
		return 0, 1

	for index in reversed(match_indexes):
		j = match_regex_groups(groups[i+1:], text[index:])
		if j != -1:
			return index +j, len(groups) - i
	
	return -1, 0


def solve_dot(pattern: str, text: str) -> int:
	if pattern == "\n":
		return -1
	return 1

	

def match_regex_groups(groups: list, text: str) -> int:
	text_pointer = 0
	i = 0
	while i < len(groups) and text_pointer < len(text):
		pattern = groups[i]
		if pattern[-1] in operators:
			text_inc, pattern_inc = solve_repetative_pattern(i, groups, text[text_pointer:])
			if i+pattern_inc == len(groups):
				return text_pointer + text_inc

		elif pattern[0] == "(":
			text_inc = match_regex(pattern[1:-1], text[text_pointer:])

		elif pattern[0] == "[":
			text_inc= solve_square_bracket(pattern, text[text_pointer:])

		elif pattern[0] == "\\":
			text_inc = solve_backward_slash(pattern, text[text_pointer])

		elif pattern == ".":
			text_inc = solve_dot(pattern, text[text_pointer:])
			
		elif pattern == text[text_pointer]:
			text_inc = 1

		else:
			break

		if text_inc == -1:
			return -1
		text_pointer += text_inc
		i += 1
		
	
	if i != len(groups):
		return -1

	return text_pointer 




def check_for_operator(pattern: str, i: int) -> int:
	if i+1 == len(pattern) or pattern[i+1] not in operators:
		return 0
	return 1


def break_regex(pattern: str) -> t.List[str]:
	i = 0
	groups = []
	while i < len(pattern):
		if pattern[i] == ")":
			raise ValueError("Unmatched closing bracket.")

		elif pattern[i] in bracket_pair:
			closing_bracket = find_closing_bracket(pattern, i)
			is_operator = check_for_operator(pattern, closing_bracket)
			groups.append(pattern[i: closing_bracket+1+is_operator])
			i = (closing_bracket+1+is_operator)
	
		elif pattern[i] == "\\":
			if i+1 == len(pattern):
				raise DanglingException
			is_operator = check_for_operator(pattern, i+1)
			groups.append(pattern[i: i+2+is_operator])
			i += (2 + is_operator)


		else:
			is_operator = check_for_operator(pattern, i)
			groups.append(pattern[i: i+1+is_operator])
			i += (1 + is_operator)

	return groups



def match_regex(pattern: str, text: str) -> int:
	groups = break_regex(pattern)
	return match_regex_groups(groups, text)



def find_pattern(pattern: str, text: str) -> t.List[str]:
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

























