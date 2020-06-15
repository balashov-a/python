income = int(input("Введите вашу выручку"))
expenses = int(input("Введите ваши издержки"))
staff = int(input("Введите количество ваших сотрудников"))
profit = income - expenses
profit_per_staff = profit / staff

if profit > 0:
    print("Ваша прибыль составляет", profit, 'рублей')
    print(f"Прибыль на сотрудника составляет {profit_per_staff:.0f} рублей на каждого сотрудника")
elif profit == 0:
    print("У вас нулевая прибыль")
else:
    print('Вы работаете в убыток, у вас', profit, 'р', 'дохода' )
