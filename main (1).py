import random


number = random.randint(1, 10)

print("I have generated a number between 1 and 10.")
guess = int(input("Guess the number: "))


if guess == number:
    print("🎉 Correct! You guessed the number.")
else:
    print("❌ Wrong guess.")
    print("The correct number was:", number)
