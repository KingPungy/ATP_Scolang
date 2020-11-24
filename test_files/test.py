from typing import List, Callable
import re

def get_and_split_input(fname : str)->List[List[str]]:
    """
    function to read in the given file and split it by line and whitespace
    also remove extranius whitespaces
    """
    infile = open(fname,'r')
    str_lst = infile.read().splitlines()
    str_lst = list(filter(None,list(map(split_without_substr,list(map(str.strip,str_lst))))))
    return str_lst



def split_without_substr(in_str : str) -> List[str]:
    """
    function to split line on spaces except when within ""
    note: only works if one "" pair is used per rule
    """
    in_str = re.sub(r"\#.*", "", in_str)
    if "\"" in in_str:
        quote_index = in_str.find("\"")
        in_str.replace('.','',1)
        return in_str[:quote_index].split() + [in_str[quote_index:]]
    return in_str.split()



print(get_and_split_input("voorbeelden\if.txt"))

# infile = open("voorbeelden\if.txt",'r')
# str_lst = infile.read().splitlines()
# str_lst = list(filter(None,str_lst))


# print(str_lst[5].find("\""))
# print(str_lst[5].rfind("\""))
# print(str_lst[5].count("\"",))

# in_str = str_lst[5]
# quote_index = in_str.find("\"")
# quote_end_index = in_str.rfind("\"")+1
# print(in_str[:quote_index].split() + [in_str[quote_index:quote_end_index]] + in_str[quote_end_index:].split())
# #print( re.findall(r"\"", str_lst[5]) ) 