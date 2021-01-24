def print_user(first_name, last_name, birth_year, city, email, phone_number):
    """Выводит информацию о пользователе одной строкой"""
    s = f"Данные пользователя: Имя - {first_name}, Фамилия - {last_name}, " + \
        f"Год рождения - {birth_year}, Город проживания - {city}, E-mail - {email}, Номер телефона - {phone_number}"
    print(s)


print_user(first_name="k", last_name="l", birth_year=76, city="i", email="a@gmail.com", phone_number="8(945)3459876")
