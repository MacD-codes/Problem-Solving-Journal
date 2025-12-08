'''
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
'''

# SOLUTION
def invert(lst):
    l1=[]
    for i in lst:
        result=i*(-1)
        l1.append(result)
    return l1
    pass