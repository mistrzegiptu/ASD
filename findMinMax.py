def findMinMax(T):
    minE = T[len(T)-1]
    maxE = T[len(T)-1]
    for i in range(0, len(T)-1, 2):
        if T[i] > T[i+1]:
            if T[i] > maxE:
                maxE = T[i]
            if T[i+1] < minE:
                minE = T[i+1]
        else:
            if T[i+1] > maxE:
                maxE = T[i+1]
            if T[i] < minE:
                minE = T[i]
    return (minE, maxE)

print(findMinMax([1,3,2,8,7,6]))