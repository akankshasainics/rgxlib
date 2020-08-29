import sys
from typing import Pattern
bracket_pair = { "(": ")", "[": "]"}
small_alphabet = "abcdefghjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
groups = {"A-Z": set(capital_alphabet), "a-z": set(small_alphabet), "0-9": set(digits)}
special_char = {"\d": set(digits), "\w": set(alpha_numeric)}

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
	i = 0
	chars = set()
	while i < len(pattern):
		if i+2 < len(pattern) and pattern[i:i+3] in groups:
			chars.update(groups[pattern[i:i+3]])
			i = i+3

		else:
			chars.add(pattern[i])
			i += 1
	# print(chars)
	return chars



# def match_square_bracket_pattern(pattern, text):
# 	if len(pattern) == 0:
# 		return []
# 	result = []
# 	letters = simplify_square_bracket(pattern)
# 	if pattern[0] != '^':
# 		for i, p in enumerate(text):
# 			if p in letters:
# 				result.append([i,i])
# 	else:
# 		for i,p in enumerate(text):
# 			if p not in letters:
# 				result.append([i,i])
# 	return result

# "[A-Z]f", "Bfc" [[0,1],[5,6]]
# def match_pattern(pattern, text, i = 0, j = float("inf")):
# 	if pattern[i] in bracket_pair:
# 		index = find_closing_bracket(pattern, i)

# 		if pattern[i] == "[":
# 			result = match_square_bracket_pattern(pattern, text, i+1, index-1)
# 		else:
# 			result = match_pattern(pattern, text, i+1, index-1)


# def match_and_return_end(pattern: str, text: str)->Optional[int]:
#     pointer = 0
#     i = 0
#     while i < len(pattern):
#         if char not in brackets:
#             if char != text[pointer]:
#                 return None
#             i+=1
#         else:
#             ending_brack = find_closing_bracket(pattern, i)
#             char_set = set_from_brack(pattern[i+1:ending_brack])
#             if text[pointer] not in char_set:
#                 return None
#             i = ending_brack+1
#         pointer += 1
#     return pointer


# def find_pattern(pattern: str, text, non_overlapping = False):
#     matches = []
#     while i < len(text):
#         match_idx = match_pattern(pattern, text[i])
#         if match_idx != -1:
#             matches.append([i, match_idx+i])
#         if non_overlapping:
#             i = match_idx +i
#         i += 1
#     return matches




def find_pattern(pattern: str, text: str) -> int:
	i = 0
	j = 0
	while i < len(pattern) and j < len(text):
		if pattern[i] in bracket_pair:
			ending_brack = find_closing_bracket(pattern, i)
			if pattern[i] == '[':
				chars = simplify_square_bracket(pattern[i+1: ending_brack])
				i = ending_brack + 1
				if text[j] in chars:
					j += 1
				else:
					break
		elif pattern[i] == text[j]:
			i += 1
			j += 1
		else:
			break

	# print(i, len(pattern))
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

