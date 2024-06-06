def zad4(A): # O(n log n)
  from queue import PriorityQueue

  q = PriorityQueue()
  q.put(-A[0])
  ans = r = 0
  while r < len(A) - 1:
    energy = -q.get()
    ans += 1
    while r < len(A) - 1 and energy > 0:
      r += 1
      energy -= 1
      q.put(-A[r])

  return ans

A = [3, 9, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(zad4(A))