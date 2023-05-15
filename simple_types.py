import datetime

year = datetime.date.today().year

birth_year = input('Введите год вашего рождения ')
real_age = year - int(birth_year)
print(f'Ваш возраст: {real_age}')
