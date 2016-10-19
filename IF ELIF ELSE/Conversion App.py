# Conversion App

print ("Welcome to the Conversion App")
print ("1) Miles to Kilometers\n2) Kilometers to Miles \n3) Meters to cm \n4) Cm to Meters")

conversion = input ("Please select your conversion type: \n")

num = input ("What number would you like to convert: \n")

n = int(num)
conv = int(conversion)

if conv == 1:
    print (n * 1.6)

elif conv == 2:
    print (n / 1.6)

elif conv == 3:
    print (n*10)

elif conver == 4:
    print (n/10)
    

