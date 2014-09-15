weight = float(input("How many pounds does your suitcase weigh? "))

if weight > 50:
	print("There is a charge for luggage that heavy.")

print("Thank you for your buisness.")

# -- absolute vales --
n = input("Number? ")
if n < 0:
	print "The absolute value of ", n, "is", -n
else:
	print 'That number is already positive'