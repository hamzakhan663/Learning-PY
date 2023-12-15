def main():
    #while condition is True..
    while True:
        x = input("Enter your name to continue: ")
        #isalpha checks if value is alphabetic so if x is not an alphabet..
        if not x.isalpha():
            print ("Please enter a string")
        #else print welcome message
        else:
            print(welcome(x))
            break

def welcome(person):
    #if what is passed into the person variable is an instance of/is an integer...
    if isinstance(person, int):
        #raise an error with the message..this is used to test an occurrence whereby person is an integer in the test file
        raise ValueError("Person must be a string")
    else:
        return f"Welcome onboard, {person}.\nIt's good to have you here.\nHave fun!"
   
   
       
if __name__ == "__main__":
    main()