# 2) Закодируйте любую строку по алгоритму Хаффмана.
# Смотрел разбор задачи здесь: https://stepik.org/lesson/13245/step/3?unit=3430,
# В задаче разобрался, но понимаю, что "отлично" - не для меня, не буду возражать против любой из оценок

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def step(self, code, acc):
        self.left.step(code, acc + '0')
        self.right.step(code, acc + '1')


class Leaf(namedtuple('Leaf', ['ch'])):
    def step(self, code, acc):
        code[self.ch] = acc or '0'


def huff_enc(string):
    h = []
    for char, freq in Counter(string).items():
        h.append((freq, len(h), Leaf(char)))
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
        root.step(code, '')
    return code


def main():
    string = input('Введите слово: ')
    code = huff_enc(string)
    encoded = ' '.join(code[ch] for ch in string)
    print(f'Ваша строка теперь выглядит так: {encoded}')

main()