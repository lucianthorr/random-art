import random
from math import sin, cos, tan, pi
from math import log, log10, acos
from statistics import mean

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.
FORMULA = ""

def __str__():
    pass

def random_sin(n):
    # if random.random() < 0.5:
    #     return sin(pi * n) * random.random()
    # else:
    return sin(pi * n)

def random_cos(n):
    # if random.random() < 0.5:
    #     return cos(pi * n) * random.random()
    # else:
    return cos(pi * n)

def random_mod_pi(n):
    # if random.random() < 0.5:
    #     return (n % pi) * random.random()
    # else:
    return (n % pi)

def random_log(n):
    return log(abs(n)) if n != 0 else (random.random()+1)


def random_axis(x,y):
    axis_choice = random.randint(1,4)
    if axis_choice == 1:
        return x
    elif axis_choice == 2:
        return y
    elif axis_choice == 3:
        return x + y
    else:
        return x*y

def random_function(axis):
    function_choice = random.randint(1,6)
    if function_choice == 1:
        return random_sin(axis)
    elif function_choice == 2:
        return random_cos(axis)
    elif function_choice == 3:
        return random_log(axis)
    else:
        return random_mod_pi(axis)

def random_formula(x,y):
    formula_choice = random.randint(1,4)
    if formula_choice == 1:
        return random_function(x) + random_function(y)
    elif formula_choice == 2:
        return random_function(x) - random_function(y)
    elif formula_choice == 3:
        return random_function(x) * random_function(y)
    else:
        return random_function(x * y)

def add_to_expression(expr):
    random_function = random.randint(4,7)
    if random_function == 0:
        new_expr = lambda x, y: (expr(x,y) * random_sin(random_axis(x,y)))
    elif random_function == 1:
        new_expr = lambda x, y: (expr(x,y) * random_cos(random_axis(x,y)))
    elif random_function == 2:
        new_expr = lambda x, y: (expr(x,y) * random_mod_pi(random_axis(x,y)))
    elif random_function == 3:
        new_expr = lambda x, y: (expr(x,y) * random_log(random_axis(x,y)))
    elif random_function == 4:
        new_expr = lambda x,y: random_sin(expr(x,y))
    elif random_function == 5:
        new_expr = lambda x,y: random_cos(expr(x,y))
    elif random_function == 6:
        new_expr = lambda x,y: random_mod_pi(expr(x,y))
    elif random_function == 7:
        new_expr = lambda x,y: random_log(expr(x,y))
    else:
        new_expr = lambda x, y: (expr(x,y) + expr(y,x))
    return new_expr

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    nests = random.randint(2,10)
    expr = lambda x,y: random_formula(x,y)
    for _ in range(nests):
        expr = add_to_expression(expr)
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x,y)


#dictionary = {"sin":lambda x, y: sin(x)}
