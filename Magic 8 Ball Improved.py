# Magic 8 Ball V2

import random
import time
import winsound

number = random.randint(1,3)

print ("Welcome to the magic 8 Ball! \n Think of a question")
time.sleep(1.5)

print()


for i in range(0,10):
    print ("Shaking........")
    time.sleep(0.5)

print("_______")
print ("Your answer is: ")

if number == 1:
    print ("Go for it!")

elif number == 2:
    print ("Dont do it!")

elif number == 3:
    print ("Think about this some more")

input ("Press any key to exit!")


