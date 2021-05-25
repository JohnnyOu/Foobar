"""
Hey I already did that
"""

def solution(n, b):
    curr = list(n)
    iterations = [] # stores all encountered IDs
    while True:
        y = sorted(curr)
        curr = subtract(list(reversed(y)), y, b)
        try:
            return len(iterations) - iterations.index(curr)
        except:
            iterations.append(curr)


# performs x - y (in the corresponding base)
def subtract(x, y, base):
    answer = []
    carry = 0
    for top, bot in zip(reversed(x), reversed(y)):
        curr = int(top) - int(bot) - carry
        answer.insert(0, curr % base)
        carry = 1 if curr < 0 else 0
    return answer