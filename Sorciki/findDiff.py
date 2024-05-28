def findDiffN2(L, val):
    n = len(L)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if L[i] - L[j] == val:
                return L[i], L[j]

def findDiff(L, val):
    n = len(L)
    i, j = 0, 0

    while j < n and i <= j:
        diff = L[j] - L[i]
        if diff == val:
            return L[j], L[i]
        elif diff > val:
            i += 1
        else:
            j += 1

    return None

print(findDiff([2,5,7,11,21,22], 10))