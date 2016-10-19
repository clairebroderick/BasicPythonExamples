import random

number = random.randint(1,10)

guesses = 5

while guesses > 0:

    guess = input ("What is your guess? : ")

    g = int(guess)
    guesses = guesses -1

    if g == number:
         print ("Well done, you got it")
    elif g > number:
        print ("Too High. Try Again")
    elif g < number:
        print ("Too Low try again")
    
    
