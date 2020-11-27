from token_class import token
from token_types import token_types, token_operator_strings, token_operator_types
from operators import *
import re
from typing import List, Callable
import shlex

def get_and_split_input(fname : str)->List[List[str]]:
    """
    function to read in the given file and split it by line and whitespace
    also remove extranius whitespaces
    """
    infile = open(fname,'r')
    str_lst = infile.read().splitlines()
    # split all words and strings, remove comments 
    # and if a line becomes empty because of comments remove it with filter
    return list(filter(None,list(map(split_without_substr,list(map(str.strip,str_lst))))))

def split_without_substr(in_str : str) -> List[str]:
    """
    function to remove comments and to split a line on spaces except when within ""
    note: only works if one "" pair is used per rule
    """
    # removing comments
    in_str = re.sub(r"\#.*\#", "", in_str)
    # if there is a " in the line look for both and split everything around it normaly 
    # but leave the spacing as is between the quotes
    if "\"" in in_str:
        quote_index = in_str.find("\"")
        quote_end_index = in_str.rfind("\"")+1
        return in_str[:quote_index].split() + [in_str[quote_index:quote_end_index]] + in_str[quote_end_index:].split()
    return in_str.split()

def get_token(input_str : str) -> token: 
    """
    get token based on string by comparing it to all token types 
    if no token type is found name token is constructed because if the string is no keyword it must be a variable name
    """
    if input_str in token_operator_strings:
        index = token_operator_strings.index(input_str)
        return token(token_operator_types[index], token_operator_types[index].value)
    elif input_str in token_types.IF_STATEMENT.__name__:
        return token(token_types.IF_STATEMENT,op_if)
    elif input_str == token_types.END_IF.__name__:
        return token(token_types.END_IF,"endif")
    elif input_str == token_types.WHILE_START.__name__:
        return token(token_types.WHILE_START,op_if)
    elif input_str == token_types.WHILE_END.__name__:
        return token(token_types.WHILE_END,"endwhile")
    elif input_str == token_types.PRINT.__name__:
        return token(token_types.PRINT,op_print)
    elif all(map(str.isdigit,input_str)) or (input_str[0] == '-' and all(map(str.isdigit,input_str[1:]))): #positive or negative
        return token(token_types.NUMBER, int(input_str))
    elif (all(map(str.isdigit,input_str.replace('.','',1))) 
        or (input_str[0] == '-' and all(map(str.isdigit,input_str.replace('.','',1)[1:])))): #floats positive and negative 
        return token(token_types.NUMBER,float(input_str))
    elif input_str[0] == "\"" and input_str[-1] == "\"":
        return token(token_types.STR,input_str.strip("\""))
    else:
        return token(token_types.NAME,input_str)

def lex(fname : str) -> List[List[token]]:
    """
    function to get the tokens for each line of the input file
    """
    return list(map(lambda row: list(map(get_token,row)),get_and_split_input(fname)))

def verbose_lex(f : Callable):
    """
    decorator to function lex for printing a bit more information
    """
    def inner(file_name : str):
        print("start lexing of program located in {}".format(file_name))
        print("lexer output")
        tokens = f(file_name)
        
        print("Regels: ",*tokens,sep="\nRegel: ")

        # for row in range(len(tokens)):
        #     print("regel:",row+1)
        #     for token in tokens[row]:
        #         print(token)
        # print("\n")
        return tokens
    return inner