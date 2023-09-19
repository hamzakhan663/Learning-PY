import time
x = int(input ("Please enter a number: "))
time.sleep(1)
y = int(input ("Please enter another number: "))
time.sleep(1)
add = x + y
rem = add%2
if rem == 0:
    print ("Number is even")
else:
    print ("Number is odd")