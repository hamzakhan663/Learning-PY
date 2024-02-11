students = [
    {"name":"Hamza", "house":"Hufflepuff"},
    {"name":"Muhammad", "house":"Gryffindor"},
    {"name":"Abdulwahab", "house":"Ravenclaw"},
    {"name":"Zayd", "house":"Gryffindor"},
    {"name":"Abdullah", "house":"Hufflepuff"},
    {"name":"Jamal", "house":"Ravenclaw"},
    {"name": "Fareedah O", "house": "Slytherin"},
    {"name": "Fareedah A", "house": "Gryffindor"},
    {"name": "Aaishah", "house": "Hufflepuff"},
    {"name": "Nuriyah", "house": "Gryffindor"},
    
    
    
]

#filter with list comprehension
ravenclaws = [
    #for each dictionary in the list, if the key is equal to the value, add the name value to the new list.
    student['name'] for student in students if student['house'] == "Ravenclaw"
    ]

for raven in ravenclaws:
    print (raven,"🐦‍⬛")

#filter with filter function
def is_gryffindor(student):
    #return true or false
    return student['house'] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print (gryffindor['name'])
       