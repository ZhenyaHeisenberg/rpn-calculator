while True:
    
    ex = input("Введите выражение: \n")

    operators = "+-*/%&^"
    
    
        
    def parse(ex):

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
        

        ex = ex.replace("(", "")
        ex = ex.replace(")", "")

            

        
        
        
            

        register = ex.split() # (1)

        if len(register) != (2 * (register.count("+") + register.count("-") + register.count("*") + register.count("/") + register.count("%") + register.count("&") + register.count("^")) + register.count("~")) + 1: # (4)
            return 'Ошибка ввода операторов и операндов\n\n\n'
        
        return register




    result = parse(ex)


    def solve(result):

        s = result

        
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


    if type(result) == str:
        print('\n', result, sep = "")
        
    else:
        print("\nОтвет: ", solve(result)[0], "\n\n\n")



