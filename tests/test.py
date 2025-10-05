from def_parse import parse
from def_solve import solve





"""Не проверяет корректность выражения, а лишь создает стек"""
# Тесты parce()
def test_parse():
    
    assert parse("9 0 /") == ['9', '0', '/']
    assert parse("3 4 +") == ['3', '4', '+']
    assert parse("5 8 -") == ['5', '8', '-']
    assert parse("3.5 5,8 /") == ['3.5', '5.8', '/']
    assert parse("3 6 - 6 *") == ['3', '6', '-', '6', '*',]
    assert parse("5 9 ^ -9 //") == ['5', '9', '^', '-9', '&']
    assert parse("3 (4 6) * + 9 %") == ['3', '4', '6', '*', '+', '9', '%']
    assert parse("3 ~   2 %   9   ^ 0 - ( 9  5 ) - +") == ['3', '~', '2', '%', '9', '^', '0', '-', '9', '5', '-', '+']
    
    




# Тесты solve()
def test_solve():

    assert solve(['3', '4', '+']) == 7.0
    assert solve(['3', '4', '^']) == 81.0
    assert solve(['3', '4', '6', '*', '+', '9', '%']) == 0.0
    assert solve(['81', '0.5', '^']) == 9.0
    assert solve(['3.6', '9.5', '*']) == 34.2
    assert solve(['66', '6', '/', '2', '^']) == 121.0


# Общие тесты solve(parce()) 
def test_main():

    assert solve(parse("9 3 /")) == 3.0
    assert solve(parse("3 6 - 6 *")) == -18.0
    assert solve(parse("3 (4 6) * + 9 %")) == 0
    assert solve(parse("3 ~   2 %   9   ^ 0 - ( 9  5 ) - +")) == 5.0
    assert solve(parse("(4 6) +  8 %   4 7    - ~ ^ ")) == 8.0


def test_error():

    assert solve(['9', '0', '+', '+']) == "Ошибка ввода операторов и операндов"
    assert solve(['8', '6', '6', '-', '/']) == "Ошибка: деление на 0 невозможно"
    assert solve(['6.4', '2', '%']) == 'Ошибка: операция "%" только для целых'




if __name__ == "__main__":
    # Запускаем все тестовые функции
    test_parse()
    test_solve()
    test_main()
    test_error()

    print("✅ Все тесты прошли успешно!")

