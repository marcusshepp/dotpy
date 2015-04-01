quotes = []
for i in range(int(input())):
	quote = raw_input()
	quotes.append(quote)
numofquotes = int(raw_input())

for j in range(1, numofquotes):
	if int(raw_input()) >= numofquotes:
		print "Rule ", j, ":", " No such rule"
	else:
		print "Rule ", j, ":", quotes[j]