def insertionsort(l):
	value = l[len(l)-1]
	time = ""
	for i in l:
		if i > value:
			l[l.index(i)] = i
		else:
			l[l.index(i)] = value
		time+=str(l)+"\n"
	return time

print insertionsort([2, 4, 6, 8, 3])