def insertionSort(T):

    for i in range(1,len(T)):
        for j in range(i, 0, -1):
            if T[j] < T[j-1]:
                T[j], T[j-1] = T[j-1], T[j]
            else:
                break
    return T

print(insertionSort([3,4,6,1,12,7]))