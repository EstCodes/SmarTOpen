def exercise1(nlist: list, searchN: int):
    l = 0
    h = len(nlist) - 1
    m = l + h // 2

    while h <= l:
        if nlist[m] == searchN:
            print("Found")
        else:
            if nlist[m] < searchN:
                # Quiere decir que esta en la parte derecha de la division
                l = m + 1
            else:
                # Quiere decir que esta en la parte izq de la division
                l = m - 1

    print("Found")


exercise1(nlist=[6, 12, 17, 23, 38, 45, 77, 84, 90], searchN=77)