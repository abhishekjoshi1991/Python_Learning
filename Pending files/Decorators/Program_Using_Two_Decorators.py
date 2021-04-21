# Let's create two decorator, one will split the string and other will convert string to uppercase

# Function for converting to uppercase

def upper_d(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

# function to split the string
def split_d(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def ordinary():
    return 'good morning'

print(ordinary())

'''
if we call upper_d before split_d then will throw error that list has no upper function
so here upper_d is executed first, then outer decorator is executed
'''