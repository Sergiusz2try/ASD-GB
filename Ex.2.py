"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def min_val1(nums: list):
    min_val = 0
    for i in nums:
        for j in nums:
            if i > j:
                break
            else:
                min_val = i

    return min_val


def min_val2(nums: list):
    min_val = nums[0]
    for i in nums[0:]:
        if i < min_val:
            min_val = i

    return min_val


values = [9, 4, 20, 15, 7, 11, 1]
print(min_val1(values))
print(min_val2(values))
