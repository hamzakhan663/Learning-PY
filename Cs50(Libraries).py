#Modules
#Random Module
# import random #Use module in code
# from time import sleep #Use specific function from module
# sleep(1) #sleep function
# print ("I'm starving, Let's see who's getting us food today.")
# sleep(2)
# choice = random.choice(["Abdullah", "Jafar", "Sheriff", "Hamza"]) #choice function prints a random choice from the list
# print(f"{choice}, You're the one getting us food today.")

#use randint to generate random atm pin
# sleep(1)
# name = input("What's your name please?: ")
# sleep(2)
# print("Just a moment")
# sleep(2)
# atm_pin = random.randint(1001,9999)
# print(f"Here you go, {name}: {atm_pin}.")

#use shuffle
# cards = ["King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace"]
# random.shuffle(cards)
# for card in cards:
#     print (card)
    
#Statistics Module
import statistics
from time import sleep

#Main Function
def main():
    mean_function()
    median_function()
    modal_function()

print("When done entering values, press any key to exit.")
sleep(1)
#Mean Function
def mean_function():
    mean_list = []
    while True: #Loop until all numbers are entered
        try: 
            question = int(input("Enter a number for Mean: "))
            mean_list.append(question)
        except ValueError: 
            if input("Are you done entering numbers? Type 'Yes' to finish: ") == 'Yes':
             break
            else:
                print("Enter a number:")
    # check if numbers are in list 
    if len(mean_list) > 0:
        math_function = statistics.mean(mean_list)
        print(math_function)
    else:
        print("No numbers entered")
    sleep(2)
        
def median_function():
    median_list = []
    while True:
        try:
            median_values = int(input("Enter a number for Median: "))
            median_list.append(median_values)
        except ValueError:
            if input("Are you done entering numbers? Type 'Yes' to finish: ") == 'Yes':
             break
            else:
                print("Enter a number: ")
    
    if len(median_list) > 0:
        math_function2 = statistics.median(median_list)
        print(math_function2)
    sleep(2)

def modal_function():
    modal_values = []
    while True:
        try:
            modal_question = int(input("Enter a number for Mode: "))
            modal_values.append(modal_question)
        except ValueError:
            if input("Are you done entering numbers? Type 'Yes' to finish: ") == 'Yes':
             break
            else:
                print("Enter a number: ")
    
    if len(modal_values) > 0:
        math_function3 = statistics.mode(modal_values)
        print(math_function3)
main()

#a betterment of my code according to GPT
# import statistics

# def input_numbers(prompt):
#     number_list = []
#     while True:
#         try:
#             question = input(prompt + " (or type 'done' to finish): ")
#             if question.lower() == 'done':
#                 break
#             else:
#                 number = int(question)
#                 number_list.append(number)
#         except ValueError:
#             print("Enter a valid number or 'done' to finish.")

#     return number_list

# def main():
#     mean_list = input_numbers("Enter a number for Mean")
#     if len(mean_list) > 0:
#         mean_value = statistics.mean(mean_list)
#         print("Mean:", mean_value)
#     else:
#         print("No numbers entered for Mean")

#     median_list = input_numbers("Enter a number for Median")
#     if len(median_list) > 0:
#         median_value = statistics.median(median_list)
#         print("Median:", median_value)
#     else:
#         print("No numbers entered for Median")

#     modal_list = input_numbers("Enter a number for Mode")
#     if len(modal_list) > 0:
#         modal_value = statistics.mode(modal_list)
#         print("Mode:", modal_value)
#     else:
#         print("No numbers entered for Mode")

# # Call the main function to execute the program
# main()

    # math_function1 = statistics.median([90,20,30,40,50])
    # print(math_function1)

    # math_function2 = statistics.mode([30,30,30,40,50])
    # print(math_function2)