#take variable number of arguments  
def promotion(*names):
    #returns a tuple of names
    return (names)

#take a single name as parameter
def status(name):
    #returns a string
    return f"{name} was promoted to the next Dojo."

#apply status function to each element in the tuple returned by promotion
results = map(status, promotion("Daniel-san", "Ken-san", "Naomi-san", "Erika-san", "Kaizen-san"))
#convert the map object to a list 
print(list(results))
