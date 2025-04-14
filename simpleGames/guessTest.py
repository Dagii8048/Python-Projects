import random

rand = random.randint(1,10)
def guess(rand):
	userInput = int(input("Please Enter a number between 1 - 10 : "))
	while True:
		if(userInput > rand):
			print("Your guess is too high...")
		elif(userInput < rand):
			print("Your guess is too low...")
		else:
			print("Yep...You guessed it right!")
			break
		userInput = int(input("Not correct, try again : "))
guess(rand)
