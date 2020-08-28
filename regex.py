import sys
brackets = { "(": ")", "[": "]"}
small_alphabet = "abcdefgjijklmnopqrstuvwxyz"
capital_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
alpha_numeric = small_alphabet + capital_alphabet + digits + '_'
groups = {"A-Z": capital_alphabet, "a-z": small_alphabet, "0-9": digits}


def find_end_bracket(pattern):
	count = 0
	i = 0
	brack = pattern[i]
	while i < len(pattern):
		if pattern[i] == brack:
			count += 1
		if pattern[i] == brackets[brack]:
			count -= 1
		if count == 0:
			return i
		i += 1
	if count != -1:
		raise ValueError("invalid pattern")


def expand_group(pattern):
	s = set()
	for c in groups[pattern]:
		s.add(c)
	return s

def simplify_square_bracket(pattern):
	i = 0
	chars = set()
	while i < len(pattern):
		if pattern[i] == "/":
			try:
				if pattern[i+1] == "d":
					for num in range(0,10):
						chars.add(num)
				elif pattern[i+1] == "w":
					chars.update(set(alpha_numeric))
				else:
					chars.add(pattern[i+1])
				i = i+2
			except ValueError:
				print("invalid pattern.")

		elif i+2 < len(pattern) and pattern[i:i+3] in groups:
			chars.update(expand_group(pattern[i:i+3]))
			i = i+3

		else:
			chars.add(pattern[i])
			i += 1

	return chars



def match_square_bracket_pattern(pattern, text):
	if len(pattern) == 0:
		return []
	result = []
	letters = simplify_square_bracket(pattern)
	if pattern[0] != '^':
		for i, p in enumerate(text):
			if p in letters:
				result.append([i,i])
	else:
		for i,p in enumerate(text):
			if p not in letters:
				result.append([i,i])
	return result


def match_pattern(pattern, text, i = 0, j = float("inf")):
	if pattern[i] in brackets:
		index = i + find_end_bracket(pattern[i:])
		if pattern[i] == "[":
			result = match_square_bracket_pattern(pattern, text, i+1, index-1)
		else:
			result = match_pattern(pattern, text, i+1, index-1)


	



	







































if __name__ == "__main__":
	length_of_args = len(sys.argv)
	args_list = str(sys.argv)
	result = match_pattern(args_list[0], args_list[1])
	print(result)

