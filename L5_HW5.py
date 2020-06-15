file_name = "text5.txt"
my_str = "1 2 3 4 5 6 7 8 9 10"

print("Набор чисел:", my_str)

with open(file_name, "w", encoding='utf-8') as f_obj:
    f_obj.writelines(my_str)

print(f"Числа записаны в {file_name}")

with open(file_name) as f_obj:
    for line in f_obj:
        my_sum = sum(list(map(int, line.split(" "))))

print("Сумма всех чисел в этом файле:", my_sum)