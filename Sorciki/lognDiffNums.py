def sortLogN(T):
    n = len(T)
    A = [0 for _ in range(ceil(log2(n)))]
    counters = [0 for _ in range(len(A))]
    for x in T:
        counters[binsearch(x)] += 1