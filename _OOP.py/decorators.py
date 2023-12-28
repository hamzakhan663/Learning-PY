def times_two_decorator(func):
    def times_two():
        value = func()
        return pow(value, 2)
    
    return times_two

@times_two_decorator
def my_function():
    return 6

print(my_function())