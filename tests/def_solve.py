def solve(checked_stack): #принимает стек, выдает ответ
    if type(checked_stack) == str:
        return checked_stack

    s = checked_stack
    operators = "+-*/%&^"

    while len(s) > 1:
        for i in range(len(s)):

            if s[i] == "~" and i > 0: # (2)
                    s[i-1] = float(s[i-1]) * (-1)
                    s.pop(i)
                    break
            elif s[i] == "~" and i == 0:
                return "Ошибка ввода операторов и операндов"
                
            if str(s[i]) in operators and i < 2: # (3)
                    
                return "Ошибка ввода операторов и операндов"
            elif str(s[i]) in operators and i >= 2:

                    
                if s[i] == "+":
                    s[i-2] = float(s[i-2]) + float(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break

                if s[i] == "-":
                    s[i-2] = float(s[i-2]) - float(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break

                if s[i] == "*":
                    s[i-2] = float(s[i-2]) * float(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break

                if s[i] == "/":
                    if float(s[i-1]) != 0:
                        s[i-2] = float(s[i-2]) / float(s[i-1])
                        s.pop(i)
                        s.pop(i-1)
                        break
                    else:
                        return 'Ошибка: деление на 0 невозможно' 

                if s[i] == "%":
                    if float(s[i-2]) % 1 == 0 and float(s[i-1]) % 1 == 0:
                        s[i-2] = float(s[i-2]) % float(s[i-1])
                        s.pop(i)
                        s.pop(i-1)
                        break
                    else:
                        return 'Ошибка: операция "%" только для целых\n\n\n'

                if s[i] == "&":
                    if float(s[i-2]) % 1 == 0 and float(s[i-1]) % 1 == 0:
                        s[i-2] = float(s[i-2]) // float(s[i-1])
                        s.pop(i)
                        s.pop(i-1)
                        break
                    else:
                        return 'Ошибка: операция "//" только для целых\n\n\n' 

                if s[i] == "^":
                    s[i-2] = float(s[i-2]) ** float(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break

    return s
