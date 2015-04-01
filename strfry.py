def strfry(str1, str2):
	word1 = []
	word2 = []
	for i in str1:
		word1.append(i)
	for j in str2:
		word2.append(j)
	word1.sort()
	word2.sort()
	if word1 == word2:
		print "Possible"
	else:
		print "Impossible"

for i in range(int(input())):
	x = raw_input()
	lister = str(x).split()
	strfry(lister[0], lister[1])