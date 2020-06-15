while True:
    km_start = int(input("Со скольки километров вы планируете начать бегать?"))
    km_finish = int(input("На скольки километрах вы планируете остановиться?"))
    days = 1
    if km_finish < km_start:
        print('Конечный результат не может быть меньше начального. Попробуйте еще раз')
    elif km_start < 0 or km_finish < 0:
        print('результаты не могут быть меньше нуля')
    else:
        while km_start < km_finish:
            km_start +=km_start * 0.1
            days += 1
        print(f"Количество дней, необходимых для достижения результата: {days}")
        break
