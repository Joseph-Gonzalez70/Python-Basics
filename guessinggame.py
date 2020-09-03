import random

random_number = random.randint(1,10)

keep_playing=None

while True:
	guess= int(input("Pick a number from 1 to 10:"))
	if guess>random_number:
		print("Too high!")
	elif guess < random_number:
		print("Too low!")
	else:
		print("You got it!")
		keep_playing = input("Would you like to keep playing?(y/n) ")
		if keep_playing == "y":
			random_number = random.randint(1,10)
			guess=None
		else:
			print("Thank you for playing")
			break

			
