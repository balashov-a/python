file_in_name = "text4in.txt"
file_out_name = "text4out.txt"
dict_en_ru = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(file_in_name, "r", encoding='utf-8') as file_in:
    text = file_in.read()

for i in dict_en_ru:
    text = text.replace(i, dict_en_ru.get(i))

with open(file_out_name, "w", encoding='utf-8') as file_out:
    file_out.write(text)