def meal_name(*args, **kwargs):
    restaurant_meal_name = args[0]
    restaurant_menu_price = kwargs["customer_price"]
    restaurant_menu_category = kwargs["customer_category"]
    restaurant_menu = {
        restaurant_meal_name: {
            'price': restaurant_menu_price,
            'category': restaurant_menu_category
        }
    }
    return restaurant_menu

# Function for inputting your orders
def customer_input_model():
    print("Welcome to Our Kitchen")
    loop_unit = int(input("How many set of meals?: "))
    all_customers_list = {}
    for i in range(loop_unit):
        customers_meal_name = input("Please input your meal name: ")
        customer_price = float(input("Please input your meal price: "))
        customer_category = input("Please input your meal category: ")
        customers_list = {
            "customer_price": customer_price,
            "customer_category": customer_category,
        }
        all_customers_list.update(meal_name(customers_meal_name, **customers_list))
    return all_customers_list

# Call the function
print(customer_input_model())