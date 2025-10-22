from def_check_operators import check_operators
from def_solve import solve

def check_brackets(stack: list[str]) -> list[str] | str:

    """Путем нахождения последнего символа ')' и предшествующего ему
    символа '(', выбирает скобки с высшим приоритетом.
    Проверяет, корректно ли выражение в скобках, применяя на него функцию solve().
    если выражение корректно, удаляет скобки из стека"""
    
            
    while ")" in stack:
        close_bracket_index = stack.index(")")
        for i in range(close_bracket_index):
            if stack[i] == "(":
                open_bracket_index = i

        substack = stack[open_bracket_index+1:close_bracket_index]

        if check_operators(substack):
            stack.pop(close_bracket_index)
            stack.pop(open_bracket_index)
        return 'Ошибка ввода операторов и операндов'
        
    return stack