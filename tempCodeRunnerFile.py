from SquareFunction import main  # Importing the main function from your module

def test_user_input():
    print("Testing number input:")
    user_input = "8"  # Simulate number input '8'
    result = main(user_input)  # Pass user input to the main function

    if result == "64":
        print("Number input test passed")
    else:
        print("Number input test failed")


if __name__ == '__main__':
    test_user_input()