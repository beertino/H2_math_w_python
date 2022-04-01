# Modules for algebraic manipulation and pretty printing
from sympy import *
from IPython.display import Math,display

def get_inverse(expr:str):
    '''Print out the possible rules for the inverse of a function
    '''
    x, y = symbols('x y')

    f_inverse = solve((y-parse_expr(expr)),x)

    #Note that there are 2 solutions in f_inverse and we need to reject the 
    #appropriate one
    try:    
        for i in range(2):
            display(Math(f'x={ latex(f_inverse[i])}'))
    except:
        pass
