def Points(X):
  n = len(X)
  X.sort()

  count = 1
  start = 0

  for i in range(1, n):
    if X[start] <= X[i] <= X[start] + 1:
      continue
    else:
      start = i
      count += 1

  return count


X = [-.5, 0, .25, .5, 1.6, 1.8, 2.6]
print(Points(X))  # 2

X = [-.51, -.5, 0, .25, .5, 1.6, 1.8, 2.6]
print(Points(X))  # 3

X = [-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]
print(Points(X))  # 3
