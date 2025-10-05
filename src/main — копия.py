while True:
    ex = input("Введите выражение:\n")

    operators = "+-*/%&^"

    def parse(ex):

        ex = ex.replace("//", "&")
        ex = ex.replace("(", " ( ")
        ex = ex.replace(")", " ) ")
        ex = ex.replace(",", "main.py")
        

        if ex.count("(") != ex.count(")"):
            return "Error_1" #Ошибка: неравное колличество символов "(" и ")"
        else:
            ex = ex.replace("(", "")
            ex = ex.replace(")", "")

            

        
        
        
            

        s = ex.split()

        if len(s) != (2 * (s.count("+") + s.count("-") + s.count("*") + s.count("/") + s.count("%") + s.count("&") + s.count("^")) + s.count("~")) + 1: #(кол-во бинарных операторов) * 2 + кол-во унарных операторов + 1 == кол-во элементов в стеке (условие правильности записи операторов и операндов в обратной польсокй нотации) 
            return "Error_2" #Ошибка ввода операторов и операндов

        
        return s




    result = parse(ex)



    def solve(result):

        s = result

        
        while len(s) > 1:
            for i in range(len(s)):

                if s[i] == "~" and i > 0:
                        s[i-1] = float(s[i-1]) * (-1)
                        s.pop(i)
                        break
                elif s[i] == "~" and i == 0:
                    return "Ошибка ввода операторов"
                
                if str(s[i]) in operators and i < 2:
                    return "Ошибка ввода операторов"
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
                            return 'Error_5' 

                    if s[i] == "%":
                        if float(s[i-2]) % 1 == 0 and float(s[i-1]) % 1 == 0:
                            s[i-2] = float(s[i-2]) % float(s[i-1])
                            s.pop(i)
                            s.pop(i-1)
                            break
                        else:
                            return 'Error_3' 

                    if s[i] == "&":
                        if float(s[i-2]) % 1 == 0 and float(s[i-1]) % 1 == 0:
                            s[i-2] = float(s[i-2]) // float(s[i-1])
                            s.pop(i)
                            s.pop(i-1)
                            break
                        else:
                            return 'Error_4' 

                    if s[i] == "^":
                        s[i-2] = float(s[i-2]) ** float(s[i-1])
                        s.pop(i)
                        s.pop(i-1)
                        break

        return s


    if type(result) == str:
        if result == "Error_1":
            print('Ошибка: неравное колличество символов "(" и ")"\n\n\n')
        elif result == "Error_2":
            print('Ошибка ввода операторов и операндов\n\n\n')
        elif result == "Error_3":
            print('Ошибка: операция "%" только для целых\n\n\n')
        elif result == "Error_4":
            print('Ошибка: операция "//" только для целых\n\n\n')
        
    else:
        print(" ")
        print("Ответ: ", solve(result)[0], "\n\n\n")






