while True:
    
    ex = input("Введите выражение: \n")

    operators = "+-*/%&^"
    
    def check_operators(substack): #проверяет, верно ли колличество операторов
        if len(substack) != (2 * (substack.count("+") + substack.count("-") + substack.count("*") + substack.count("/") + substack.count("%") + substack.count("&") + substack.count("^")) + substack.count("~") + 1):
            return 0
        else:
            return 1
        
    
    def parse(ex): #Преобразует строку в стек

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

    stack = parse(ex)

    def check_brackets(stack): #проверяет, верно ли расставлены скобки
            
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

    
    checked_stack = check_brackets(stack)

    def solve(checked_stack): #принимает стек, выдает ответ

        s = checked_stack

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
                            return 'Ошибка: деление на 0 невозможно\n\n\n' 

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






    def calc(ex):
        if type(stack) == str:
            return stack
        else:
            checked_stack = check_brackets(stack)

            if type(checked_stack) == str:
                return checked_stack
            else:
                return solve(checked_stack)[0]
    
    print("\n", calc(ex), "\n\n", sep="")
    

