# def print_pack_report(starting_value):
#    # Дополните функцию
#    for number in reversed(range(1, starting_value+1)):
#        if number % 3 == 0 and number % 5 == 0:
#            print(f'{number} - расфасуем по 3 или по 5')
#        elif number % 3 != 0 and number % 5 == 0:
#            print(f'{number} - расфасуем по 5')
#        elif number % 3 == 0 and number % 5 != 0:
#            print(f'{number} - расфасуем по 3')
#        else:
#            print(f'{number} - не заказываем!')


# def count_canisters(temperatures_per_day):
#    hot_days_counter = 0
#    # Допишите функцию.
#    for day in temperatures_per_day:
#        if day >= 30:
#            hot_days_counter += 1
#    return hot_days_counter
#
#
# forecast_temperatures = [26, 28, 30, 31, 29, 31, 28, 26]
## Вызовите функцию и напечатайте результат в нужном формате.
# print(count_canisters(forecast_temperatures))


# def print_multiplication_table():
#    # Напишите код, который напечатает таблицу умножения.
#    for x in range(1,10):
#        for y in range(1,10):
#            print(f'{x} * {y} = {x*y}')
#        print('-'*10)
#
#
# print_multiplication_table()

# races_data = [
#    {"Ferrari": 20, "Mercedes": 5, "Aston Martin": 10, "Williams": 15},
#    {"Mercedes": 15, "Aston Martin": 20, "Ferrari": 10, "Williams": 0},
#    {"Ferrari": 20, "Williams": 15, "Aston Martin": 10, "Mercedes": 5},
# ]
#
#
# def get_competition_data(racers_list):
#    comand_names = list(racers_list[0].keys())
#    comand_names.sort()
#    teams = {team: 0 for team in comand_names}  #  make dict where value == 0
#    for race in racers_list:  # unpack dict
#        for team, score in race.items():  #  unpack values from dict
#            if team in teams:
#                teams[team] += score  #  if team in dict add scores
#            # else:
#            #    print('not in race')
#    winner_team = None
#    winner_score = 0
#    for team, score in teams.items():
#        if winner_score < score:
#            winner_score = score
#            winner_team = team
#    print(
#        f"Команды, участвовавшие в гонке: {comand_names[0]},"
#        f"{comand_names[1]}, {comand_names[2]}, {comand_names[3]}"
#    )
#    print(f"В гонке победила команда {winner_team} с результатом {winner_score} баллов")
#
#
# get_competition_data(races_data)
#
#
# def add(operand_x, operand_y):
#    return operand_x + operand_y
#
#
# x = 10
# y = 5
# print("Сумма чисел:", add(x, y))
"""
from math import sqrt
from typing import Optional, Union


 def add_numbers(x: int, y: int) -> int:
    return x + y


def Calculate_Square_Root(number: Union[float, int]) -> float:
    return sqrt(number)


def calc(your_number: Union[float, int]) -> Optional[str]:
    if your_number <= 0:
        return None
    return (
        f"Мы вычислили квадратный корень из введённого вами числа."
        f"Это будет: {Calculate_Square_Root(your_number)}"
    )


x = 10
y = 5

print("Сумма чисел: ", add_numbers(x, y))
print(calc(25.5)) """

# class Employee:
#    vacation_days = 28
#
#    def __init__(self, first_name, second_name, gender):
#        self.first_name = first_name
#        self.second_name = second_name
#        self.gender = gender
#        self.remaining_vacation_days = Employee.vacation_days
#        self._employee_id = self.__generate_employee_id()
#
#    def consume_vacation(self, days):
#        self.remaining_vacation_days -= days
#
#    def get_vacation_details(self):
#        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
#
#    def __generate_employee_id(self):
#        emp_id = hash(self.first_name + self.second_name + self.gender)
#        return emp_id
#
#
# class FullTimeEmployee(Employee):
#    def __init__(self, first_name, second_name, gender, salary):
#        super().__init__(first_name, second_name, gender)
#        self.__salary = salary
#
#    def __get_vacation_salary(self):
#        vacation_salary = self.__salary * 0.8
#        return vacation_salary
#
#
#    def get_unpaid_vacation(self, start_date, days):
#        return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'
#
#
# class PartTimeEmployee(Employee):
#    vacation_days = 14
#
#    def __init__(self, first_name, second_name, gender):
#        super().__init__(first_name, second_name, gender)
#        self.remaining_vacation_days = PartTimeEmployee.vacation_days
#
#
## Пример использования:
# full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
# part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
# print(full_time_employee._FullTimeEmployee__get_vacation_salary())
# print(full_time_employee._employee_id)
# print(part_time_employee._employee_id)
#
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
# Импортируйте необходимые модули.
from datetime import datetime
from random import sample

# Напишите декоратор obfuscator
# adict = {"name": "StasBasov", "password": "iamthebest"}
#
#
# def obfuscator(func):
#    def wrapper():
#        result = func()
#        for key in result.keys():
#            if key == "name":
#                new_data = ""
#
#                loggin = result["name"]
#                counter = 0
#                while counter < len(loggin):
#                    for char in loggin:
#                        if loggin.index(char) == 0 or counter == len(loggin) - 1:
#                            # print(loggin.index(char))
#                            # print(len(loggin) - 1)
#                            new_data += char
#                            counter += 1
#                        else:
#                            char = "*"
#                            new_data += char
#                            counter += 1
#                    result["name"] = new_data
#            elif key == "password":
#                new_data = ""
#                password = result["password"]
#                for char in password:
#                    char = "*"
#                    new_data += char
#                result["password"] = new_data
#        return result
#
#    return wrapper
#
#
## print(obfuscator(adict))
#
#
# @obfuscator
# def get_credentials():
#    return {"name": "BasovStas", "password": "rootpermissions"}
#
#
# print(get_credentials())
from typing import Optional

# Укажите два параметра функции:
# def validate_record(name, date):
#    date_format = "%d.%m.%Y"
#    date_ok = True
#    try:
#        datetime.strptime(date, date_format)
#        return date_ok
#    except ValueError:
#        print(f"Некорректный формат даты в записи: {name}, {date}")
#        return not date_ok
#
#    pass
#
#
## Укажите параметры функции:
# def process_people(data):
#    # Объявите счётчики.
#    good_counter = 0
#    bad_counter = 0
#    # wrong_date_f = []
#    # right_date_f = []
#
#    for date_value in data:
#        formate_check = validate_record(date_value[0], date_value[1])
#        if formate_check is True:
#            good_counter += 1
#        else:
#            bad_counter += 1
#
#    # print("x-", wrong_date_f)
#    # print("o-", right_date_f)
#    print(f"Некорректных записей: {bad_counter}\nКорректных записей: {good_counter}")
#    # в каждой паре значений из списка data
#    # проверьте корректность формата даты рождения
#    # и в зависимости от результата проверки увеличьте один из счётчиков.
#    pass
#
#
# data = [
#    ("Иван Иванов", "10.01.2004"),
#    ("Пётр Петров", "15.03.1956"),
#    ("Зинаида Зеленая", "6 февраля 1997"),
#    ("Елена Ленина", "Второе мая тысяча девятьсот восемьдесят пятого"),
#    ("Кирилл Кириллов", "26/11/2003"),
# ]
# process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>


# def choose_days():
#    # Определяем диапазон дат первой половины месяца.
#    first_month_half = list(range(0, 15))
#
#    # Выбор трёх случайных чисел:
#    random_days = sample(first_month_half, k=3)
#    # Cортировка этих чисел по возрастанию:
#    sorted_days = sorted(random_days)
#    print(sorted_days)
#
#    # Получаем сегодняшнюю дату.
#    # На её основе будут генерироваться даты для занятий:
#    now = datetime.now()
#
#    # Чтобы было проще формировать сообщение, начнём цикл с 1.
#    for i in range(0, 3):
#        # Генерируем дату занятия, подменяя номер дня в сегодняшней дате.
#        practice_day = now.replace(day=sorted_days[i]).strftime("%d.%M.%Y")
#        print(f"{i}-е занятие: {practice_day}")
#
#
# choose_days()
# class Product:
#    def __init__(self, name, retail_price, purchase_price):
#        self.name = name
#        self.retail_price = retail_price
#        self.purchase_price = purchase_price
#
#    # Опишите свойство profit
#    @property
#    def profit(self):
#        income = self.retail_price - self.purchase_price  # ?
#        return income
#
#    # Опишите статический метод average_price()
#    @staticmethod
#    def average_price(prices):
#        avg_price = sum(prices) / len(prices)
#        return int(avg_price)
#
#    # Опишите свойство information
#    @property
#    def information(self):
#        return f"Товар: {self.name}, розничная цена: {self.retail_price}, закупочная цена: {self.purchase_price}"
#
#
## Данные для проверки, не изменяйте их.
# product_1 = Product("Картошка", 100, 90)
# product_2 = Product("Перчатки", 150, 120)
# product_3 = Product("Велосипед", 170, 150)
#
# assortment_prices = [
#    product_1.retail_price,
#    product_2.retail_price,
#    product_3.retail_price,
# ]
#
# print(f"Средняя стоимость: {Product.average_price(assortment_prices)}")
# print(f"Прибыль магазина с товара {product_1.name}: {product_1.profit}")
# print(f"Информация о товаре {product_1.name}: {product_1.information}")

# Ссылка на урок: [Спринт 3/19 → Тема 5/7: Расширенные возможности Python → Урок 7/8: Практика по теме]( https://practicum.yandex.ru/trainer/backend-developer/lesson/3eaa941a-aeac-48a0-b554-24337efa6249/task/347f6bf9-93b3-4286-87f7-6dac6e9ddf3d/ )


# def fibonacci(n):
#    # Допишите функцию.
#    x = 0
#    y = 1
#    first_numbers = (x, y)
#    if n == 0:
#        yield x
#    elif n == 1 or n != 1 and n > 1:
#        for number in first_numbers:
#            yield number
#        for _ in range(2, n):
#            z = x + y
#            x = y
#            y = z
#            # element[n] = element[n - 1] + element[n - 2]
#            yield y
#
#
# sequence = fibonacci(10)
# for number in sequence:
#    print(number)


class User:
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError("Необходимо указать параметры пользователя")

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(cls, name, last_name):
        cls.first_name = name
        cls.last_name = last_name
        return cls(name, last_name)

    def hello(self):
        return f"hello my name is {self.username}"

    # Опишите метод класса with_username.
    @classmethod
    def with_username(cls, username):
        if User.is_username_allowed(username) is True:
            cls.username = username
            # print(cls.username)
            # print("yes")
            return cls(first_name=None, last_name=None, username=username)
        else:
            raise ValueError("Некорректное имя пользователя")

    # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: str):
        if "admin" in username.lower()[0:5]:
            return False
        return True

    # Опишите метод-свойство full_name.
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.username:
            return f"@{self.username}"


def is_username_allowed(username: str):
    if "admin" in username.lower():
        return False
    return True


# stas = User.with_name("Стас", "Басов")
# print(stas.full_name)
# print(is_username_allowed(input("Your word here: ")))

# Попробуем создать пользователя с "запрещённым" именем.
ne_stas = User.with_username("not_admin")
# print(ne_stas.hello())
print(ne_stas.full_name)
