def my_func(var_1, var_2, var_3):
    arr = [var_1, var_2, var_3]
    var_max = max(arr)
    arr.remove(var_max)
    return var_max + max(arr)

print(my_func(15,5,27))