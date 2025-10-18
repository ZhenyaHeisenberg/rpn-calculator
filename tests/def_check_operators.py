def check_operators(substack: list[str]) -> bool: #проверяет, верно ли колличество операторов
    return len(substack) == (2 * (substack.count("+") + substack.count("-") + substack.count("*") + substack.count("/") + substack.count("%") + substack.count("&") + substack.count("^")) + substack.count("~") + 1)
