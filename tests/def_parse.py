def parse(ex: str) -> list[str] | str: #Преобразует строку в стек

    brackets_count = 0
    for i in range(len(ex)):
        if ex[i] == "(":
            brackets_count += 1
        elif ex[i] == ")":
            brackets_count -= 1
        if brackets_count < 0:
            return 'Ошибка: есть неоткрытые скобки'
    if brackets_count != 0:
        return 'Ошибка: есть незакрытые скобки'

    ex = ex.replace("//", "&")
    ex = ex.replace("(", " ( ")
    ex = ex.replace(")", " ) ")
    ex = ex.replace(",", ".")
        
    

    stack = ex.split() # (1)
    
    return stack
