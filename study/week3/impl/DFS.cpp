#include <iostream>
#include <stack>
#define INCLUDE_ADJACENTMATRIXGRAPH
#include "adjacent_matrix_graph.cpp"

using namespace std;

void DFS(AdjacentMatrixGraph& graph, int root)
{
    const int vertices = graph.getSize();
    int v, edge;
    bool* visited = new bool[vertices];
    stack<int> s;

    s.push(root);

    while (!s.empty())
    {
        v = s.top();
        s.pop();
        printf("%c ", graph.getVertex(v));
        if (!visited[v])
        {
            visited[v] = true;
            for (int i = 0; i < vertices; i++)
            {
                edge = graph.getEdge(v, i);
                if (edge > 0 && !visited[i])
                    s.push(i);
            }
        }
    }
    putchar('\n');
}

int main(void)
{
    AdjacentMatrixGraph graph;
    graph.insertVertex('A');
    graph.insertVertex('B');
    graph.insertVertex('C');
    graph.insertVertex('D');
    graph.insertVertex('E');
    graph.insertVertex('F');
    graph.insertVertex('G');

    graph.insertEdgeUndirected(0, 1);
    graph.insertEdgeUndirected(0, 2);
    graph.insertEdgeUndirected(1, 3);
    graph.insertEdgeUndirected(1, 4);
    graph.insertEdgeUndirected(2, 5);
    graph.insertEdgeUndirected(2, 6);

    graph.display();

    DFS(graph, 0);

    return 0;
}