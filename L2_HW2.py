my_list = input("Ввести несколько элементов с пробелами: ").split()
index = 0

while index < len(my_list) - 1:
    if index % 2 == 0:
        my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    index  += 1
print(my_list)