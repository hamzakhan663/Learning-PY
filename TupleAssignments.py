#  allows a tuple of variable names on the left of an assignment statement to be assigned values from a tuple on the right of the assignment. "Unpacking the values into the variable names"

(a,b,c,d) = (10,20,30,40)
print(a)

julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia
print(f"{name} {surname} is an {profession} born in {birth_place} in {birth_year}. She got a role in {movie} in {movie_year}.")

[a,b,c,d,e] = [2,4,6,8,10]
print (pow(e,2))


characters = [("Lim", "Ju-kyung"), ("Lee", "Su-ho"), ("Han", "Seo-jun"), ("Kang", "Soo-jin")]
for surname,first_name in characters:
    print (f"Starring {surname} {first_name}.")

# enumerate
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for index,value in enumerate(fruits):
    print(f"{index}.{value}")

#Runestone question - The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list of keys from the dictionary track_medal_counts and assign the list to the variable name track_events. Do NOT use the .keys() method.

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events=[]
for key,value in track_medal_counts.items():
    track_events.append(key)

print(track_events)