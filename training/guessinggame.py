# Guessing game
# creating var for the entry and the answer
n = 0
actualnum = 50

# make sure that the program loops if the wrong answer is entered
while n != actualnum:

# reassign n to the input value
	n = int(raw_input("Guess a number: "))
	
# if the input is greater than the answer it will tell you
	if n > actualnum:
		print "Too high! "

# if the input is less than the answer it will tell you
	elif n < actualnum:
		print "Too low! "

# if the input is equal to the answer it will tell you
	else:
		print "There we go!"

# keep track of how many times the user guesses
total = 0

while n != actualnum:

	total += n
	
	if total == 3:
		print "that took you three tries"

	elif total == 2: 
		print "that took two tries"

	elif total == 1: 
		print "that only took one try"