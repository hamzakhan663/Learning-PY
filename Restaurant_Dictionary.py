import time

#Restaurant Menu
Food = {
    "food": {
        "White Rice": 200,
        "Fried Rice": 300,
        "French Fries": 400
    },

    "protein": {
        "KFC Chicken": 2500,
        "Tofu": 1000,
        "Fried Eggs": 200
    },

    "drinks": {
        "Chapman": 1500,
        "Teem": 200,
        "Water": 150,
    }
}
# Customer Order Details
customer_order = {}

print("Welcome to Khan Restaurant")

name = input("Enter name: ")
time.sleep(1)
print("Alright, Mr " + name)
time.sleep(1)
print("Would you like to see our food list? (yes/no)")
answer = input("")
protein_answer = ""  # Define protein_answer here
drink_answer = ""   # Define DRINK_answer here
order_summary = ""   # Define order summary here

if answer == "yes":
    print("Alright, give us a second")
    time.sleep(1)
    y = 1
    print("Here's our food list:")
    
    ## Main Food Order
    for meal in Food["food"]:
        print(y, "-", meal)
        y += 1

    choice = int(input("Choose your main meal (1, 2, or 3): "))

    if 1 <= choice <= 3:
        selected_meal = list(Food["food"].keys())[choice - 1]
        customer_order[selected_meal] = Food["food"][selected_meal]
        print("You've chosen", selected_meal)
    else:
        print("Invalid choice")

    ## Protein Order
    time.sleep(1)
    print("Would you like a side of protein with that? (yes/no)")
    protein_answer = input("")

if protein_answer == "yes":
    print("Alright, give us a second")
    time.sleep(1)
    z = 1
    print("Here's our protein list:")

    for side in Food["protein"]:
        print(z, "-", side)
        z += 1

    protein_choice = int(input("Choose your protein (1, 2, or 3): "))

    if 1 <= protein_choice <= 3:
        selected_side = list(Food["protein"].keys())[protein_choice - 1]
        customer_order[selected_side] = Food["protein"][selected_side]
        print("You've chosen", selected_side + " as your protein")
        
        ## Drink Order
        time.sleep(1)
        print("You now have", selected_meal + " and" , selected_side + " as your combo")
        time.sleep(1)
        print("Would you like to have a drink with that? (yes/no)")
        drink_answer = input("")

if drink_answer == "yes":
    print("Alright, give us a second")
    time.sleep(1)
    a = 1
    print("Here's our list of available drinks:")

    for drink in Food["drinks"]:
        print(a, "-", drink)
        a += 1
        
    drink_choice = int(input("Choose your drink (1, 2, or 3): "))

    if 1 <= drink_choice <= 3:
        selected_drink = list(Food["drinks"].keys())[drink_choice - 1]
        customer_order[selected_drink] = Food["drinks"][selected_drink]
        print("You've chosen", selected_drink)
        time.sleep(1)
        print("You now have", selected_meal + ",", selected_side + " and", selected_drink + " as your full order")
        time.sleep(1)
        print("Would that be all Mr", name + "? (yes/no)")
        order_summary = input("")

if order_summary == "yes":
    print("Alright, thank you for patronizing The Khan Restaurant!")
else:
    print("Invalid choice")
