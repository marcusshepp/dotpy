def odds_then_evens(a):
	new_list = []
	for key in a:
		if key%2 == 0:
			new_list.append(key)
			a.remove(key)
	return a+new_list

l = range(0, 10)
print l
print odds_then_evens(l)