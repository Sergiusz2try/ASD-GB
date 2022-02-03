"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""


from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(digit: int, rev_digit=''):
    num = digit % 10
    digit = digit // 10
    rev_digit += str(num)

    if digit != 0:
        return revers_4(digit, rev_digit)
    else:
        return rev_digit


print(timeit("revers", globals=globals(), number=1000))
print(timeit("revers_2", globals=globals(), number=1000))
print(timeit("revers_3", globals=globals(), number=1000))
print(timeit("revers_4", globals=globals(), number=1000))


'''
1.5799999999999842e-05
1.5699999999993497e-05
1.4699999999999436e-05
1.6700000000001436e-05
Все алгоритмы сработали примерно за одинаковое время, но я считаю что
алгоритм №3 будет быстрее всех т.к. там проходит проход по индексам с конца в начало,
что представляет минимальную сложность соответственно скорость работы будет лучше
'''
