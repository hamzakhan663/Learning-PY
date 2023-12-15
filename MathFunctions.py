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