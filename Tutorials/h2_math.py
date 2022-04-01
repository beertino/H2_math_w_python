# Modules for algebraic manipulation and pretty printing
from xmlrpc.client import Boolean
from sympy import *
from IPython.display import Math,display

def print_inverse(f:Function):
    '''Print out the possible rules for the inverse of a function
    '''
    x, y = symbols('x y')

    f_inverse = solve((y-f(x)),x)

    #Note that there are possibly 2 solutions in f_inverse and we need to reject the 
    #appropriate one
    try:    
        for i in range(2):
            display(Math(f'x={ latex(f_inverse[i])}'))
    except:
        pass


def self_compose(f:Function,num_comp = 1,simp:bool=True):
    x = symbols('x')
    composite_function = x

    for n in range(num_comp):
        #Note that we simplify here because otherwise, the expression just gets
        #into a bigger and bigger nest
        if simp:
            composite_function = simplify(f(composite_function))
        else:
            composite_function = f(composite_function)

    return composite_function


