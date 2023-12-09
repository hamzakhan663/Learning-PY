#EVEN/ODD? FUNCTION
def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("As Even as the river flows!")
    else:
        print("As Odd as snow in spring!")

def is_even(number):
    # even_or_odd = number % 2 == 0
    # return even_or_odd
    if number % 2 == 0:
        return True
    else:
        return False
    #return number % 2 == 0
main()
    