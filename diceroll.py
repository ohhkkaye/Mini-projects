import random

def diceroll():
	print "Here is your first roll!"
	print random.randint(1, 6)
	print "Would you like to roll again?"
	answer = raw_input("yes or no? ")
	while answer == 'yes':
		print "Here's another roll!"
		print random.randint(1, 6)
		print "Would you like to roll again?"
		answer = raw_input("yes or no? ")
	else:
		print "Thanks for playing!"
			

diceroll()