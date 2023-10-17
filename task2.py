salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
cur_month = 0
while cur_month != months:
    if cur_month != 0:
        spend += spend * increase
    money_capital += spend - salary
    cur_month += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
