def findFirstError(T):
    l = T[0]
    r = T[len(T)-1]
    mid = (l+r) // 2

    while l < mid:
        mid = (l+r) // 2
        if T[mid] == mid:
            l = mid
        else:
            r = mid
    
    if T[mid+1] - T[mid] > 1:
        return T[mid] + 1
        
    return -1

print(findFirstError([1,2,3,4,5,6,7,8,9]))