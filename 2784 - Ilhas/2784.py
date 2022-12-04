INFINITY = 9999999

class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes + 1
        self.edges = edges
        self.matrix = [[INFINITY for column in range(nodes+1)] 
                        for row in range(nodes+1)]


def dijkstra(graph, origin_island):

    cost = [INFINITY for _ in range(graph.nodes)]
    origin = [0 for _ in range(graph.nodes)]
    visited = [False for _ in range(graph.nodes)]

    origin[origin_island] = origin_island
    cost[origin_island] = 0

    min_cost = 0

    while min_cost != INFINITY:
        min_cost = INFINITY

        for i in range(1, graph.nodes):
            if not visited[i] and min_cost > cost[i]:
                next = i
                min_cost = cost[i]

        if min_cost == INFINITY:
            break

        visited[next] = origin[next]

        for i in range(1, graph.nodes):
            if cost[i] > cost[next] + graph.matrix[next][i]:
                cost[i] =  cost[next] + graph.matrix[next][i]
                origin[i] = next

    return cost


def main():
    line = input().split()
    qnt_island = int(line[0])
    qnt_cables = int(line[1])

    graph = Graph(qnt_island, qnt_cables)

    for _ in range(qnt_cables):
        line = input().split()
        island_u = int(line[0])
        island_v = int(line[1])
        ping = int(line[2])

        graph.matrix[island_u][island_v] = ping
        graph.matrix[island_v][island_u] = ping
        
    server = int(input())

    cost = []
    less_distant = INFINITY
    more_distant = 0
    cost = dijkstra(graph, server)

    for island in range(1, len(cost)):
        if island != server:
            less_distant = min(less_distant, cost[island])
            more_distant = max(more_distant, cost[island])

    print(more_distant - less_distant)

main()
