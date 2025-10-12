from constants import OPERATORS
        
    
def parse(ex: str) -> list[str] | str:

    """Функция приводит строку к правильному виду
    и создает из нее стек"""

    brackets_count = 0
    for i in range(len(ex)):
        if ex[i] == "(":
            brackets_count += 1
        elif ex[i] == ")":
            brackets_count -= 1
        if brackets_count < 0:
            return 'Ошибка: есть неоткрытые скобки\n\n\n'
    if brackets_count != 0:
        return 'Ошибка: есть незакрытые скобки\n\n\n'

    ex = ex.replace("//", "&")
    ex = ex.replace("(", " ( ")
    ex = ex.replace(")", " ) ")
    ex = ex.replace(",", ".")
        
    

    stack = ex.split() # (1)
    
    return stack


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

        if check_operators(substack) == False:
            return 'Ошибка ввода операторов и операндов'
        else:
            stack.pop(close_bracket_index)
            stack.pop(open_bracket_index)
    return stack

def check_operators(substack: list[str]) -> bool:
    
    """В соответствии описанной в README формуле проверяет
    правильность введенного выражения"""
    
    
    return len(substack) == (2 * (substack.count("+") + substack.count("-") + substack.count("*") + substack.count("/") + substack.count("%") + substack.count("&") + substack.count("^")) + substack.count("~") + 1)


def solve(checked_stack: list[str]) -> list[str] | str:

    """Находит первое вхождение оператора в стеке, после чего применяет его
    на предыдущий/предыдущийе операнд/операнды, записывает результат в стек,
    а отработавшие символы из стека удаляет"""

    if check_operators(checked_stack) == False:
        return 'Ошибка ввода операторов и операндов'

    s = checked_stack

    while len(s) > 1:
        for i in range(len(s)):

            if s[i] == "~":
                if i > 0:
                    s[i-1] = str(float(s[i-1]) * (-1))
                    s.pop(i)
                    break
                else:
                    return "Ошибка ввода операторов и операндов"

            if s[i] in OPERATORS:
                if i < 2:
                    return "Ошибка ввода операторов и операндов"
                
                match s[i]:
                    case "+":
                        result = float(s[i-2]) + float(s[i-1])
                    case "-":
                        result = float(s[i-2]) - float(s[i-1])
                    case "*":
                        result = float(s[i-2]) * float(s[i-1])
                    case "/":
                        if float(s[i-1]) == 0:
                            return 'Ошибка: деление на 0 невозможно\n\n\n'
                        result = float(s[i-2]) / float(s[i-1])
                    case "%":
                        if float(s[i-1]) == 0:
                            return 'Ошибка: деление на 0 невозможно\n\n\n'
                        elif float(s[i-1])%1 != 0 or float(s[i-2])%1 != 0:
                            return 'Ошибка: операция % только для целых чисел\n\n\n'
                        result = float(s[i-2]) % float(s[i-1])
                    case "&":
                        if float(s[i-1]) == 0:
                            return 'Ошибка: деление на 0 невозможно\n\n\n'
                        elif float(s[i-1])%1 != 0 or float(s[i-2])%1 != 0:
                            return 'Ошибка: операция // только для целых чисел\n\n\n'
                        result = float(s[i-2]) // float(s[i-1])
                    case "^":
                        result = float(s[i-2]) ** float(s[i-1])
                    case _:
                        return "Ошибка ввода операторов и операндов"
                
                # Общая часть для всех операций
                s[i-2] = str(result)
                s.pop(i)
                s.pop(i-1)
                break

    return s






def calc(ex: str) -> str:
    
    """Сочетает в себе все служебные функции, calc(ввод)
    напрямую выдает результат, опираясь на служебные функции"""


    if isinstance(parse(ex), str):
        return stack
    else:
        checked_stack = check_brackets(parse(ex))

        if isinstance(checked_stack, str):
            return checked_stack
        else:
            return solve(checked_stack)[0]

        


ex = input("Введите выражение: \n")
print("\n", calc(ex), "\n\n", sep="")


    

