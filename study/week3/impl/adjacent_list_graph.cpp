#include <iostream>
#define MAX_VTXS 256

using namespace std;

/**
 * @brief 인접 리스트에 사용할 노드 클래스
 */
class Node
{
public:
    int id;             // 정점의 id
    Node* next;         // 다음 Node의 주소
    Node(int id, Node* node): id(id), next(node) {}
};

/**
 * @brief 인접리스트로 구현한 그래프
 */
class AdjacentListGraph
{
private:
    int size;
    char vertices[MAX_VTXS];
    Node* edges[MAX_VTXS];

public:
    AdjacentListGraph(): size(0)
    {
        for (int i = 0; i < MAX_VTXS; i++)
            edges[i] = nullptr;     // CLEAN UP ARRAY
    }

    ~AdjacentListGraph()
    {
        reset();
    }

    /**
     * @brief 주어진 정점 인덱스(id) 를 사용해 정점의 이름을 가져온다.
     * 
     * @param id 정점의 인덱스.
     * @return char 정점의 이름.
     */
    char getVertex(int id)
    {
        return vertices[id];
    }

    /**
     * @brief 그래프가 가득 찼는지 판단한다.
     * 
     * @return true 그래프의 정점의 개수가 MAX_VTXS개일 때.
     * @return false 그래프의 정점의 개수가 MAX_VTXS개보다 적을 때.
     */
    bool isFull()
    {
        return size == MAX_VTXS;
    }

    int getSize()
    {
        return size;
    }

    /**
     * @brief 그래프가 비어있는지 판단한다.
     * 
     * @return true 그래프의 정점의 개수가 0개일 때.
     * @return false 그래프에 1개 이상의 정점이 있을 때.
     */
    bool isEmpty()
    {
        return size == 0;
    }

    /**
     * @brief 새 정점을 그래프에 삽입한다.
     * 
     * @param name 새 정점의 이름.
     */
    void insertVertex(char name)
    {
        if (isFull())
            throw "AdjacentListGraph is full!";
        vertices[size++] = name;
    }

    /**
     * @brief 무방향 그래프의 간선을 추가한다. (u-v)
     * 
     * @param u 정점 인덱스.
     * @param v 정점 인덱스.
     */
    void insertEdgeUndirected(int u, int v)
    {
        insertEdgeDirected(u, v);
        insertEdgeDirected(v, u);
    }

    /**
     * @brief 방향 그래프의 간선을 추가한다. (u->v)
     * 
     * @param u 정점 인덱스.
     * @param v 정점 인덱스.
     */
    void insertEdgeDirected(int u, int v)
    {
        edges[u] = new Node(v, edges[u]);       // 새로운 노드로 head 포인터 변경.
    }

    Node* adjacentEdges(int u)
    {
        return edges[u];
    }

    /**
     * @brief 그래프를 초기화한다.
     */
    void reset()
    {
        for (int i = 0; i < size; i++)
            if (edges[i] != nullptr)
            {
                delete[] edges[i];
                edges[i] = nullptr;
            }
        size = 0;
    }

    /**
     * @brief 그래프를 출력한다.
     */
    void display()
    {
        printf("vertex size: %d\n", size);
        for (int i = 0; i < size; i++)
        {
            printf("%c : ", getVertex(i));
            Node* head = edges[i];
            while (head != nullptr)
            {
                printf("%c ", getVertex(head->id));
                head = head->next;
            }
            putchar('\n');
        }
    }
};

#ifndef INCLUDE_ADJACENTLISTGRAPH      // 타 코드에서 include하지 않는 경우에만 main을 포함.
int main(void)
{
    AdjacentListGraph graph;

    graph.insertVertex('A');
    graph.insertVertex('B');
    graph.insertVertex('C');
    graph.insertVertex('D');

    graph.insertEdgeUndirected(0, 1);   // A -> B, B -> A
    graph.insertEdgeUndirected(0, 3);   // A -> D, D -> A
    graph.insertEdgeUndirected(1, 2);   // B -> C, C -> B
    graph.insertEdgeUndirected(1, 3);   // B -> D, D -> B
    graph.insertEdgeUndirected(2, 3);   // C -> D, D -> C

    graph.display();
    return 0;
}
#endif