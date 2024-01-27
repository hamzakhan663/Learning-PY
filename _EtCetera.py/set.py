students = [
    {"name":"Hamza", "house":"Hufflepuff"},
    {"name":"Muhammad", "house":"Gryffindor"},
    {"name":"Abdulwahab", "house":"Ravenclaw"},
    {"name":"Zayd", "house":"Gryffindor"},
    {"name":"Abdullah", "house":"Hufflepuff"},
    {"name":"Jamal", "house":"Ravenclaw"},
    
]

# houses = []
# for student in students:
#     if student['house'] not in houses:
#         houses.append(student['house'])

# for house in sorted(houses):
#     print (house)

#using set constructor
houses = set()
for student in students:
    houses.add(student['house'])

for house in sorted(houses):
    print (house)
