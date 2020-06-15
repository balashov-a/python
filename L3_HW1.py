def my_func(a,b):
    try:
        answer = a / b
    except ZeroDivisionError:
        return "Делить на ноль нельзя"
    return answer

try:
    var_1 = float(input("Введите делимое: "))
    var_2 = float(input("Введите делитель: "))
    print("Ответ:", my_func(var_1, var_2))
except ValueError:
    print("Вы ввели не число, повторите пожалуйста")