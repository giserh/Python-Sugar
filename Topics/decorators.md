# Decorators
Decorators allow you to make simple modifications to callable objects like functions, methods, or classes. We shall deal with functions for this tutorial. The syntax:

```python
@decorator
def functions(arg):
    return "Return"
```
is equivalent to:
```python
def function(arg):
    return "Return"
function = decorator(function)
```

As you may have seen, a decorator is just another function which takes a functions and returns one. For example you could do this:
```python
def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)
    return new_function

@repeater
def Multiply(num1, num2):
    print(num1*num2)

Multiply(2, 3)
>>> 6
>>> 6
```

Another example:
```python
def Multiply(multiplier):
    def Multiply_Generator(old_function):
        def new_function(*args, **kwds):
            return multiplier*old_function(*args, **kwds)
        return new_function
    return Multiply_Generator

@Multiply(3)
def Num(num):
    return num

print(Num(3))
>>> 9
```
