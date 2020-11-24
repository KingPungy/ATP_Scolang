from enum import Enum
from operators import *
class token_types(Enum):
    OPERATOR_PLUS       = op_plus, "plus"
    
    OPERATOR_MIN        = op_min, "min"

    OPERATOR_POWER      = op_power, "power"

    OPERATOR_DIVIDE     = op_divide, "divide"

    OPERATOR_MULTIPLY  = op_mul, "times"

    OPERATOR_MODULUS    = op_modulus, "modulo"

    OPERATOR_ASSIGN     = op_assign, "is"

    OPERATOR_EQUAL_TO   = op_equal, "equal_to"
    OPERATOR_SMALLER_THAN   = op_smaller_than, "smaller_than"
    OPERATOR_GREATER_THAN   = op_greater_than, "greater_than"
    OPERATOR_GREATER_EQUAL  = op_greater_equal, "greater_equal"
    OPERATOR_SMALLER_EQUAL  = op_smaller_equal, "smaller_equal"
    OPERATOR_NOT_EQUAL      = op_not_equal, "not_equal"

    IF_STATEMENT    = 11, "if"
    END_IF          = 12, "endif"

    WHILE_START     = 13, "while"
    WHILE_END       = 14, "endwhile"

    PRINT           = 15, "show"

    NAME            = 16, "NAME"
    STR             = 17, "STR"
    NUMBER          = 18, "NUMBER"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.__name__ = name
        return member

    def __str__(self) -> str:
        return "token_type: {}, value: {}, str: {}".format(self.name,self.value,self.__name__)
    
    def __repr__(self) -> str:
        return self.__str__()

#tuple with strings used to check if input string is operator
token_operator_strings = tuple(filter(None, list(map(lambda t: t.__name__ if t.value in all_op else None, token_types))))
#tuple with all operator token types
token_operator_types   = tuple(filter(None, list(map(lambda t: t if t.value in all_op else None, token_types))))