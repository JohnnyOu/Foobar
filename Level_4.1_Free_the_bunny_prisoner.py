"""
Free the bunny prisoners
"""

from itertools import combinations

def solution(num_buns, num_required):
    answer = [[] for _ in range(num_buns)]
    
    # distribute each key to this many people
    distr = num_buns - num_required + 1
    
    for key, comb in enumerate(combinations(range(num_buns), distr)):
        for i in comb:
            answer[i].append(key)
    
    return answer