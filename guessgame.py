import random 

guessTaken = 0

print("hello, what's your name?")

myName = raw_input()

number = random.randint(1, 20)
print("well"+ myName + ", I am thinkin of a number between 1 and 20.")


while guessTaken < 6:
	print("take a guess.")
	guess = raw_input()
	guess = int(guess)

	guessTaken += 1

	if guess < number:
		print("Your guess is too low.")

	if guess > number:
		print("Your guess is too high")

	if guess == number:
		break
if guess == number:
	guessTaken = str(guessTaken)
	print("good job" + myName + ", you guessed my number in" + guessTaken + 'guesses' )

if guess != number:
	number = str(number)
	print("Nope. The number I was thinking of was" + number)

	
