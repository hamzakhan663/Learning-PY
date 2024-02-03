class Account:
    def __init__(self):
        #Initialize instance variable
        self._balance = 0
    
    #balance method can be accessed like an attribute
    @property   
    def balance(self):
        #return value of instance variable
        return self._balance
    
    #deposit method
    def deposit(self, amount):
        self._balance += amount
    
    #withdraw method    
    def withdraw(self, amount):
        self._balance -= amount
        

def main():
    #object of the class
    account = Account()
    #balance method accessed like an attribute
    print(f"Initial Balance: ${account.balance}")
    account.deposit(1000)
    account.withdraw(250)
    print(f"Final Balance: ${account.balance}")
    
if __name__ == "__main__":
    main() 