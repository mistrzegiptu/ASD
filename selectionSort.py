def selectionSort(T):

    for i in range(len(T)):
        min = i
        for j in range(i, len(T)):
            if T[min] > T[j]:
                min = j
        T[i], T[min] = T[min], T[i]
    
    return T

print(selectionSort([3,1,6,4,5,12,9]))