#include <iostream>
#include <queue>
#define INCLUDE_ADJACENTLISTGRAPH
#include "adjacent_list_graph.cpp"

using namespace std;

void BFS(AdjacentListGraph& graph, int root)
{
    const int size = graph.getSize();
    bool* visited = new bool[size];
    int v;
    Node* node;
    queue<int> q;
    q.push(root);

    while (!q.empty())
    {
        v = q.front();
        q.pop();
        if (!visited[v])
        {
            visited[v] = true;
            printf("%c ", graph.getVertex(v));
            node = graph.adjacentEdges(v);
            while (node != nullptr)
            {
                if (!visited[node->id])
                    q.push(node->id);
                node = node->next;
            }
        }
    }
    putchar('\n');
}

int main(void)
{
    AdjacentListGraph graph;

    graph.insertVertex('A');
    graph.insertVertex('B');
    graph.insertVertex('C');
    graph.insertVertex('D');
    graph.insertVertex('E');

    graph.insertEdgeUndirected(0, 1);
    graph.insertEdgeUndirected(0, 2);
    graph.insertEdgeUndirected(0, 4);
    graph.insertEdgeUndirected(1, 2);
    graph.insertEdgeUndirected(2, 3);
    graph.insertEdgeUndirected(2, 4);
    graph.insertEdgeUndirected(3, 4);

    graph.display();

    BFS(graph, 0);
    return 0;
}
