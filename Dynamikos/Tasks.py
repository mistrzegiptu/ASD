def Tasks(T):
    T.sort(key=lambda x: x[1], reversed = True)
    max_dl = 0
    for dl, profit in T:
        max_dl = max(max_dl, dl)
    S = [False for _ in range(max_dl + 1)]
    result = []
    for dl, profit in T:
        for i in range(dl, -1, -1):
            if not S[i]:
                S[i] = True
                result.append((dl, profit))

    return result