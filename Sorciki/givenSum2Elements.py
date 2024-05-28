def sumTwoElements(T, sum):
    i = 0
    j = len(T)-1
    while i <= j:
        if T[i] + T[j] > sum:
            j -= 1
        elif T[i] + T[j] < sum:
            i += 1
        else:
            return (i, j)
    return (-1, -1)

print(sumTwoElements([1,3,5,8,11,13,16,17], 16))