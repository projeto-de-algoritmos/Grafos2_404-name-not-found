#include <iostream>

#define INFINITY 9999999

typedef struct Graph
{
    int nodes;
    int edges;
    int roads[501][501]; // Adjacency matrix
}Graph;

Graph graph;

int dijkstra(int origin_city, int destination_city) {
    int min_cost;
    int next;
    int cost[graph.nodes+1];
    bool visited[graph.nodes+1];

    for(int i = 1; i <= graph.nodes; i++) {
        visited[i] = false;
        cost[i] = INFINITY;
    }

    cost[origin_city] = 0;

    for(int i = 1; i <= graph.nodes; i++) {
        min_cost = INFINITY;

        if(visited[destination_city]) 
            break;

        for(int j = 1; j <= graph.nodes; j++) {
            if(!visited[j] && min_cost > cost[j]) {
                min_cost = cost[j];
                next = j;
            }
        }

        if(min_cost == INFINITY)
            break;

        visited[next] = true;

        for(int j = 1; j <= graph.nodes; j++) {
            if(cost[j] > min_cost + graph.roads[next][j]) {
                cost[j] = min_cost + graph.roads[next][j];
            }
        }
    }
    return cost[destination_city];
}

int main() {
    int qnt_cities;
    int qnt_agreements;

    while(std::cin >> qnt_cities >> qnt_agreements) {
        
        if(qnt_agreements == 0 && qnt_cities == 0) 
            break;

        int city_x;
        int city_y;
        int hours;
        int queries;

        graph.nodes = qnt_cities;
        graph.edges = qnt_agreements;
        for(int i=1; i <= qnt_cities; i++) {
            for(int j=1; j <= qnt_cities; j++) {
                graph.roads[i][j] = INFINITY;
            }
        }

        for(int i = 0; i < qnt_agreements; i++) {
            std::cin >> city_x >> city_y >> hours;

            // Insert information in graph...
            graph.roads[city_x][city_y] = hours;

            // Same country
            if(graph.roads[city_y][city_x] != INFINITY) {
                graph.roads[city_x][city_y] = 0;
                graph.roads[city_y][city_x] = 0;
            }
        }

        std::cin >> queries;

        for(int i = 0; i < queries; i++) {
            std::cin >> city_x >> city_y;
            int cost_in_hours = dijkstra(city_x, city_y);

            if(cost_in_hours == INFINITY) {
                std::cout << "Nao e possivel entregar a carta" << std::endl;
            }
            else {
                std::cout << cost_in_hours << std::endl;
            }
        }
        std::cout << std::endl;
    }

    return 0;
}