from typing import Callable
from token_class import token

"""
This file contains all the nodes used in the AST all nodes are derived from the node class
"""
class node:
    """Basic Node
    """
    def __str__(self) -> str:
        return "basic node, type: {}".format(type(self))
    def __repr__(self) -> str:
        return self.__str__()

#operator node used to store lhs,rhs and the opperator
class op_node(node):
    """Operator Node,

    This Node has a lhs, rhs and operator
    """
    def __init__(self,lhs : node, op : Callable, rhs : node):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    def __str__(self) -> str:
        return "{{lhs: {}, op: {}, rhs: {}}}".format(self.lhs,self.op.__name__,self.rhs)
    def __repr__(self) -> str:
        return self.__str__()

#number node used to store a integer value
class number_node(node):
    """Number Node,

    This Node has a token as name and a value
    """
    def __init__(self, token : token):
        self.__token = token
        self.value = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.value)
    def __repr__(self) -> str:
        return self.__str__()

#name node(used to store variable names)
class name_node(node):
    """Name Node,

    This Node has a name token and a name value
    """
    def __init__(self, token : token):
        self.__token = token
        self.name = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.name)
    def __repr__(self) -> str:
        return self.__str__()

#if(if) node used to signal the start of a condition
class if_node(node):
    """If Node,

    Used to signal the start of a condition. 

    Has a condition, operator and an end_location
    """
    def __init__(self,conditie : node, op : Callable, eind_locatie : int):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self) -> str:
        return "{{if: conditie: {} : end_if: {}}}".format(self.conditie, self.eind_locatie)
    def __repr__(self) -> str:
        return self.__str__()

#einde if node used to signal the end of a condition
class end_if_node(node):
    """End If Node,

    Used to signal the end of an if block. 
    """
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "{end_if_node}"
    def __repr__(self) -> str:
        return self.__str__()

#while(while) node used to signal the start of a loop
class while_node(node):
    def __init__(self, conditie : node, op : Callable, eind_locatie : int):
        self.conditie = conditie
        self.op = op
        self.eind_locatie = eind_locatie
    def __str__(self) -> str:
        return "{{while: conditie: {} : einde while: {}}}".format(self.conditie, self.eind_locatie)
    def __repr__(self) -> str:
        return self.__str__()

#einde while node used to signal the end of a loop
class end_while(node):
    def __init__(self, hoeveelheid_regels_terug : int):
        self.hoeveelheid_regels_terug = hoeveelheid_regels_terug
    def __str__(self) -> str:
        return "{{end_while: hoeveelheid_regels_terug = {}}}".format(self.hoeveelheid_regels_terug)
    def __repr__(self) -> str:
        return self.__str__()

#print node used for printing variables and or expressions
class print_node(node):
    def __init__(self,to_print : node,op : Callable):
        self.to_print = to_print
        self.op = op
    def __str__(self):
        return "{{print: {}}}".format(self.to_print)
    def __repr__(Self):
        return self.__str__()

# node used to store "const char *" like string
class str_node(node):
    def __init__(self, token : token):
        self.__token = token
        self.value = token.value
    def __str__(self) -> str:
        return "{}:{}".format(self.__token.token_type.name, self.value)
    def __repr__(self) -> str:
        return self.__str__()

#tuple to store all single sided nodes this makes it easy to check if the node is single sided
single_sided_nodes = (print_node,while_node,if_node)