"""
Running with bunnies
"""

from itertools import combinations, permutations


def solution(times, time_limit):
    answer = []
    num_bunnies = len(times) - 2
    floyd(times) # find shortest path between each pair of nodes
    
    # determine if there is a negative cycle
    for i, row in enumerate(times):
        if row[i] < 0: # negative diagonal indicates negative cycle
            return list(range(num_bunnies))
    
    # check every combination of bunnies
    for num in range(1, num_bunnies + 1):
        for curr in list(combinations(range(num_bunnies), num)):
            if find_path(times, time_limit, curr) and len(curr) > len(answer):
                    answer = curr
                    break
    return answer


# Floyd-Warshall algorithm: to find the minimum weight
# between every pair of nodes; modify 'times' in place
def floyd(times):
    for k in range(len(times)):
        for i in range(len(times)):
            for j in range(len(times)):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]


# Find shortest path that goes through all the nodes in 'bunnies'
# Output True if the path is within 'time_limit'
def find_path(times, time_limit, bunnies):
    for perm in list(permutations(bunnies)):
        perm = [0] + [val + 1 for val in perm] + [-1]
        cost = sum([times[b1][b2] for b1, b2 in zip(perm[:-1], perm[1:])])
        if cost <= time_limit:
            return True
    return False