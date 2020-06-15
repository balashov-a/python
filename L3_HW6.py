word = "word"
text = "some text with words"

def int_func(my_str):
    return my_str.capitalize()

print(int_func(word))
print(" ".join(list(map(int_func, text.split()))))