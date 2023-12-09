def addition(*args):
    num = 0
    for x in args:
        num = num + x
    return num
print (addition(2,4,5,6))

def subtraction(*args) :
    num = args[0]
    sum = 0
    for x in args[1:]:
        sum = sum + x
        result = num - sum
    return result
print (subtraction(155,10,8,9))

def mul(*args):
    mult = 1
    for x in args:
        mult = mult * x
    return mult
print (mul(2,4,5,6))


    