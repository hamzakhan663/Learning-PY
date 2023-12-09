

# # # Polymorphism

# # class Animal:
    
# #     def __init__(self,name):
# #         self.name = name
        
# #     def speak(self):
# #         print("I do not know what to say")
        

# # class Dog(Animal):
    
# #     def speak(self):
# #         print("Dogs Bark - woof woof woof")

# # class Lion(Animal):
# #     def speak(self):
# #         print("Lions roar - roooooar")

# # Bingo = Dog("Boosky")

# # Lion_obj = Lion("simba")

# # Bingo.speak()
# # Lion_obj.speak()



# # ENCAPSULATION


# class Account:
    
#     def __init__(self,name):
#         self.name = name
#         self.__account_balance = 1800
    
#     @property
#     def acct_balance(self):
#         return self.__account_balance
    
#     @acct_balance.setter
#     def acct_balance(self,amount):
#         self.__account_balance = amount
    
#     @acct_balance.deleter
#     def acct_balance(self):
#         del self.__account_balance

        

# acct_1 = Account("Phil")


# print(acct_1.acct_balance)  # get the account balance

# acct_1.acct_balance = 4500

# print(acct_1.acct_balance)

# del acct_1.acct_balance

# print(acct_1.acct_balance())





class Person:
    
    def __init__(self,name):
        self.name = name
        self.__password = "sljgatrg;a8949ywrehw"
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,new_password):
        self.__password = new_password
        
    @password.deleter    
    def password(self):
        del self.__password
    

        
    

p1 = Person("Godswill")

# before encapsulation

print(p1.password) # shows password
p1.password = "jshdihriuigefs"  # change password
# del p1.password  # delete password


# AFTER ENCAPSULATION
# p1.show_password()  # show password
# p1.change_password("jshdihriuigefs") # change password
# p1.delete_password()  # delete password

   




