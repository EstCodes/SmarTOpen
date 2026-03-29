"""
Task:

Remove duplicates so the array becomes:
[1, 2, 3, _, _]

Thinking:

Use:
One pointer = last unique value
One pointer = scanning forward
Only move the first pointer when you find a new value
"""

# j = fast pointer
# i = slow pointer
def rmv_dups(lst):
    i = 0

    for j in range(1, len(lst)):
        if lst[j] != lst[i]:
            i += 1
            lst[i] = lst[j]

    print(lst[:i + 1])

rmv_dups([1, 1, 2, 2, 3])