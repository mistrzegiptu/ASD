def bubelSort(T):
    for i in range(len(T)):
        for j in range(len(T)-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T

print(bubelSort([1,5,7,3,4]))