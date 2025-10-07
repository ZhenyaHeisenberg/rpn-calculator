from def_check_operators import check_operators

def check_brackets(stack): #проверяет, верно ли расставлены скобки

    if type(stack) == int:
        return(stack)
            
    while ")" in stack:
        close_bracket_index = stack.index(")")
        for i in range(close_bracket_index):
            if stack[i] == "(":
                open_bracket_index = i

        substack = stack[open_bracket_index+1:close_bracket_index]

        if check_operators(substack) == 0:
            return 'Ошибка ввода операторов и операндов'
        else:
            stack.pop(close_bracket_index)
            stack.pop(open_bracket_index)
    return stack
