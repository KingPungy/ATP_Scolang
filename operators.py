from copy import copy
from program_state import program_state
from typing import Union

#basic mathematical operators for floats and ints
def op_plus(a : Union[int,float,str],b : Union[int,float,str]) -> Union[int,float,str]:
    """
    Plus/ADD operator funtion, 
    
    supports [int,float,str]
    """
    if type(a) == str:
        b = str(b)
    elif type(b) == str:
        a = str(a)

    return a + b

def op_min(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    """
    Minus/MIN operator funtion,
    
    supports [int,float]
    """
    return a - b

def op_power(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    """
    Power/POW operator funtion, 
    
    supports [int,float]
    """
    return a ** b

def op_mul(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    """
    Multiply/MUL operator funtion, 
    
    supports [int,float]
    """
    return a * b

def op_divide(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    """
    Divide/DIV operator funtion, 
    
    supports [int,float] returns floats
    """
    return a / b

def op_modulus(a : Union[int,float],b : Union[int,float]) -> Union[int,float]:
    """
    Modulus operator funtion, 
    
    supports [int,float] returns int if possible
    """
    return a % b

#rational operators
def op_equal(a : Union[int,float,str],b :Union[int,float,str]) -> int:
    """
    Equal "==" operator funtion, 
    
    supports [int,float,str] returns int(0 or 1)
    """
    return int(a == b)

def op_greater_than(a : Union[int,float,str],b : Union[int,float,str]) -> int:
    """
    Greater Than ">" operator funtion, supports [int,float,str]  to return int(0 or 1)

    When type(str) uses length of str
    """
    if type(a) == str:
        a = len(a)
    if type(b) == str:
        b = len(b)
    return int(a > b)

def op_smaller_than(a : Union[int,float,str],b : Union[int,float,str]) -> int:
    """
    Smaller Than "<" operator funtion, supports [int,float,str] to return int(0 or 1)

    When type(str) uses length of str 
    """
    if type(a) == str:
        a = len(a)
    if type(b) == str:
        b = len(b)
    return int(a < b)

def op_greater_equal(a : Union[int,float,str],b : Union[int,float,str]) -> int:
    """
    Greater or equal to ">=" operator funtion, supports [int,float,str] to return int(0 or 1)

    When type(str) uses length of str 
    """
    if type(a) == str:
        a = len(a)
    if type(b) == str:
        b = len(b)
    return int(a >= b)

def op_smaller_equal(a : Union[int,float,str],b : Union[int,float,str]) -> int:
    """
    Smaller or equal to "<=" operator funtion, supports [int,float,str] to return int(0 or 1)

    When type(str) uses length of str 
    """
    if type(a) == str:
        a = len(a)
    if type(b) == str:
        b = len(b)
    return int(a <= b)

def op_not_equal(a : Union[int,float,str],b : Union[int,float,str]) -> int:
    """
    Greater or equal to ">=" operator funtion, supports [int,float,str] to return int(0 or 1)

    When only one is of type(str) results in failure unless using ascii characters
    """
    return int(a != b)

#operators to modify program state and check ifs
def op_if(conditie : Union[int,float], aantal_regels : int) -> int:
    """
    operator to check if condition and return 1(go to next row) or the amount of rows to skip
    """
    if conditie:
        return 1
    return aantal_regels

def op_assign(name : str, value : Union[int,float], program_state : program_state) -> program_state:
    """
    operator to assign a value to a certain variable. and return a new program state(with row number increased by one)
    """
    output = copy(program_state)
    to_add = {name:value}
    output.variables.update(to_add)
    output.row_number +=1
    return output

def update_row_number(aantal_regels : int, program_state : program_state) -> program_state:
    """
    operator to increase row number based on aantal_regels
    """
    output = copy(program_state)
    output.row_number += aantal_regels
    return output

def op_print(to_print : Union[int,float], program_state : program_state) -> program_state:
    """
    operator to print the to_print part" and increase row number by one
    """
    output = copy(program_state)
    output.row_number +=1
    print(to_print)
    return output


# To determine the order of operations
op_precedence1 = (op_power,)
op_precedence2 = (op_mul,op_divide,op_modulus)
op_precedence3 = (op_min,op_plus)
op_precedence4 = (op_assign,op_equal,op_greater_than,op_smaller_than,\
                  op_greater_equal, op_smaller_equal, op_not_equal)
all_op = op_precedence1 + op_precedence2 + op_precedence3 + op_precedence4