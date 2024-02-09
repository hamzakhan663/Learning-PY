def main():
    print(add(10,10,30,200))
    print(subtract(-5, 5))
    
def add(*args):
    addition = 0
    for num in args:
        addition += num
    return addition

def subtract(var1,var2):
    subtraction = var1-var2
    return subtraction


if __name__ == "__main__":   
    main()