#Cypher Task

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

code = input ("Please enter the word you want to code")

n=1
newcode = (" ")

#fi = first index
#ni = new index(fi +2)
#si = second index

for i in code:
      fi = (letters.index(code[n]))
      n=n+1

      ni = int(fi)+2

      newcode= newcode +(letters[ni])
     
