"""
Gearing up for destruction
"""

def solution(pegs):
    """
    Based on the prompt, we rewrite the problem in terms of equations.
    Let n be the number of pegs. We then have n gears of unknown radii.
    The first n-1 equations are just that the sum of two adjacent radii
        equals the distance between the two adjacent pegs.
    The final equation is that the radius of the first and last gears is 2.
    Define diff to be the difference between adjacent pegs
    """
    diff = [pegs[i + 1] - pegs[i] for i in range(len(pegs) - 1)]
    
    
    """
    We have a system of n linear equations with n unknowns:
        r[i] + r[i + 1] = diff[i] (for i = 0, 1, ..., n - 2)
        r[0] - 2r[n - 1] = 0
    The system has one unique solution because, if written in matrix form, 
        the matrix is square and has full rank.
    Use any method to solve, say row reduce the matrix. It is easy to reduce
        this matrix because each row only has two nonzero entries.
    After solving, the radius of the first peg (r[0]) is:
        answer      if n is odd
        answer / 3  if n is even
    """
    answer = 2 * sum([(1 - 2 * (i % 2)) * curr for i, curr in enumerate(diff)])
    
    
    """
    The answer is only valid if all the radii are greater than 1,
        so we use the below code to check that.
    The solution obtained above tells us that each radius can be written 
        in terms of the previous radius and the current element of diff.
    We compute each radius (stored in var). If a radius is smaller than 1, 
        then no solution exists per the constraints of this problem.
    Note that if n is even, the answer should be divided by 3 at the end.
    """
    if len(pegs) % 2 != 0:
        var = answer
        for curr in diff:
            if var < 1:
                return [-1, -1]
            var = -var + curr
        return [answer, 1]
    else:
        var = answer
        for curr in diff:
            if var < 3:
                return [-1, -1]
            var = -var + 3 * curr
        return [answer, 3] if answer % 3 != 0 else [answer // 3, 1]