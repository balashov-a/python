my_list = [1, 1.7, "Text", [1, 2, 3], True, (1, 2.5, "text"), {1, 2, 3, "text"}, { 1: 1, 2: 2, 3: 'Text'}, bytearray(b'text') ]
for el, value in enumerate(my_list):
    print(f"{el}. {value} - type ({type(value)})")