# create a function that checks if a number is prime

def checkprime(n): #n is the number that will be raw user input

	# make sure n is a positive integer
	n = abs(int(n))
	# 0 and 1 are not prime numbers
	if n < 2:
		return False
	# 2 is the only even prime number
	if n == 2:
		return True
	# all other even numbers are not prime
	# I need to understand this line
	if not n & 1:
		return False

	for x in range(3, int(n**0.5) + 1, 2):
		if n % x == 0:
			return False

	return True

# output
userinput = float(input("Check if your number is prime: "))

# if the number is prime print a positive statement
if checkprime(userinput): 
	print checkprime(userinput), ", this is a prime number"

# if the number is not prime print a negative statement
else:
	print "No, this is not a prime number"