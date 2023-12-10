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

# #Meow Function
# def main():
#     meow(get_number()) 

# def get_number():
#     while True:
#          amount_of_times = int(input("Amount of times you want a sound to be shown: "))
#          if amount_of_times > 0:
#             return amount_of_times

# def meow(number):
#   for _ in range(number):
#     print ("meow")

# main()


# # #Lists
# students = ["Hamza", "Muzzamil", "Zayd"]
# # for student in students: #Print all values in the list 
# #     print (student)
    
# for i in range(len(students)): #figure out how many students are in the list, instead of hardcoding the number 3
#    print(students[i])
   

fairies = [] #empty list to collect input of fairies
valid_fairies = ["Bloom","Aisha","Musa","Terra","Flora","Stella"] #list holding valid names of fairies the program will run user input through to validate

for i in range(6): #ask for 6 input
    while True:
        name_of_fairies = input(f"Enter name of fairy {i + 1}: ") #ask user to input names, i+1 to make it look like "Enter name of fairy 1"
        if len(name_of_fairies) != 0 and name_of_fairies in valid_fairies : # Add names to the empty list if and only if the length of the list is not zero and the names of fairies inputed corresponds with the valid list containing fairy names
            fairies.append(name_of_fairies)
            break
        else:
            print("Invalid Fairy Name!") #If those conditions aren't met, print this

types_of_fairies = ["Fire Fairy", "Water Fairy", "Mind Fairy", "Earth Fairy", "Nature Fairy", "Light Fairy"] #List containing each type of fairy from the valid_fairies list

if len(fairies) >= 3:  # Check if there are at least 3 fairies
    
    fairy_index = 2
    if len(fairies) > fairy_index:
        fairy_name = fairies[fairy_index]
        if fairy_name in valid_fairies:
            index_in_valid_fairies = valid_fairies.index(fairy_name)
            fairy_type = types_of_fairies[index_in_valid_fairies]
            fairy_question= input(f" What type of fairy is {fairy_name}?: ")
            if fairy_question == fairy_type:
                print("Indisputably correct!")
            else: 
             print("FAIL!")
        else:
            print("Fairy not in list")
    else: 
        print("Amount of fairies must be at least 3")
        
              
else:
    print ("Enter up to three fairies")

#Dictionaries