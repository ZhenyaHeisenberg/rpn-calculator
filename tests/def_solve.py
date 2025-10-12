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

            if s[i] == "~" and i > 0: # (2)
                s[i-1] = str(float(s[i-1]) * (-1))
                s.pop(i)
                break
            elif s[i] == "~" and i == 0:
                return "Ошибка ввода операторов и операндов"
                
            if s[i] in OPERATORS and i < 2: # (3)
                    
                return "Ошибка ввода операторов и операндов"
            elif str(s[i]) in OPERATORS and i >= 2:

                    
                if s[i] == "+":
                    s[i-2] = str(float(s[i-2]) + float(s[i-1]))
                    s.pop(i)
                    s.pop(i-1)
                    break

                if s[i] == "-":
                    s[i-2] = str(float(s[i-2]) - float(s[i-1]))
                    s.pop(i)
                    s.pop(i-1)
                    break

                if s[i] == "*":
                    s[i-2] = str(float(s[i-2]) * float(s[i-1]))
                    s.pop(i)
                    s.pop(i-1)
                    break

                if s[i] == "/":
                    if float(s[i-1]) == 0:
                        return 'Ошибка: деление на 0 невозможно\n\n\n'
                    else:
                        s[i-2] = str(float(s[i-2]) / float(s[i-1]))
                        s.pop(i)
                        s.pop(i-1)
                        break
                         

                if s[i] == "%":
                    if float(s[i-2]) % 1 == 0 and float(s[i-1]) % 1 == 0:
                        s[i-2] = str(float(s[i-2]) % float(s[i-1]))
                        s.pop(i)
                        s.pop(i-1)
                        break
                    else:
                        return 'Ошибка: операция "%" только для целых\n\n\n'

                if s[i] == "&":
                    if float(s[i-2]) % 1 == 0 and float(s[i-1]) % 1 == 0:
                        s[i-2] = str(float(s[i-2]) // float(s[i-1]))
                        s.pop(i)
                        s.pop(i-1)
                        break
                    else:
                        return 'Ошибка: операция "//" только для целых\n\n\n' 

                if s[i] == "^":
                    s[i-2] = str(float(s[i-2]) ** float(s[i-1]))
                    s.pop(i)
                    s.pop(i-1)
                    break

    return s
