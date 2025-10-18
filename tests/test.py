from def_parse import parse
from def_solve import solve
from def_check_brackets import check_brackets



# Тесты parse()
"""Проверяет на наличие неоткрытых/незакрытых скобок, создает стек"""
def test_parse():
    
    assert parse("9 0 /") == ['9', '0', '/']
    assert parse("3 4 +") == ['3', '4', '+']
    assert parse("5 8 -") == ['5', '8', '-']
    assert parse("3.5 5,8 /") == ['3.5', '5.8', '/']
    assert parse("3 6 - 6 *") == ['3', '6', '-', '6', '*',]
    assert parse("5 9 ^ -9 //") == ['5', '9', '^', '-9', '&']
    assert parse("3 ~   2 %   9   ^ 0 - ( 9  5 ) - +") == ['3', '~', '2', '%', '9', '^', '0', '-', '(', '9', '5', ')', '-', '+']
    assert parse(") 9 0 / (") == "Ошибка: есть неоткрытые скобки"
    


# Тесты check_brackets()
"""Проверяет, правильно ли расставлены скобки, после чего удаляет их или выводит ошибку"""
def test_check_brackets():
    
    assert check_brackets(['(', '4', '3', '+', ')'])  == ['4', '3', '+']
    assert check_brackets(['(', '4', '3', '+', ')', '10', '-']) == ['4', '3', '+', '10', '-']
    assert check_brackets(['(', '4', '3', ')', '+'])  == "Ошибка ввода операторов и операндов"
   
    

# Тесты solve()
"""Преобразует стек в ответ"""
def test_solve():

    assert solve(['3', '4', '+']) == ['7.0']
    assert solve(['3', '4', '^']) == ['81.0']
    assert solve(['81', '0.5', '^']) == ['9.0']
    assert solve(['3.6', '9.5', '*']) == ['34.2']
    assert solve(['66', '7', '&', '2', '^']) == ['81.0']
    assert solve(['66', '6', '/', '2', '^']) == ['121.0']
    assert solve(['3', '4', '6', '*', '+', '9', '%']) == ['0.0']


# Общие тесты solve(parce()) 
def test_main():

    assert solve(check_brackets(parse("9 3 /"))) == ['3.0']
    assert solve(check_brackets(parse("3 6 - 6 *"))) == ['-18.0']
    assert solve(check_brackets(parse("3 (4 6) * + 9 %"))) == "Ошибка ввода операторов и операндов"
    assert solve(check_brackets(parse("3 ~   2 %   9   ^ 0 - ( 9  5 ) - +"))) == "Ошибка ввода операторов и операндов"
    assert solve(check_brackets(parse("(4 6) +  8 %   4 7    - ~ ^ "))) == "Ошибка ввода операторов и операндов"
    assert solve(check_brackets(parse("5 2 // 4 + 3 ^   4  6 + *"))) == ['2160.0']




if __name__ == "__main__":
    # Запускаем все тестовые функции
    test_parse()
    test_solve()
    test_check_brackets()
    test_main()

    print("✅ Все тесты прошли успешно!")

