# #EVEN/ODD? FUNCTION
# def main():
#     x = int(input("Enter a number: "))
#     if is_even(x):
#         print("As Even as the river flows!")
#     else:
#         print("As Odd as snow in spring!")

# def is_even(number):
#     # even_or_odd = number % 2 == 0
#     # return even_or_odd
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#     #return number % 2 == 0
# main()

friends_name = input("Enter Friends Character: ")

match friends_name:
    case "Chandler" | "Chandler Bing":
        print("Sarcastic, Funny, Caring")
    case "Monica" | "Monica Geller":
        print("High Maintenance, Loving, Quirky")
    case "Joey" | "Joey Tribianni":
        print("Foodie, Dashing, Ladies Magnet")
    case "Ross" | "Ross Geller":
            print("Insecure, Nice, Thoughtful") 
    case "Rachel" | "Rachel Green":
        print("Selfish, Independent, Beautiful")
    case "Phoebe" | "Phoebe Buffay":
        print("Not Funny, Anti Mondler, Singer")
    case _:
        print("Uhm, Who?")