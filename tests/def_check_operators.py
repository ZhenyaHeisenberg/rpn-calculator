def check_operators(substack): #проверяет, верно ли колличество операторов
    if len(substack) != (2 * (substack.count("+") + substack.count("-") + substack.count("*") + substack.count("/") + substack.count("%") + substack.count("&") + substack.count("^")) + substack.count("~") + 1):
        return 0
    else:
        return 1
