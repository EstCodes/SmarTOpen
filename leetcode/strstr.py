def strStr(haystack: str, needle: str) -> int:
    def badCharacter(string, size):
        size = 256
        badC = ...
        for i in range(size):
            badC = [ord(string[i])] = i
        return badC


    n = len(needle)
    h = len(haystack)
    if n == 0 or h == 0:
        return 0
    indexN = n - 1
    while indexN < h:
        indexN2 = n - 1
        # R to L
        """
        While indexN2 is greater or equal to 0 and also... if the element inside hystack, which can be identified as the index
        index inside the haystack = indexN - (lenght of needle - 1 - indexN2)
        also... if the result of the index inside the haystack is greater than h then use 0
        otherwise, everything is good. 
        """
        while indexN2 >= 0 and needle[indexN2] == haystack[indexN - (n - 1 - indexN2) if indexN - (n - 1 - indexN2) < h else 0]:
            indexN2 -= 1
        if indexN2 < 0:
            return indexN - n + 1
        else:
            ...

strStr(haystack="sadbutsad", needle="sad")