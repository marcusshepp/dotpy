"""
You are given an integer N. Find the digits in this number that exactly divide N 
(division that leaves 0 as remainder) and display their count. 
For N=24, there are 2 digits (2 & 4). Both of these digits exactly divide 24. 
So our answer is 2.

Note

If the same number is repeated twice at different positions, 
it should be counted twice, e.g., For N=122, 2 divides 122 exactly and occurs at ones' 
and tens' position. So for this case, our answer is 3.
Division by 0 is undefined.
"""

def is_duplicate_num(n):
	""" Returns True if an integer has dublicate values. """
	
	count = 0
	x = [x for x in str(n)]
	for i in range(len(x)):
		if x.count(x[i]) > 1:
			count += 1
	if count > 1:
		return True
	else:
		return False	

def find_digits(n):

	count, i = 0, 0
	if is_duplicate_num(n):
		count += 1
	while i <= n:
		if i % n == 0:
			count += 1 
		i += 1
	return count



for i in range(int(raw_input())):
	print find_digits(int(raw_input()))