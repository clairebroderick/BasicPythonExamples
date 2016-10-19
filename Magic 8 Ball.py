# Magic 8 Ball

import random

number = random.randint(1,3)

print ("Welcome to the magic 8 Ball! \n Think of a question")

print ("Shaking........\n" *10)

if number == 1:
    print ("Go for it!")

elif number == 2:
    print ("Dont do it!")

elif number == 3:
    print ("Think about this some more")

input ("Press any key to exit!")
