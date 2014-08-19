def permutations(string):
	if len(string) == 1:
		return [string]
	else:
		b = []
		for index, char in enumerate(string):
			b += [char + x for x in permutations(string[0:index] + string[index + 1: len(string)])]
		return b

print permutations("abc")