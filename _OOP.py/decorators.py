#define a decorator holding a parameter(func) which is a reference to the function.
def times_two_decorator(func):
    #nested function/modified function
    def times_two():
        #initialize a variable to the return value of the original function
        value = func()
        return pow(value, 2)
    
    #return modified function
    return times_two

#decorate the function hence modifying the original function
@times_two_decorator
def my_function():
    return 6

#print the modified function
print(my_function())