from def_check_operators import check_operators
from def_solve import solve

s = ['1', '(', '4', '+', '4', ')', '4']

def check_brackets(stack): #проверяет, верно ли расставлены скобки

    if type(stack) == int:
        return(stack)
            
    while ")" in stack:
        close_bracket_index = stack.index(")")
        for i in range(close_bracket_index):
            if stack[i] == "(":
                open_bracket_index = i

        substack = stack[open_bracket_index+1:close_bracket_index]

        if check_operators(substack) == 1 and len(solve(substack)) == 1:
            stack.pop(close_bracket_index)
            stack.pop(open_bracket_index)
        else:
            return 'Ошибка ввода операторов и операндов'
        
            
    return stack
print(check_brackets(s))
