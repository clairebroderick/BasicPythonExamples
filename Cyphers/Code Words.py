#Create lists

letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
revletters = [" ", "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]

#Ask the user for the input
word = input ("Please enter the word you want to code: \n")

#Set the variables
n = 0
codeword = " "





for i in word:
     letter = word[n] #Finds the letter
     index = (letters.index(letter)) #finds the index of the letter
     codeword = codeword + (revletters[index]) #Finds the coded letter and adds it to codeword
     n = n+1
     


print (codeword)






