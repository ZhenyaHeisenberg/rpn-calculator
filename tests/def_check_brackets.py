from def_check_operators import check_operators
from def_solve import solve

def check_brackets(stack: list[str]) -> list[str] | str:
            
    while ")" in stack:
        close_bracket_index = stack.index(")")
        for i in range(close_bracket_index):
            if stack[i] == "(":
                open_bracket_index = i

        substack = stack[open_bracket_index+1:close_bracket_index]

        if check_operators(substack) == False:
            return 'Ошибка ввода операторов и операндов'
        else:
            stack.pop(close_bracket_index)
            stack.pop(open_bracket_index)
    return stack