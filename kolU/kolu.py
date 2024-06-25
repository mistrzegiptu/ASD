from kolutesty import runtests
from _collections import defaultdict, deque
def projects(n, L):
  G = defaultdict(list)
  in_degree = [0] * n
  for (p, q) in L:
    G[q].append(p)
    in_degree[p] += 1

  queue = deque([i for i in range(n) if in_degree[i] == 0])
  topo_order = []

  while queue:
    node = queue.popleft()
    topo_order.append(node)
    for neighbor in G[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)

  max_depth = 0
  depths = [0] * n

  for node in topo_order:
    for neighbor in G[node]:
      if depths[neighbor] < depths[node] + 1:
        depths[neighbor] = depths[node] + 1
        max_depth = max(max_depth, depths[neighbor])

  return max_depth + 1  # Add 1 to account for the initial node

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
