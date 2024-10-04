# class Product:
#    # Опишите инициализатор класса и метод get_info()
#    def __init__(self, product_name, amount):
#        self.product_name = product_name
#        self.amount = amount
#
#    def get_info(self):
#        return f"{self.product_name} (в наличии: {self.amount})"
#
#
# class Kettlebell(Product):
#    # Опишите инициализитор класса и метод get_weight()
#    def __init__(self, product_name, amount, weight):
#        self.weight = weight
#        super().__init__(product_name, amount)
#
#    def get_weight(self):
#        return f"{Product.get_info(self)}." f" Вес: {self.weight} кг"
#
#
# class Clothing(Product):
#    # Опишите инициализатор класса и метод get_size()
#    def __init__(self, product_name, amount, size):
#        self.size = size
#        super().__init__(product_name, amount)
#
#    def get_size(self):
#        return f"{Product.get_info(self)}. Размер {self.size}"
#
#
## Для проверки вашего кода создадим пару объектов
## и вызовем их методы:
# small_kettlebell = Kettlebell("Гиря малая", 15, 2)
# shirt = Clothing("Футболка", 5, "L")
#
# print(small_kettlebell.get_weight())
# print(shirt.get_size())
# small_k = Product(
#    "Гиря малая",
#    15,
# )
# print(small_k.get_info())
# Импортируйте нужную библиотеку.
# from datetime import datetime
#
#
# class Store:
#    def __init__(self, address):
#        self.address = address
#
#    def is_open(self, date):
#        # Метод is_open() в родительском классе всегда возвращает False,
#        # это "код-заглушка", метод, предназначенный для переопределения
#        # в дочерних классах.
#        return False
#
#    def get_info(self, date_str):
#        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
#        date_object = datetime.strptime(date_str, "%d.%m.%Y")
#
#        # Передайте в метод is_open() объект даты date_object и определите,
#        # работает ли магазин в указанную дату.
#        # В зависимости от результата будет выбрано значение
#        # для переменной info.
#
#        if self.is_open(date_object):
#            info = "работает"
#        else:
#            info = "не работает"
#        return f"Магазин по адресу {self.address} {date_str} {info}"
#
#
# class MiniStore(Store):
#    # Переопределите метод is_open().
#    # def __init__(self, address):
#    #    super().__init__(address)
#
#    def is_open(self, date):
#        # Метод is_open() в родительском классе всегда возвращает False,
#        # это "код-заглушка", метод, предназначенный для переопределения
#        # в дочерних классах.
#        print(date.weekday())
#        if date.weekday() in range(0, 5):
#            return True
#        return False
#
#
# class WeekendStore(Store):
#    # Переопределите метод is_open().
#    def is_open(self, date):
#        # Метод is_open() в родительском классе всегда возвращает False,
#        # это "код-заглушка", метод, предназначенный для переопределения
#        # в дочерних классах.
#        print(date.weekday())
#        if date.weekday() in range(5, 7):
#            return True
#        return False
#
#
# class NonStopStore(Store):
#    # Переопределите метод is_open().
#    def is_open(self, date):
#        # Метод is_open() в родительском классе всегда возвращает False,
#        # это "код-заглушка", метод, предназначенный для переопределения
#        # в дочерних классах.
#        print(date.weekday())
#        # if date.weekday() in range(5, 7):
#        #    return True
#        return True
#
#
# mini_store = MiniStore("Улица Немига, 57")
# print(mini_store.get_info("29.03.2024"))
# print(mini_store.get_info("30.03.2024"))
#
# weekend_store = WeekendStore("Улица Толе би, 321")
# print(weekend_store.get_info("29.03.2024"))
# print(weekend_store.get_info("30.03.2024"))
#
# non_stop_store = NonStopStore("Улица Арбат, 60")
# print(non_stop_store.get_info("29.03.2024"))
# print(non_stop_store.get_info("30.03.2024"))
from decimal import Decimal, getcontext


class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price):
        getcontext().prec = 4
        new_price = price - (price * self.__discount / 100)
        return Decimal(str(new_price))

    def set_discount(self, discount):
        if discount <= 80:
            self.__discount = discount
        elif discount > 80:
            self.__discount = 80


customer = Customer("Иван Иванович")
print(customer.get_price(100))
customer.set_discount(20)
print(customer.get_price(100))
