# guessRandomNumber.py
Guess the random number generator

import random

def guess(x):
  random_num = random.randint(1,x)
  guess = 0
  while guess != random_num:
    guess = int(imput(f"Guess a number between 1 and {x}: "))
    if guess < random_num:
      print("Sorry too low")
    elif guess > random_num:
      print("Too high, pick another number")
  print("Great Job, you choose correctly")
