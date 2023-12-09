# i = 0
# while i != 3:
#     print ("meow")
#     i = i + 1

# i = 0
# while i < 3:
#     print ("woof")
#     #Incrementing i
#     i +=1 # i = i + 1

# #For loops
# for i in range(10): 
#     print ("meow")
    
#While True = GOing forever by default, continue keyword continues until condition True is met. Break keyword if condition is met.

# while True:
#     n = int(input("Enter amount of times you want the cat to make a sound: "))
#     if n > 0:
#         break

# for i in range(n):
#     print ("meow")

# while True:
#     friends = input("Enter one of the six friends: ")
#     if friends not in ["Chandler", "Rachel", "Phoebe", "Ross", "Joey", "Monica"]:
#         continue
#     else:   
#         break

# match friends:
#     case "Chandler" | "Monica" | "Phoebe":
#         print ("Married")
    
#     case "Ross" | "Rachel":
#         print ("In a relationship")
    
#     case "Joey":
#         print ("Single")

#Meow Function
def main():
    meow(get_number()) 

def get_number():
    while True:
         amount_of_times = int(input("Amount of times you want a sound to be shown: "))
         if amount_of_times > 0:
            return amount_of_times

def meow(number):
  for _ in range(number):
    print ("meow")

main()