from decimal import Decimal
from datetime import datetime, date, timedelta

DATE_FORMAT = '%Y-%m-%d'
goods = {}


def add(items, title, amount, expiration_date=None):
    if expiration_date:  # check if expiration_date not None
        #  convert string into datetime format
        date = datetime.date(datetime.strptime(expiration_date, DATE_FORMAT))
    else:
        date = None
    #  make a dictionari with goods parametrs
    goods_parametrs = {'amount': amount, 'expiration_date': date}
    if title in items.keys():  # check if good name in dict
        #print('yes')
        items[title].append(goods_parametrs)  # upgrade if is
    else:
        items.update({title: [goods_parametrs]})  # make new if not


def add_by_note(items, note):
    new_note = note.split()
    good_name = ''
    amount_index = 0
#    print(new_note)
    try:
        # check if last one value of the list is date
        bool(datetime.strptime(new_note[-1], DATE_FORMAT))  # return True/False
        date = new_note[-1]
        # pop data from list to make easer search anather goods parametrs
        date_value = new_note.pop(new_note.index(date))
#        print(date)
    except ValueError:
        date_value = None  # return None if the last list element not date
    # check wich one element of the list is number
    for number in range(0, 9):
        for note in new_note:
            if str(number) in note:
                # compear numbers from range with items in list
                if amount_index != new_note.index(note):
                    # save index into verable if value != index
                    amount_index = new_note.index(note)
                elif amount_index == new_note.index(note):
                    # just pass if index already in verable to evoid repitition
                    continue
    # collect strings from list to add into good_name
    for word in new_note[:amount_index]:
        good_name += " " + word
    good_amount = Decimal(new_note[amount_index])  # concert value to  Decimal
    #print(items, good_name, good_amount, date_value)
    if date_value:
        add(items, good_name.strip(), good_amount, date_value)
    else:
        add(items, good_name.strip(), good_amount,)


def find(items, needle):
    list_of_goods = []
    for key in items.keys():
        if needle.lower() in key.lower():
            list_of_goods.append(key)
    return list_of_goods


def amount(items, needle):
    sum_of_amount = Decimal('0')
    goods = find(items, needle)
    for good in goods:
        print(good)
        for products, parametrs in items.items():
            if good == products:
                #print(parmetrs)
                for parametr in parametrs:
                    quantity = parametr['amount']  # get amount of good
                    #print(quantity)
                    sum_of_amount += quantity
                    #sum_of_amount += items[item.index(good)]['amount']
    return sum_of_amount


def expire(items, in_advance_days=0):
    bad_products = []
    today = date.today()
    future_date = today + timedelta(days=in_advance_days)
    for products, parametrs in items.items():
        for parametr in parametrs:
            #print(parametr)
            if parametr['expiration_date'] is not None and parametr['expiration_date'] <= future_date:
                bad_product = (products, amount(items, products))
                bad_products.append(bad_product)
                if len(bad_product) > 1:
                    break
        #        #print('bad')
        #    #else:
            #    print('good')
            #print(good)
    #print(today)
    #print(future_date)
    #print(bad_products)
    return bad_products


#add(goods, 'Яйца', Decimal('10'), '2025-9-30')
#add(goods, 'Яйца', Decimal('3'), '2023-10-15')
add(goods, 'Вода', Decimal('1.5'), )
#add_by_note(goods, 'Яйца гусиные 40 2023-07-15')
add_by_note(goods, 'Фабрика №2: яйца 2 2023-11-15')
add_by_note(goods, 'Фабрика №2: яйца 3 2023-11-17')
add_by_note(goods, 'Яйца Фабрики №1 1 2025-11-15')
#add_by_note(goods, 'Вода 1.5')
#print(find(goods, 'йц'))
#print(find(goods, 'ВОдА'))
#print(amount(goods, 'Фабрик'))
print(expire(goods, in_advance_days=0))
#print(goods)
# goods = {
#     'Пельмени Универсальные': [
#         {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 9, 30)}
#         {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 10, 28)}
#     ]
# } 
#{'Фабрика №2: яйца': [{'amount': Decimal('2'), 'expiration_date': None},
#                      {'amount': Decimal('3'),
#                       'expiration_date': datetime.date(2024, 9, 17)}],
# 'Яйца Фабрики №1': [{'amount': Decimal('1'),
#                      'expiration_date': datetime.date(2024, 9, 19)}],
# 'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]}
'''
add_by_note()
-Разделить строку на части по пробелам с помощью str.split.
-Определить, является ли последняя часть строки датой.
-Ту часть строки, где указано количество продукта, конвертировать в число типа Decimal
-Оставшуюся часть строки объединить, чтобы получить название продукта: если название состояло из нескольких слов — функция str.split разобъёт его на части.
-Вызвать функцию add(), передав в неё получившиеся данные — название, количество и срок хранения
'''
