# Guessing Game

import random

number = random.randint(1,10)

guess = 0

while guess != number:
    guess = input("Whats your guess? ")
    g = int(guess)
    if g < number:
            print ("Too low!")
    elif g > number:
        print ("Too high.")
    elif g == number:
        print ("Well done!")
            
            
