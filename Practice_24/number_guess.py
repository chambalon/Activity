import random


number = random.randint(1,101)

print("Welcome to number guess game. Guess a number between 1 to 100")


guess=0
while True:

    num = input("Make a guess: ")
    guess+=1
    if num.isdigit():
        num= int(num)
    else:
        print("Enter an integer")
        continue

    if num == number:
        print("you have guessed it right in", guess,"guessess")
        break
    elif num < number:
        print("Too low")
        continue
    elif num > number:
        print("too high")
        continue






