import random
from math import sin, cos, tan, pi
from math import log, log10, acos
from statistics import mean

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.
FORMULA = ""

def random_sin(n):
    return sin(pi * n)

def random_cos(n):
    return cos(pi * n)

def random_mod_pi(n):
    return (n % pi)/10

def average(x,y):
    return mean([x,y])

def random_log(n):
    """ returns log of n or a random number, if n == 0 """
    return log(abs(n)) if n != 0 else (random.random()+1)

def random_axis(x,y):
    """ Returns an axis or a combination of axes. """
    axis_choice = random.randint(0,100)
    if axis_choice <= 40:
        return x
    elif axis_choice <= 80:
        return y
    elif axis_choice <= 90:
        return x + y
    else:
        return x*y

def random_operator(axis):
    """ Random Operators takes the axis and applies a randomly generated
    operator to it.  """
    function_choice = random.randint(1,20)
    if function_choice <=15:
        return random_sin(axis)
    elif function_choice <= 30:
        return random_cos(axis)
    elif function_choice <= 45:
        return random_log(axis)
    else:
        return random_mod_pi(axis)

def random_function(x,y):
    """ Creates a random base function from a variety of operators and how
    they are combined. """
    formula_choice = random.randint(0,100)
    if formula_choice <= 35:
        return random_operator(x)
    elif formula_choice <= 70:
        return random_operator(y)
    elif formula_choice <= 85:
        return average(random_operator(x),random_operator(y))
    else:
        return random_operator(x)*random_operator(y)

def add_to_expression(expr):
    """ Randomly generates larger expressions from the given expression. """

    random_operator = random.randint(0,100)
    if random_operator <= 15:
        new_expr = lambda x, y: (expr(x,y) * random_sin(random_axis(x,y)))
    elif random_operator <= 30:
        new_expr = lambda x, y: (expr(x,y) * random_cos(random_axis(x,y)))
    elif random_operator <= 35:
        new_expr = lambda x, y: (expr(x,y) * random_mod_pi(random_axis(x,y)))
    elif random_operator <= 40:
        new_expr = lambda x, y: (expr(x,y) * random_log(random_axis(x,y)))
    elif random_operator <= 60:
        new_expr = lambda x,y: random_sin(expr(x,y))
    elif random_operator <= 80:
        new_expr = lambda x,y: random_cos(expr(x,y))
    elif random_operator <= 85:
        new_expr = lambda x,y: random_mod_pi(expr(x,y))
    elif random_operator <= 90:
        new_expr = lambda x,y: random_log(expr(x,y))
    else:
        new_expr = lambda x, y: (expr(x,y) + expr(y,x)/2)
    return new_expr


def create_expression():
    """Creates a simple expression and then builds upon it a random amount
    of times using add_to_expression. """
    nests = random.randint(2,10)
    expr = lambda x,y: random_function(x,y)
    for _ in range(nests):
        expr = add_to_expression(expr)
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    #print(expr(x,y))
    return expr(x,y)


#dictionary = {"sin":lambda x, y: sin(x)}
