from WelcomeFunction import welcome

def main():
    #call functions
    test_welcome_string()
    test_welcome_int()

def test_welcome_string():
    #testing to see if passing in the below string returns the right output
    assert welcome("Jalal") == "Welcome onboard, Jalal.\nIt's good to have you here.\nHave fun!"
    
def test_welcome_int():
    #trying to pass an int into the welcome function
    try:
        welcome(1)
    except ValueError as e:
        #comparing the string representation of the error to the string
        assert str(e) == "Person must be a string"
main()