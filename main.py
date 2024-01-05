

# def my_name(name):  # функція
#     print(name)


# my_name('Serhii')


# def sum_nums(a, b):
#     sum = a+b
#     return sum


# def change_person_age(person):  # функція не змінює зовнішній об'єкт
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     return person_copy


# person_one = {
#     'name': 'serhii',
#     'age': 36
# }

# new_person = change_person_age(person_one)

# print(new_person)
# print(person_one)


# print(sum_nums(5,2))


# my_disk['brand'] = 'Samsung'
# my_disk['price'] = 80

# print(my_disk)

# my_dict ={}

# key_1 = input('Please enter key1: ')
# value_1 = input('Please enter value1: ')

# my_dict[key_1] = value_1

# print(my_dict)

# Кортежі(tuple)

# my_nums = (10, 20, 30)
# print(my_nums.count(10))
# print(my_nums.index(10))

# my_list = list(my_nums)

# my_list.append(40)
# print(my_list)

# my_nums = tuple(my_list)

# print(my_nums)

# Набори(set)


# my_set = {1, 2, 3, 4}

# my_set.add(5)

# another_set = { 3, 4, 5, 6}

# new_set = my_set.intersection(another_set)

# list_set = list(new_set)
# print(list_set)

# Діапазони(range)

# my_range = range(2,20,2)

# for n in my_range:
#     print(n)

# Функція(zip)


# product = ['laptop', 'pc', 'printer']

# quantity = [1010, 20, 30]


# product_quantity = zip(product, quantity)

# product_quantity_list = list(product_quantity)

# print(product_quantity_list)

# product_quantity_copy = product_quantity_list.copy()


# product_quantity_dict = dict(product_quantity_copy)
# print(product_quantity_dict)


# def merge_list_to_dict(list_1, list_2):
#     result = dict(zip(list_1, list_2))
#     return result


# result_def = merge_list_to_dict(product, quantity)
# print(result_def)


# def get_posts_info(name, age):  # Функція з f(шаблонною строкою)
#     info = f"Hello {name} you are {age}"
#     return info


# print(get_posts_info("Serhii", 25))


# Об'єднання параметрів функції в словник
# def update_car_info(**car):
#     car['is available'] = True
#     return car


# print(update_car_info(brand='BVW', price=1000))


# def my_name(name):       #рекурсія
#     print(name)
#     my_name('Serhii')

# my_name('Serhii')


# dict_one = {"a": 1}
# dict_two = {"a": 1}

# dict_one == dict_two and print('dictionaries are equal')

# Розпаковка, об'єднання словників
# button_red  = {
#     'color': 'red',
#     'type' : 'button'
# }

# button_black  = {
#     'color': 'black',
#     'width': 200
# }

# button_grey = {
#    'color': 'grey',
#     'heigth': 300
# }


# button = {**button_black,
#           **button_red,
#           **button_grey}


# del button["color"]
# print(button)

# Замикання + lambda функція

# def greeting(greet):
#     return lambda name: f"{greet}, {name}"

# morning_greeting = greeting("Good Morning")

# print(morning_greeting("Serhii"))

# evening_greeting = greeting("Good Evening")

# print(evening_greeting('Serhii'))

# goodbuy = greeting("Goodbyu")

# print(goodbuy('Serhii'))


# Замикання без лямбда функції

# def greeting(greet):
#     def info(name):
#         return f"{greet}, {name}"
#     return info


# morning_greeting = greeting("Good Morning")

# print(morning_greeting("Serhii"))

# evening_greeting = greeting("Good Evening")

# print(evening_greeting('Serhii'))

# def count(x):
#     def number(y):
#         return x+y
#     return number

# count_number = count(10)
# print(count_number(5))


# Умовні інструкції

# my_number = 0

# if my_number > 0:
#     print('My number is positive')
# elif my_number < 0:
#      print('My number is negative')
# else:
#     print('My number is zero')


# def my_nums(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "a or b not even"
#     if a >= b:
#         return f"{a} more than {b}"


# print(my_nums(10, 2.5))


# def route_info (route):

#     if ('distance' in route) and (type(route["distance"]) is int):
#         return f"Distance to your destination is {route['distance']}"

#     elif ( route.get('speed') and route.get('time')) and (type(route['speed'] and route['time']) == int):
#         return f"Distance to your destination is {route['speed'] * route['time']}"

#     else: return "no"


# print(route_info({"distance":1}))


# def route_info(dict):
#     if ("distance" in dict) and (type(dict['distance'] is int)):
#         return f"Distance to your destination is {dict['distance']}"

#     elif ((dict.get('time') and 'speed' in dict)
#           and type(dict["time"] and (dict["speed"]) == int)):
#         return f"Distance to your destination is {dict['time'] * dict['speed']}"
#     else:
#         return 'No distance info'


# print(route_info({'distance': 20}))

# print(route_info({'time': 21, 'speed': 2}))

# print(route_info({'timed': 20}))


# Тернарний оператор

# string = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

# res = "String is long" if len(string) > 79 else "String is not long"
# print(len(string))
# print(res)


# Цикл for in

# my_list = [1, 2, 3]

# for el in my_list:
#     print(el)
#     print(type(el))

# my_dict = {"a":1, 'b': 2, 'c':3}

# for key in my_dict:
#     print(key)
#     print(my_dict[key])

# for item in my_dict.items():
#     key, value = item
#     print(item)


# for num in range(100):
#     print(num)

# list = [1, 'Hello', 5, True, 3.5, False]
# def checking_list(list, type_elem):
#     checked_list = []
#     for elem in list:
#         if type(elem) == type_elem:
#             checked_list.append(elem)

#     return checked_list

# print(checking_list(list, int))
# print(checking_list(list, bool))


# Цикл while

# i = 10

# while i < 50:
#     i+=10
#     print(i)


# while True:
#     num = int(input('Guess the number from 1 to 5:'))
#     if num !=random_num:
#         print('Try again')
#         continue
#     print('Great!')
#     break


# while True:
#     num_1 = int(input('Enter nunber one: '))
#     num_2 = int(input('Enter nunber two: '))
#     (result) = num_1/num_2
#     print(int(result))
#     answer = input("Yes or No: ")
#     if answer == "No":
#         break

# list = [1, 2, 3, -5, -8, -9]
# pos_nums = []
# for num in list:

#     if num < 0:
#         pos_nums.append(num)
# print(pos_nums)


# Some practice


# def convert(miles):
#     kilometers = miles * 1.61
#     return f"{miles} miles it`s a {kilometers} kilometers"


# print(convert(1))


# def is_even(number):
#     if number % 2 == 0:
#        return ("number is even")
#     else:
#        return ("number is not even")

# print(is_even(3))


# list = [1, 2, 3, 4, 5, -2, -1, "stop"]

# # i = 0

# # while list[i] != -2:
# #     print(i)
# #     i+=1

# for i in list:
#     if i == "stop":
#         break
#     print(i)

# my_list = [ 1, 83,75, 34,855, 2, 3, 4 ]

# sorted_list = sorted(my_list, reverse = True)

# my_list.sort(reverse = True)


# dict  = { 'a': 1, 'b':2}


# del dict['a']

# dict['a'] = 4

# print(dict)

# Округлення функція round
# amount = float(input("Enter amount: "))
# price = float(input("Enter price: "))

# total = f"Your price {round(amount * price, 2)} uah"

# print(total)


# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# even_nums = nums[3:8:4]

# print(even_nums)


# nums = {'one': 1,
#         "two": 2}

# for key, value in nums.items():
#     print(key, value)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]


# def even_number(list):
#     count_even = 0
#     count_odd = 0
#     for even in list:
#         if even % 2 == 0:
#             count_even += 1
#         if even % 2 != 0:
#             count_odd += 1
#     print(count_even)
#     print(count_odd)


# even_number(list)

# # задача не перетворення літери на юнікод

# def letter_to_codes(string):

#     dict = {}

#     for letter in string:
#         if letter not in dict:
#             dict[letter] = ord(letter)

#     return dict

# print(letter_to_codes('Hello'))

# Задача підрахунок літер у строці та додавання результату у словник

# str = "hello worldfsdfdsfsfsdfwf"

# dict = {}

# for char in str:
    
#    count = dict.get(char, 0)
#    count+=1
#    dict[char] = count
        
# print(dict)

from datetime import datetime

# current_time = datetime.now()

# print(current_time)

holy_evening = datetime(year=2024, month=1, day=6, hour=16)
current_time = datetime.now()

until_holy_evening = holy_evening - current_time
print(f"'До Святвечора залишилось: {until_holy_evening}'") 
now = datetime.now()


str = 'Hello fron another comp'
str2 = 'Hello from another comp'
str3 = 'Hello from another laptop'
str4 = 'Hello from another laptop again'