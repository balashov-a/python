var_1 = 15
var_2 = -3

def method_1(x, y):
    return x ** y

def method_2(x, y):
    result = x
    for _ in range(1, abs(y)):
        result *= x
    return 1 /result

print(f"Вовзедение числа {var_1} в степень {var_2} с помощью оператора '**', результат: ", method_1(var_1, var_2) )
print(f"Вовзедение числа {var_1} в степень {var_2} с помощью  'for in' , результат: ", method_2(var_1, var_2) )