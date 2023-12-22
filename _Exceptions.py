#Test your code here
try:
    x = input("What's your name?: ")
    #If input contains non alphabets, then..
    if x.isalpha():
       print (f"Welcome, {x}.") 
    #Custom error message to trigger an exception
    else:
        raise ValueError("Invalid input, Integers are not allowed as input.")
#If try block condition is not met, catch the error and handle it
except ValueError as e:
    print (e)

#Keeps asking for the age until it is greater than or equal to 18, Illogical but needed to grasp loops with the exception
def get_info():
    while True: #To loop repeatedly until we pass the condition
        try:
            age = int(input("You want to drink a beer right? What's your age?: "))
        
            if age >= 18:
                print (f"Okay, Go ahead, {x}.")
                break
        
            else:
                raise Exception("Could you BE any more younger?")
                
        except Exception as e:
            print (e)
            
