balance = 0 

def main():
    deposit(1000)
    withdraw(50)
    print(f"Balance:${balance}")
    
def deposit(fund):
    global balance
    balance += fund
    
def withdraw(fund):
    global balance
    balance -= fund
    
    
if __name__ == "__main__":
    main()