import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.current_date = dt.date.today()
        self.days_ago = self.current_date - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.current_date:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.days_ago <= record.date <= self.current_date:
                week_stats.append(record.amount)
        return sum(week_stats)


class CashCalculator(Calculator):
    rub = 1
    dollar = 60.73
    euro = 59.79

    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('dollars', self.dollar),
                      'eur': ('euros', self.euro),
                      'rub': ('руб', self.rub)}
        delta_cash = self.limit - self.get_today_stats()
        name, rate = currencies.get(currency)
        delta_cash = delta_cash / rate
        if delta_cash == 0:
            message = f'Денег нет, держись'
        elif delta_cash > 0:
            message = f'На сегодня осталось {delta_cash} {name}'
        else:
            delta_cash < 0
            message = f'Денег нет, держись, твой долг: {abs(delta_cash)} {name}'
        return message, delta_cash


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        delta_calories = self.limit - self.get_today_stats()
        if delta_calories > 0:
            message = f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более' \
                      f' {delta_calories} Ккал'
        else:
            message = f'Хватит есть!'
        return message, delta_calories


cash_calculator = CashCalculator(1000)
cal_calculator = CaloriesCalculator(2500)
cash_calculator.add_record(Record(amount=140, comment='кофе'))
cal_calculator.add_record(Record(amount=300, comment='завтрак'))
print(cash_calculator.get_today_cash_remained('rub')[0])
print(cal_calculator.get_calories_remained()[0])
