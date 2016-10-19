#Cypher Task

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

code = input ("Please enter the word you want to code: \n")

codeword = " "

n = 0

for i in code:
     #Get the letter n index from list
     fi = (letters.index(code[n]))
     n = n+1

     #Add two to the inedx
     ni = int(fi)+2

     #Get the value of the new index

     codeword = codeword + letters[ni]

     print (codeword)



