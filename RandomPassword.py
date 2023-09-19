import random
import time

# Generate a random 4-digit PIN as a string
pin = str(random.randint(0, 9999)).zfill(4) 
print("Your password is:", pin)

while True:
    lucky_guess = input("Please enter your 4-digit guess: ")

    feedback = ''
    
    if lucky_guess == pin:
        print("Access granted.")
        break
    else:
        if len(lucky_guess) != 4 or not lucky_guess.isdigit():
            print("Invalid input. Please enter a four digit guess.")
            continue
        
        for i in range(4):
            if lucky_guess[i] == pin[i]:
                feedback += lucky_guess[i]
            else:
                feedback += '*'
        print("Incorrect password. Feedback:", feedback)
