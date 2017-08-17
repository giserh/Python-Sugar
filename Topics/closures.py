def outer_func():
    message = 'Hi'

    def inner_func():
        # free variables
        print(message)

    return inner_func

my_func = outer_func()
my_func()
