
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

            

        
        
        
            

    s = ex.split() # (1)

    if len(s) != (2 * (s.count("+") + s.count("-") + s.count("*") + s.count("/") + s.count("%") + s.count("&") + s.count("^")) + s.count("~")) + 1: #(кол-во бинарных операторов) * 2 + кол-во унарных операторов + 1 == кол-во элементов в стеке (условие правильности записи операторов и операндов в обратной польсокй нотации) 
        return 'Ошибка ввода операторов и операндов\n\n\n'
        
    return s
