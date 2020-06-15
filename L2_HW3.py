user_month = int(input("Введите номер месяца (от 1 до 12)"))
while user_month not in range(1, 13):
    user_month = int(input("Число должно быть от 1 до 12. Введите пожалуйста еще раз номер месяца (от 1 до 12)"))
seasons = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11] }
for season, months_in_season in seasons.items():
    for one_of_the_months in months_in_season:
        if one_of_the_months == user_month:
            print("Время года:", season)
