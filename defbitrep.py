def bitrep(n):
	""" Returns the signed 32-bit binary representation of an integer. """
	
	arr = []
	j=0
	while j<32:
		x=n%2
		if x>0:
			arr.append(1)
		else:
			arr.append(0)
		n/=2
		j+=1
	# using extended slice syntax. thanks SOF	
	return arr[::-1] # [start:stop:step] so step is -1

print bitrep(13)