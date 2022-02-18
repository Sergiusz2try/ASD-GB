"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""


import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple('Node', ["left", "right"])):
    def walk(self, code, acc):

        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple('Leaf', ["char"])):
    def walk(self, code, acc):

        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(freq, _count, root)] = h
        root.walk(code, " ")
    return code


if __name__ == '__main__':
    string = input()
    code = huffman_encode(string)
    encoded = "".join(code[ch] for ch in string)
    for ch in sorted(code):
        print(f"{ch}: {code[ch]}")
    print(encoded)
