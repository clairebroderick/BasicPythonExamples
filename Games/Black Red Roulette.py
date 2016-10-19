# Roulette

name = input ("What is your name? \n")

print ("Welcome to the colour guessing game", name, ".")

#Set the Variables
playerscore = 0
computerscore = 0
Goes = 0

import random
import time

while Goes<6:
     userChoice = input ("Pick a colour black (B) or Red (R):\n")
     Goes = Goes +1

     ComputerChoice = random.randint(1,2)
     if ComputerChoice == 1:
          print ("Computer choose Red")
          ComputerChoice = "R"

     elif ComputerChoice == 2:
          print ("Computer choose Black")
          ComputerChoice = "B"

     if userChoice == "B" and ComputerChoice == "B":
          print("You win!\n")
          playerscore = playerscore +1

     elif userChoice == "R" and ComputerChoice == "R":
          print("You win!\n")
          playerscore = playerscore +1

     elif userChoice == "R" and ComputerChoice == "B":
          print ("You loose!\n")
          computerscore = computerscore + 1

     elif userChoice == "B" and ComputerChoice == "R":
          print ("You loose!\n")
          computerscore = computerscore + 1

print ("Your score is: ", playerscore, " The computer scored: ", computerscore)
gameend = print ("Game Over")



     
