def main(user_input):
    while True:
        try:
            number = int(user_input)
        except ValueError:
            print("Not a number")
        else:
            print(squared(number))
            break
    

def squared(n):
    return n*n

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    main(user_input)