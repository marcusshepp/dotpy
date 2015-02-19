# -- First assignment --
#last = raw_input('Enter your lastname: ')
#first = raw_input('Enter your firstname: ')
#print last, first

# -- Iterables --

# mylist is the iterable (reading the list one by one)
mylist = [x*x for x in range(3)]
for i in mylist:
		print "This is an iteration list ", i

for i in mylist:
		print "This is the second iteration list ", i


# -- Generators --

# notice () rather then [] -  *only in interators*
# generators don't stay in memory which is why the list won't print twice.
mylist = (x*x for x in range(3))
for i in mylist:
		print "This is a generator list ", i

for i in mylist:
		print 'This is the second generator list ', i #this won't print because the list wasn't saved in memory


# -- Yield --

def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i #keyword like 'return' that returns a generator
myGenerator = createGenerator() #Creat a generator
print 'myGenerator', myGenerator #myGenerator is an object -- prints out: myGenerator <generator object createGenerator at 0x10959b0a0> 
								#-- this is where the 'myGenerator' object is stored in memory

for i in myGenerator:
	print 'for loop', i #Output list: 0, 1, 4