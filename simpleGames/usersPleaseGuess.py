import random

def guess(x):
	random_number = random.randint(1,x)
	attempts = 0
	while True:
		try:
			guess = int(input(f"Guess a number between 1 and {x}: "))
			attempts += 1
			if guess < random_number:
				print("Sorry, guess again. Too low.")
			elif guess > random_number:
				print("Sorry, guess again. Too high.")
			else:
				print(f"Yay, congrats. You have guessed the number {random_number} correctly in {attempts} attempts!")
				break
		except ValueError:
			print("Sorry, invalid input. Please enter an integer.")
user_input = int(input("Up to what number should I set the range for you : "))
guess(user_input)