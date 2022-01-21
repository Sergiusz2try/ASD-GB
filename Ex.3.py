"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def top_profit1(companies: dict):
    top_comp = {}                                               # O(1)
    i = 3                                                       # O(1)
    while i != 0:                                               # O(N)
        top = max(companies.items(), key=lambda k_v: k_v[1])    # O(N)
        top_comp[top[0]] = top[1]                               # O(1)
        companies.pop(top[0])                                   # O(1)
        i -= 1                                                  # O(1)

    return top_comp                                             # O(1)
# Сложность: O(N^2)


def top_profit2(companies: dict):
    sorted_values = sorted(companies.values())  # O(N log N)
    sorted_dict = {}                            # O(1)

    for i in sorted_values:                     # O(N)
        for k in companies.keys():              # O(N)
            if companies[k] == i:               # O(1)
                sorted_dict[k] = companies[k]   # O(1)
                break

    top_comps = {}                                                  # O(1)
    for key, value in reversed(list(sorted_dict.items())[-3:]):     # O(N)
        top_comps[key] = value                                      # O(1)

    return top_comps                                                # O(1)
# Сложность: O(N^2)


profits = {
                "iSoft": 13600,
                "Microsoft": 56500,
                "MD": 45700,
                "KFC": 55100,
                "Apple": 76800,
                "AvtoClub": 32100,
                "Motorola": 22550
          }
