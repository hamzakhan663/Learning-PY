#Code to accept names of the 6 Winx Saga Fairies and ask user for their fairy type.

fairies = [] #empty list to collect input of fairies
valid_fairies = ["Bloom","Aisha","Musa","Terra","Flora","Stella"] #list holding valid names of fairies the program will run user input through to validate

for i in range(6): #ask for 6 inputs
    while True:
        name_of_fairies = input(f"Enter name of fairy {i + 1}: ") #ask user to input names, i+1 to make it look like "Enter name of fairy 1"
        if len(name_of_fairies) != 0 and name_of_fairies in valid_fairies : # Add names to the empty list if and only if the length of the list is not zero and the names of fairies inputted corresponds with the valid list containing fairy names
            fairies.append(name_of_fairies) #Add input to empty list
            break #leave loop and continue
        else:
            print("Invalid Fairy Name!") #If those conditions aren't met, print this

types_of_fairies = ["Fire Fairy", "Water Fairy", "Mind Fairy", "Earth Fairy", "Nature Fairy", "Light Fairy"] #List containing each type of fairy from the valid_fairies list

if len(fairies) > 2:  # Check if there are at least 3 fairies
    
    fairy_index = 2 #Index of the fairy in the list the question will be based on
    
    if len(fairies) > fairy_index: #check if the inputs in the fairies list is more than the fairy index, i.e it checks if there are more than 3 fairies in the list so it has enough input to continue
        fairy_name = fairies[fairy_index] #variable fairy name is equal to the value of the fairy index. The name of the fairy in fairy index is stored in this variable
        if fairy_name in valid_fairies: #checks if the name of the fairy is one of the valid names in the list
            index_in_valid_fairies = valid_fairies.index(fairy_name) #variable stores the index of the fairy name in the list of valid fairy names
            fairy_type = types_of_fairies[index_in_valid_fairies] #variable uses the index gotten from the list of valid fairies and equates it to the same index in the type of fairies list
            fairy_question= input(f" What type of fairy is {fairy_name}?: ") #ask the type of fairy based on the fairy name
            if fairy_question == fairy_type: #if the input is correct, print..
                print("Indisputably correct!")
            else: #else print...
             print("FAIL!")
        else: #if fairy is not in list..
            print("Fairy not in list")
    else: #if the amount of fairies in the list is less than the fairy index...i.e if the amount of input given to the program is less than the fairy index, it cannot continue
        print(f"Amount of fairies must be at least {fairy_index + 1}")
        
              
else: #if there aren't three fairies in the list at least...
    print ("Enter up to three fairies")
