# Text Based Game

import time

print ("Welcome to the maze")
time.sleep (1)

print ("You are stuck in an old castle and need to excape")
time.sleep (1)

print ("You are stuck in a large room, you cant remember how you got here. In front of you there is a door do you want to open it? Press Y to open it. Press N to leae it closed: \n")
time.sleep (1)

choice1 = input ("Enter Y or N to continue: \n")

if choice1 == "Y":
    print ("You open the door, there is a dark corridor which you walk along, feeling your way along the walls")

elif choice1 == "N":
    print ("You stay in the room. Suddenly there is a loud bang and a blinding flash. That is all you remember")
    sys.exit(3)
    
print ("You come to a junction. Do you go left, straight, or right?")
time.sleep(1)

choice2 = input ("Enter L, S, R: \n")

if choice2 == "L":
    print ("Unfortunately after taking 2 steps you fell down a hole and that is all you remember. The end!")

elif choice2 == "S":
    print ("You keep walkng along the corridor. You come accross a shaft of light, there is a strange whoshing sound. Do you walk towards the light, or do you keep going straight down the corridor?")

elif choice2 == "R":
    print ("You walk for about 100 meters, suddenly you feel the floor crumbling from under you. That is the last thing you remember!")

else:
    print ("You have pressed an invalid key, you die!")
