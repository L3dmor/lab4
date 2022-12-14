from lab_3 import Record, CaloriesCalculator, CashCalculator
import pytest

zapisi = []


@pytest.fixture()
def test_Calories_Calculator():
    calculate = CaloriesCalculator(500)
    calculate.add_record((Record(amount=400, comment='Завтрак')))
    return calculate.get_calories_remained()


@pytest.fixture()
def test_Cash_Calculator():
    calculate = CashCalculator(150)
    calculate.add_record((Record(amount=160, comment='Булочка')))
    return calculate.get_today_cash_remained('rub')


def test_cal_calc(test_Calories_Calculator):
    assert (
            test_Calories_Calculator[
                0] == f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {test_Calories_Calculator[1]} Ккал'
            or test_Calories_Calculator[0] == 'Хватит есть!')
    print("\n", test_Calories_Calculator[0])


def test_cash_calc(test_Cash_Calculator):
    assert (test_Cash_Calculator[0] == f'На сегодня осталось {test_Cash_Calculator[1]} руб'
            or test_Cash_Calculator[0] == 'Денег нет, держись'
            or test_Cash_Calculator[0] == f'Денег нет, держись, твой долг: {abs(test_Cash_Calculator[1])} руб')
    print("\n", test_Cash_Calculator[0])


@pytest.mark.parametrize("a", [(1),
                               (2),
                               (3)
                               ])
def test_1_good(a):
    zapisi.clear()
    zapisi.append(Record(amount=100, comment='Тест'))
    zapisi.append(Record(amount=100, comment='Тест'))
    zapisi.append(Record(amount=100, comment='Тест'))
    k = len(zapisi)
    assert k > a
