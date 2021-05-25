"""
Doomsday fuel
"""

from fractions import Fraction, gcd


def solution(m):
    for i, row in enumerate(m):
        if sum(row) == 1 and row[i] == 1:
            m[i][i] = 0
    
    # note the nonzero and zero rows
    nonzero = []
    zero = []
    for i, row in enumerate(m):
        if sum(row) != 0: 
            nonzero.append(i)
        else:
            zero.append(i)
    
    # if s0 goes nowhere
    if sum(m[0]) == 0 or len(m) == 1:
        return [1] + [0 for _ in range(len(m) - len(nonzero) - 1)] + [1]
    
    # swap rows and columns to shift 0's down
    indices = nonzero + zero
    new_m = [[0 for _ in m] for _ in m]
    for i in range(len(new_m)):
        for j in range(len(new_m)):
            new_m[i][j] = m[indices[i]][indices[j]]
    m = new_m
    
    # convert m to be Markov-compatible
    markov = []
    for i, row in enumerate(m):
        curr_sum = sum(row)
        if curr_sum != 0:
            markov.append([Fraction(val, curr_sum) for val in row])
    
    # find the inverse of fundamental matrix: I - Q
    fund = [[-val for val in row[:len(markov)]] for row in markov]
    for i, row in enumerate(fund):
        row[i] += 1
    
    # solve for (I - Q)x = R
    # R is stored in column-major order for faster solving
    R = [[row[j] for row in markov] for j in range(len(fund[0]), len(markov[0]))]
    answer = [gauss_elim(fund, rhs) for rhs in R]
    
    # first row is the probability starting at s0
    answer = [val[0] for val in answer]
    
    # find least common denominator
    lcd = 1
    for val in answer:
        lcd = lcd * val.denominator // gcd(lcd, val.denominator)
    
    # find corresponding numerators
    return [val.numerator * (lcd // val.denominator) for val in answer] + [lcd]


# This function solves the linear system of equations [matrix]x = [value]
# using Gaussian elimination with partial pivots
#
# @param  matrix - square matrix of rational numbers
# @param  value - vector of the same dim as matrix; the right hand side of equation
# @return the solution to [matrix]x = [value]
def gauss_elim(matrix, value):
    # augment the matrix
    aug = [lhs + [rhs] for lhs, rhs in zip(matrix, value)]
    
    for j in range(len(aug) - 1):
        # find largest pivot below
        col = [aug[i][j] for i in range(j, len(matrix))]
        m_index = col.index(max(col)) + j
        
        # singular matrix
        if abs(aug[m_index][j]) == 0:
            raise Exception("Matrix is singular")
        
        # swap row with the maximum pivot
        aug[j], aug[m_index] = aug[m_index], aug[j]
        
        # do elementary row operation, then store multiplier 
        for i in range(j + 1, len(aug)):
            m = aug[i][j] / aug[j][j]
            for k in range(j + 1, len(aug[0])):
                aug[i][k] -= m * aug[j][k]
            aug[i][j] = m
    
    # Check if last row is 0; only checking the last term will suffice
    if abs(aug[len(aug) - 1][len(aug) - 1]) == 0:
        raise Exception("Matrix is singular")
    
    # Backward substitution
    result = [0 for i in range(len(value))]
    for i in range(len(aug) - 1, -1, -1):
        lst = [aug[i][j] * result[j] for j in range(i + 1, len(aug))]
        result[i] = (aug[i][len(aug[i]) - 1] - sum(lst)) / aug[i][i]
                
    return result