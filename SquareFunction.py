def main():
    while True:
        try:
            user_input = (input("Enter a number: "))
        except ValueError:
            print("Not a number")
        else:
            print(squared(user_input))
            break
    

def squared(n):
    return pow(n, 2)

if __name__ == "__main__":
    main()