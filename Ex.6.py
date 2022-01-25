"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""


import random


def guess_number(number=random.randint(0, 100), attempt=10):
    if attempt > 0:
        trying = int(input("Угадайте число: "))
        if trying == number:
            print("Поздравляю вы угадали!!!")
        elif trying > number:
            print("Загаданное число меньше...")
            attempt -= 1
            return guess_number(number=number, attempt=attempt)
        elif trying < number:
            print("Загаданное число больше...")
            attempt -= 1
            return guess_number(number=number, attempt=attempt)
    else:
        print(f"Вы проиграли, загаданное число: {number}")


guess_number()
