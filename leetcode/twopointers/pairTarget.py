"""
Determine if two numbers add up to 6

How to think:

Start one pointer at the beginning
Start the other at the end
Check the sum:
If too small → move the left pointer right
If too big → move the right pointer left
"""
def pair_target(lst, target):
    r=len(lst)-1
    l=0
    while l < r:
        op = lst[l]+lst[r]
        if op < target:
            l+=1
        elif op == target:
            return True
        else:
            r-=1
    return False

print(pair_target(lst=[1, 2, 3, 4, 5, 6], target=6))