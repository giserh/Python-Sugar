#########################
#                       #
# First-class functions #
#                       #
#########################
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    return [func(i) for i in arg_list]

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)
# [1, 8, 27, 64, 125]

#################
#               #
# First example #
#               #
#################
def logger(msg):
    '''
    Returns a function load_message, that uses the
    '''
    def log_message():
        print('Log:', msg)

    return log_message

log_hi = logger('Hi!')
log_hi()
# Log: Hi!

##################
#                #
# Second example #
#                #
##################
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_hi = html_tag('h1')
print_hi('Test Headline!')
# <h1>Test Headline!</h1>

print_hi('Another Headline!')
# <h1>Another Headline!</h1>

print_hi = html_tag('p')
print_hi('Test paragraph!')
# <p>Test paragraph!</p>
