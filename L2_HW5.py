my_list = [7, 5, 3, 3, 7]
print("Текущий рейтинг: ", my_list)
rate = int(input("Поставьте оценку от 1 до 10: "))
if  0 < rate < 11:
    my_list.append(rate)
    print("Новый рейтинг: ", sorted(my_list)[::-1])
else:
    print("Оценкой может быть только число от 1 до 10")