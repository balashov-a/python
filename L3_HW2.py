user_name = "Иван"
user_lastname = "Иванов"
user_birthdate = 1985
user_city = "Москва"
user_email = "some_email@gmail.com"
user_phone = 79991112233

def my_func(name, lastname, birthdate, city, email, phone):
    return print(f"{name} {lastname}, {birthdate} года рождения, проживает в г. {city}. Email: {email}, Тел: {phone}")

my_func(name = user_name, lastname = user_lastname, birthdate = user_birthdate, city = user_city, email = user_email, phone = user_phone)