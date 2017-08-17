print("Using decorators.")
def repeater(old_function):
    def new_function(*args, **kwds): #See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) #we run the old function
        old_function(*args, **kwds) #we do it twice
    return new_function #we have to return the new_function, or it wouldn't reassign it to the value

@repeater
def Multiply(num1, num2):
    print(num1 * num2)

Multiply(2, 3)

print("Equivalent as above statement without decorators.")

def Multiply(num1, num2):
    print(num1*num2)

function = repeater(Multiply) #this passes the function to the decorator, and reassigns it to the functions
function(4, 2)

def Multiply(multiplier):
    def Multiply_Generator(old_function):
        def new_function(*args, **kwds):
            return multiplier*old_function(*args, **kwds)
        return new_function
    return Multiply_Generator #it returns the new generator


@Multiply(3) #Multiply is not a generator, but Multiply(3) is
def Num(num):
    return num

print(Num(3))
