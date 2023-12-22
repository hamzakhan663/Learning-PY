#import modules.
import csv
import os

#initialize file paths.
file_path = "Cs50(FileHandling).py/alumni.csv"
temporary_file = "Cs50(FileHandling).py/temporary_file.csv"

#initialize words to find and replace.
old_word = "Sulaimon"
new_word = "Suleyman"

#open file in read mode.
with open(file_path, "r") as file:
    #reader object reads the file.
    reader = csv.reader(file)
    #turns the rows gotten from the reader to a list.
    rows = list(reader)
    
    #initialize an empty list that will hold the modified rows.
    modified_rows = []
    #for each row in rows(nested list).
    for row in rows:
        #each cell in each row is stripped of trailing whitespaces then if the old word is found, the new word replaces it. list comprehension is used.
        modified_row = [cell.strip().replace(old_word, new_word) for cell in row]
        #append each modified row to the modified list.
        modified_rows.append(modified_row)

#open the temporary file in write mode.   
with open(temporary_file, "w", newline='') as file2:
    #writer object to write to the file.
    writer = csv.writer(file2)
    #for each modified row in the list, write the modified row to the file with writer. This can also be done by removing the loop and passing the list itself to the writerows() method.
    for modified_row in modified_rows:
        writer.writerow(modified_row)
        
#replace the content in second argument with the content of the first argument.
os.replace(temporary_file, file_path)