import random
randnum = random.randint(0,10)

userguess = raw_input("Guess a number between 1 and 10 ")
while randnum != userguess:
	if randnum > userguess:
		print "too low!"
		userguess = raw_input("Guess a number between 1 and 10 ")
	if randnum < userguess:
		print "too high!"
		userguess = raw_input("Guess a number between 1 and 10 ")
print "you win!"