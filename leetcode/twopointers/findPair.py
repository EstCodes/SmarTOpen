"""
Task:

Find which two positions (indices) add to 10

Thinking:

Same strategy as pairTarget
But now track positions, not just True/False
"""

def find_pair(lst, target):
    r, l = len(lst)-1, 0

    while l < r:
        pro = lst[l]+lst[r]
        if pro == target:
            print(r, l)
        if pro < target:
            l+=1
        else:
            r-=1

find_pair([2, 3, 4, 7, 11], 10)