import random
randnum = random.randint(1,10)
print randnum
userguess = int(raw_input("Guess a number between 1 and 10 "))
while randnum != userguess:
	if randnum > userguess:
		print "too low!"
		userguess = int(raw_input("Guess a number between 1 and 10 "))
	if randnum < userguess:
		print "too high!"
		userguess = int(raw_input("Guess a number between 1 and 10 "))
print "you win!"