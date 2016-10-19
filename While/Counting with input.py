# Counting up from one number to another number in 2s

print ("Welcome! I am going to count up fronm a number you specify to another number in 2's")


FirstNo = input ("Please enter the number you would like to start at: \n")
LastNo = input ("Please enter the nubber you would like to stop at: \n")

FN = int(FirstNo)
LN = int(LastNo)

while FN <=LN:
    print (FN)
    FN = FN+2
    

