"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def odd_even(digit: int, even=0, odd=0):
    num = digit % 10
    digit = digit // 10
    parity = num % 2

    if parity == 0:
        even += 1
    else:
        odd += 1

    if digit != 0:
        return odd_even(digit, even, odd)
    else:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")


odd_even(123)