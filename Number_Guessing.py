import random 
from time import sleep
print("Welcome to Number Guessing Game!")
sleep(1)
level=input("Choose a difficulty. Type 'easy' or 'hard' or 'expert': ")
if level == 'easy':
    life = 10
    sleep(1)
    print(f"You have {life} attempts. Let's begin!")
elif level == 'hard':
    life = 5
    sleep(1)
    print(f"You have {life} attempts. Let's begin!")
elif level == 'expert':
    life = 2
    sleep(1)
    print(f"You have {life} attempts. Let's begin!")
else:
        SystemExit()
        
while True:
    # numbers = []
    # for number in range(1,101):
    #     numbers.append(number)   
    sleep(1)
    user_guess = int(input("Guess a number between 0 and 100: "))

    chosen_number = random.randrange(1,101)
    # print (chosen_number)
    if user_guess < chosen_number:
        print ("Too low")
        
    elif user_guess > chosen_number:
        print ("Too high")

    else:
        print("Correct!")
    
    life = life - 1
    sleep(1)
    print(f'You have {life} attempts left.')
    if life == 0:
        sleep(1)
        print("Game over.")
        break
     

    