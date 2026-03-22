import random
import time

from word import a

name = input("please enter your name :")
print(f"welcome {name},"
      f"time to play Hangman")
time.sleep(1)

print("start guessing....")
time.sleep(0.5)

guesses = "" #starts empty
turns = 10 #stores variable
b = random.choice(a) #randomly selected value from a
print(b)
while True:
    guess = input("guess a character: ")
    guesses += guess #each guess is added into empty list
    if guess not in b:
        turns -= 1
        print("wrong")
        print(f"you have {turns} more guess")

    if turns == 0:
        print("you lose")
        break #program ends

    fail = 0 #variable is initialized as zero
    for i in b:
        if i in guesses: #for amount of guesses
            print(i, end=" ")
        else:
            print("_", end="  ")
            fail += 1
    if fail == 0:
        print("you win")
        break
