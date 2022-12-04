def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def print_result(previous_nodes, shortest_path, start_node, target_node, dist_max, num_bota):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)

    total = []


    # make the inverso of the code above
    tesss = path
    for i in reversed(range(len(tesss)-1)):
      summ = 0
      for j in reversed(range(len(tesss)-1)):
        summ = summ + shortest_path[tesss[j]] - shortest_path[tesss[j+1]]

        if (tesss[j] in castle and tesss[j+1] in castle) or (tesss[j] == 'v1' and tesss[j+1] in castle):
          total.append(summ)
          break

        if summ >= dist_max or (tesss[j] in castle and tesss[j+1] not in castle):


          if summ != dist_max:
            summ = summ - shortest_path[tesss[j]] + shortest_path[tesss[j+1]]

            if tesss[j] in castle and tesss[j+1] not in castle:
              summ = summ + shortest_path[tesss[j]] - shortest_path[tesss[j+1]]
              total.append(summ)
              break
          
          total.append(summ)
          summ = 0
          break
        
      tesss.pop(i+1)
    sort_total = sorted(total, reverse=True)
    if sort_total[0] > dist_max:
      sort_total.pop(0)
    # print(sort_total)
    total = 0
    for i in range(num_bota):
      total = total + sort_total[i]

    print("{}".format(shortest_path[target_node]-(total)))

castle = []
nodes = []

tam = int(input())
for j in range(tam):
  nodes = []
  castle = []
  A, B, M, L, K = map(int, input().split())
  # print(A, B, M, L, K)

  for i in range(A+B):
      if i >= A:
          castle.append('c'+str(i+1))
          nodes.append('c'+str(i+1))
      else:
          nodes.append('v'+str(i+1))



  init_graph = {}
  for node in nodes:
      init_graph[node] = {}
      

  for i in range(M):
      u, v, peso = map(int, input().split())

      #transform to init_graph format
      if 'c'+str(u) in castle:
          u_ = 'c'+str(u)
      else:
          u_ = 'v'+str(u)
      if 'c'+str(v) in castle:
          v_ = 'c'+str(v)
      else:
          v_ = 'v'+str(v)

      # print(u, v, peso)
      init_graph[u_][v_] = peso


  graph = Graph(nodes, init_graph)

  previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=nodes[-1::][0])
  print_result(previous_nodes, shortest_path, start_node=nodes[-1::][0], target_node=nodes[0::][0], dist_max=L, num_bota=K)
