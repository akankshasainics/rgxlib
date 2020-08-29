import sys
brackets = { "(": ")", "[": "]"}

def find_end_bracket(i, pattern):
	count = 0
	try:
		while i < len(pattern):
			if pattern[i] == "(":
				count += 1
			if pattern[i] == ")":
				count -= 1
			if count == 0:
				return i
			i += 1
	except ValueError:
		print("invalid pattern.")


def expand_group(start, end):
	s = set()
	for c in range(start, end+1):
		s.add(chr(c))
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
				else:
					chars.add(pattern[i+1])
				i = i+2
			except ValueError:
				print("invalid pattern.")

		elif i+2 < len(pattern):
			if pattern[i:i+3] == "A-Z":
				chars.update(expand_group(ord("A"), ord("Z")+1))
				i += 3
			elif pattern[i:i+3] == "a-z":
				chars.update(expand_group(ord("a"), ord("z")+1))
				i += 3
			elif pattern[i:i+3] == "0-9":
				chars.update(expand_group(ord("0"), ord("9")+1))
				i += 3

		else:
			chars.add(pattern[i])
			i += 1

	return chars



def eval_square_bracket(pattern, text):
	result = []
	letters = simplify_square_bracket(pattern)
	for i, p in enumerate(pattern):
		if p in letters:
			result.append([i,i])
	return result


def match_pattern(pattern, text, i = 0, j = float("inf")):
	if pattern[i] in brackets:
		index = find_end_bracket(i, pattern)
		if pattern[i] == "[":
			result = eval_square_bracket(pattern, text, i+1, index-1)
		else:
			result = match_pattern(pattern, text, i+1, index-1)































if __name__ == "__main__":
	length_of_args = len(sys.argv)
	args_list = str(sys.argv)
	result = match_pattern(args_list[0], args_list[1])
	print(result)

