def find(parent, i):
  if parent[i] != i:
    parent[i] = find(parent, parent[i])
  return parent[i]

def Kruskal(V, graph):
  result = []
  i = 0
  e = 0

  graph = sorted(graph, key=lambda item: item[2])

  parent = []
  rank = []

  for node in range(V):
    parent.append(node)
    rank.append(0)

  while e < V - 1:

    u, v, w = graph[i]
    i = i + 1

    x = find(parent, u)
    y = find(parent, v)

    if x != y:
      e = e + 1
      result.append([u, v, w])

      if rank[x] < rank[y]:
        parent[x] = y
      elif rank[x] > rank[y]:
        parent[y] = x
      else:
        parent[y] = x
        rank[x] += 1

  minimumCost = 0
  for u, v, weight in result:
    minimumCost += weight
  # print maximum daily amount of Byteland dollars the government can save
  print(sum-minimumCost)


while True:
    sum = 0
    graph = []
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    for i in range(m):
        x, y, w = map(int, input().split())
        sum = sum + w
        graph.append([x, y, w])
    Kruskal(n, graph)