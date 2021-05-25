"""
Bomb baby
"""

def solution(x, y):
    steps = 0
    num1 = int(x)
    num2 = int(y)
    
    while num1 >= 1 and num2 >= 1:
        if num1 == 1 or num2 == 1:
            return str(steps + max(num1, num2) - 1)
        if num1 >= num2:
            steps += num1 // num2
            num1 = num1 % num2
        else:
            steps += num2 // num1
            num2 = num2 % num1
        
    return "impossible"