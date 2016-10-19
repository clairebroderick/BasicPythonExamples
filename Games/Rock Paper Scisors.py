#Paper Rock Scisors

name = input ("What is your name? \n")

print ("Welcome to paper, rock, scisors", name, " .")

#Set the Variables
playerscore = 0
computerscore = 0
Goes = 0

import random

while Goes<4:
     choice = input ("What is your choice Rock, Paper, Scisors \n r,p,s?\n")

     if choice == "r":
          print ("You choose Rock")
          Goes = Goes +1
                    

     elif choice == "p":
          print ("You choose Paper")
          Goes = Goes +1
                    

     elif choice == "s":
          print ("You choose Scisors")
          Goes = Goes +1
                    


     compChoice = random.randint(1,3)


     if compChoice == 1:
          cc = "r"
          print ("Computer choose Rock")

     elif compChoice ==2:
          cc= "p"
          print ("Computer choose Paper")

     elif compChoice == 3:
          cc = "s"
          print ("Computer choose Scisors")


#Who wins

#User Wins Options:
          
     if choice == cc:
          print ("Snap, you both chose the same!\n")

     elif choice  == "p" and cc == "r":
          print ("User Wins!\n")
          playerscore = playerscore + 1

     elif choice  == "r" and cc == "s":
          print ("User Wins!\n")
          playerscore = playerscore + 1

     elif choice  == "s" and cc == "p":
          print ("User Wins!\n")
          playerscore = playerscore + 1



#Computer Wins Options

     if cc  == "p" and choice == "r":
          print ("Computer Wins!\n")
          computerscore = computerscore + 1

     elif cc  == "r" and choice == "s":
          print ("Computer Wins!\n")
          computerscore = computerscore + 1

     elif cc  == "s" and choice == "p":
          print ("Computer Wins!\n")
          computerscore = computerscore + 1
     
print ("Your score is", playerscore)
print ("The computers score is", computerscore)



