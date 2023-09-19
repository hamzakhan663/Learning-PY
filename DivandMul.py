def find_numbers():
    numbers = []
    for i in range(1500,2701):
        if i%5 == 0 and i%7 == 0:
            numbers.append(i)
    return numbers

div_mul = find_numbers()
print (div_mul)
