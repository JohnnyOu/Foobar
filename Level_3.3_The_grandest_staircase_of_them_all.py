"""
The grandest staircase of them all
"""

import numpy.polynomial.polynomial as p

def solution(n):
    term = [1, 1]
    prod = [1]
    for _ in range(n):
        prod = p.polymul(prod, term)
        term.insert(1, 0)
    return int(prod[n] - 1)