# Convertor

print ("Welcome to the convertor")



number = input ("Please enter the number you would like to convert: \n")

n = int(number)

print ("What conversion would you like to cary out?")

print ("1) Convert from miles to km \n2) Convert from km to miles \n3)Convert from foot to m \n4) convert from m to feet")

conversion = input ("Enter your selection: \n")
conv = int(conversion)

if conv == 1:
    print (n * 1.609)

elif conv ==2:
     print (n * 0.62137)

elif conv ==3:
     print (n * 0.3048)
    
