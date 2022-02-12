from memory_profiler import profile
from numpy import array


@profile
def odd_nums(n=100000):
    lst = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            lst.append(i)
    return lst


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     40.5 MiB     40.5 MiB           1   @profile
     5                                         def odd_nums(n=100000):
     6     40.5 MiB      0.0 MiB           1       lst = []
     7     43.1 MiB      0.0 MiB      100001       for i in range(1, n + 1):
     8     43.1 MiB      1.6 MiB      100000           if i % 2 != 0:
     9     43.1 MiB      1.0 MiB       50000               lst.append(i)
    10     43.1 MiB      0.0 MiB           1       return lst
'''


@profile
def odd_nums_opt(n=100000):
    lst = filter(lambda x: x % 2 == 0, array(range(n)))
    return lst


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    27     49.9 MiB     49.9 MiB           1   @profile
    28                                         def odd_nums_opt(n=100000):
    29     50.6 MiB      0.7 MiB           1       lst = filter(lambda x: x % 2 == 0, array(range(n)))
    30     50.6 MiB      0.0 MiB           1       return lst
'''


if __name__ == '__main__':
    odd_nums()
    odd_nums_opt()


'''
С помощью функции filter и array мы смогли оптимизировать код и уменьшить выделяемую память
'''
