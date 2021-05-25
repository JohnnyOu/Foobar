"""
Disorderly escape
"""

from fractions import gcd
from collections import Counter
from functools import reduce


def solution(w, h, s):
    fact = factorial(max(w, h) + 1) # store all factorials in list
    mult = lambda x, y: x * y # for reduce()
    answer = 0
    for row in [Counter(part) for part in partition(h)]:
        for col in [Counter(part) for part in partition(w)]:
            power = sum([sum([gcd(r, c) * row[r] * col[c] for c in col]) for r in row])
            answer += fact[w] * fact[h] * s ** power \
                // reduce(mult, [r ** row[r] * fact[row[r]] for r in row]) \
                // reduce(mult, [c ** col[c] * fact[col[c]] for c in col])
    return str(answer // fact[w] // fact[h])


def factorial(num):
    answer = [1]
    for i in range(1, num + 1):
        answer.append(i * answer[-1])
    return answer


def partition(num):
    answer = set()
    answer.add((num, ))
    for x in range(1, num):
        for y in partition(num - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer