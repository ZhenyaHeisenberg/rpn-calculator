import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from constants import OPERATORS
from def_check_operators import check_operators

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
