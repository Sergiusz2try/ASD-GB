from memory_profiler import profile


@profile
def reverse(digit: int, rev_digit=''):
    num = digit % 10
    digit = digit // 10
    rev_digit += str(num)

    if digit != 0:
        return reverse(digit, rev_digit)
    else:
        if str(int(rev_digit)) != rev_digit:
            rev_digit += '0'
            return int(rev_digit)
        else:
            return int(rev_digit)


@profile
def reverse_opt(digit):
    nums = list(str(digit))
    result = ''.join(i for i in nums[::-1])
    return result


if __name__ == '__main__':
    reverse(15**65)
    print(reverse_opt(15**65))


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     41.4 MiB     41.4 MiB          77   @profile
     5                                         def reverse(digit: int, rev_digit=''):
     6     41.4 MiB      0.0 MiB          77       num = digit % 10
     7     41.4 MiB      0.0 MiB          77       digit = digit // 10
     8     41.4 MiB      0.0 MiB          77       rev_digit += str(num)
     9                                         
    10     41.4 MiB      0.0 MiB          77       if digit != 0:
    11     41.5 MiB      0.1 MiB          76           return reverse(digit, rev_digit)
    12                                             else:
    13     41.4 MiB      0.0 MiB           1           if str(int(rev_digit)) != rev_digit:
    14                                                     rev_digit += '0'
    15                                                     return int(rev_digit)
    16                                                 else:
    17     41.4 MiB      0.0 MiB           1               return int(rev_digit)


Filename: D:\GB\ASD-GB\task_1\task_1_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    20     41.5 MiB     41.5 MiB           1   @profile
    21                                         def reverse_opt(digit):
    22     41.5 MiB      0.0 MiB           1       nums = list(str(digit))
    23     41.5 MiB      0.0 MiB         157       result = ''.join(i for i in nums[::-1])
    24     41.5 MiB      0.0 MiB           1       return result

Второе решение вышло гораздо оптимизированное как по использованию памяти так и по скорости благодаря использованию
lc 
'''
