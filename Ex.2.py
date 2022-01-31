"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""


import hashlib
import json


class HashClass:

    def __init__(self, login, password):
        self.login = login
        self.password = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        with open('hash.json', 'r') as file:
            src = json.load(file)

        src[f'{self.login}'] = self.password

        with open('hash.json', 'w') as file:
            json.dump(src, file)

    def access(self, password):
        with open('hash.json', 'r') as file:
            src = json.load(file)

        pass_hash = src[f"{self.login}"]

        if hashlib.sha256(self.login.encode() + password.encode()).hexdigest() == pass_hash:
            print("Добро пожаловать!!!")
        else:
            print("Вы ввели неверный пароль...")


profile1 = HashClass('Oleg123', 'qwerty65')
profile1.access('qwerty645')
