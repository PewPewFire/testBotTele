token = 'your token'

dictCity = {
    "Лондон":"file_id",
    "Москва":"file_id",
    "Рим":'file_id',
    "Париж":"file_id"
    }

# Пользователь вводит имя, фамилия, возраст. Создайте словарь user и запишите данные пользователя в него.
# name = input()
# lastname = input()
# users = dict(name=name, lastname=lastname)
# print(users)

# a = int(input('Введите кол-во фруктов: '))
# fruits = dict()
# for i in range(a):
#     fruit = input()
#     count = int(input())
#     fruits.get(fruit, count)
# print(fruits)

# fruits = dict()
# fruits['Апельсин'] = 2
# fruits["Ананас"] = 3
# print(fruits)
# взять ключ и значения
# нужно создать список, где один правильный ответ и три неправильных


# countFriends = int(input('Введите кол-во друзей: '))
#
# friends = [{'Вася': 20}, {'Петя': 15}]
# for i in range(countFriends):
#     name = input('Введите имя: ')
#     age = int(input("Введите возраст: "))
#     dictFriends = {}
#     dictFriends[name] = age
#     friends.append(dictFriends)
# print(friends)
# junFr = 999
# for q in friends:
#     if junFr > list(q.values())[0]:
#         junFr = list(q.values())[0]

# Из городов выбрать один из вместе со значением.(случаный)
# Сделать список из 4 вариантов ответа. Один из которых правильный.
# Перемешать


cityList = list(dictCity.keys())
print(cityList)

import random
cityQues = random.choice(cityList)
photo = dictCity[cityQues]
random.shuffle(cityList)
print(cityList)
