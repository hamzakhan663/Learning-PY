# import time 
# name = input("Enter your name in the format (Surname, First Name, Middle Name): ").title().strip()
# last, first, middle = name.split(" ")
# time.sleep(2)
# course = "CS50's Introduction to Programming with Python."
# print (f"Hello, {first} {middle}. Welcome to {course}")

# x = int(input ("What's x? "))
# y = int(input ("What's y? "))

# z = x/y
# print(f"{z:.2f}")

# #Main method
# def main():
#     name = input("Enter your name: ").title()
#     hello(name)
    
# #Function
# def hello(person):
#     print (f"Hello, {person}")

# #Call main method
# main()

#Function without main method
def square(number):
    return pow(number, 2) #or return number ** 2 or return number * number
x  = int(input("What's x? "))
print ("The square of x is", square(x))
