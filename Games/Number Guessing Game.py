#Number Guessing Game


name = input ("What is your name? \n")

print ("Welcome to the number guessing game", name, ".")

#Set the Variables
playerscore = 0
computerscore = 0
Goes = 0

import random
import time

while Goes<11:
     
     userChoice = input ("Pick a number from 1 to 10:\n")
     choice = int(userChoice)

     compChoice = random.randint(1,10)

     print ("You choose", choice)
     print ("Computer chose", compChoice)

     time.sleep(1)

     

     if choice > compChoice:
          print ("You win!")
          playerscore = playerscore + 1
          print ("Your score:", playerscore, "   ", "Computer Score:", computerscore, "\n")
          time.sleep(1)
          
     elif choice < compChoice:
          print ("YOu loose!")
          computerscore = computerscore + 1
          print ("Your score:", playerscore, "   ", "Computer Score:", computerscore, "\n")
          time.sleep(1)
          
     else:
          print ("Its a draw!")
          print ("Your score:", playerscore, "   ", "Computer Score:", computerscore, "\n")
