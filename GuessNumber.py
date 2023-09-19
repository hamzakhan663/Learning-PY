import random

number = random.randint(1, 9)
print(number)

while True:
    int_guess = int(input("Enter your guess: "))

    if int_guess != number:
        if int_guess > number:
            print("Guess is higher than the number.")
        elif int_guess < number:
            print("Guess is lower than the number.")
    elif int_guess == number:
        print("Well guessed!")
        break
