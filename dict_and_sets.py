#Задача 3 Операции с коллекциями урок 7/10
#Ваша задача — разработать систему для работы сервисного центра всемирно известной компании "Cucumber".
#Она выпускает мобильные гаджеты и устройства для «умного дома».
#Полный перечень техники производства "Cucumber" c указанием модельного ряда содержится в словарях mobile_devices и home_devices.
#Каждый день компания присылает перечень устройств, поддержка которых прекращена. Перечень хранится в множестве not_supported_devices.
#Задача программы — заполнить словарь result_catalog: в него должны попасть только те устройства, поддержку которых компания не прекратила.
#Ключами словаря должны быть названия устройств, а значениями — годы выпуска, например, 'cucuEar': 2018.
#Выведите на экран строку 'Каталог поддерживаемых девайсов:'; на следующей строке напечатайте словарь result_catalog. 

mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}
result_catalog = {}

#def get_supported_catalog(devices, dict_devices):
#    supported_catalog = {}
#    not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}
#    for divice in devices:
#        if divice not in not_supported_devices:
#            #print(divice)
#            supported_catalog[divice] = dict_devices[divice]
#    return supported_catalog
##    print(supported_catalog)
#
#
#mobile_list = list(mobile_devices.keys())
#home_list = list(home_devices.keys())
#supported_devices = {0}
#
#mobile = get_supported_catalog(mobile_list, mobile_devices)
#home = get_supported_catalog(home_list, home_devices)
#result_catalog.update(mobile)
#result_catalog.update(home)
#print(result_catalog)
not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_catalog = {}

# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices:
        supported_catalog[device] = dict_devices[device]
    return supported_catalog


all_devices = set(mobile_devices).union(home_devices)
supported_devices = all_devices.difference(not_supported_devices)


for device in supported_devices:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
#    # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_mob_dev)
    supported_home_dev = get_supported_catalog(home_devices, device)
#    # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_home_dev)

print('Каталог поддерживаемых девайсов: ')
print(result_catalog)




