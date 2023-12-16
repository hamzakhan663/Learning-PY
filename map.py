def cubed(x):
    cube = pow(x, 3)
    return cube

def congrats(person):
    return f"You got the job! {person}"
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
persons = ["Hamza", "Jafar", "Nuriyah", "Abdullah"]

result = map(congrats, persons)
print (list(result))
