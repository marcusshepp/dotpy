def common_substring(s1, s2):
	"""
	You are given two strings, A and B. 
	Find if there is a substring that appears in both A and B.
	"""

	x, y = list(s1), list(s2)
	flag = ""
	for _ in x:
		if _ in y:
			flag = "yes"
		else:
			flag = "no"
	return flag

for _ in range(input()):
	x = input()
	y = input()
	print common_substring(x, y)