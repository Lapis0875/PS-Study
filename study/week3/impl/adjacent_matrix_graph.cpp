#include <iostream>
#define MAX_VTXS 256

using namespace std;

/**
 * @brief 인접행렬로 구현한 그래프
 */
class AdjacentMatrixGraph
{
private:
    int size;           // 정점의 개수
    char vertices[MAX_VTXS];      // 정점의 이름
    int matrix[MAX_VTXS][MAX_VTXS];      // 인접 행렬
public:
    /**
     * @brief 생성자.
     */
    AdjacentMatrixGraph() : size(0)
    {
        reset();
    }
    ~AdjacentMatrixGraph() {}   // 소멸자. 사용되지 않는다.

    bool isFull()
    {
        return size == MAX_VTXS;
    }

    bool isEmpty()
    {
        return size == 0;
    }

    int getSize()
    {
        return size;
    }

    /**
     * @brief 해당 인덱스의 정점의 문자 (이름)를 가져온다.
     * 
     * @param i 정점의 인덱스
     * @return char 정점의 이름
     */
    char getVertex(int i)
    {
        return vertices[i];
    }

    /**
     * @brief 두 정점 사이의 간선을 반환한다.
     * 
     * @param u 정점
     * @param v 정점
     * @return int 간선의 가중치. 0이면 간선이 없다.
     */
    int getEdge(int u, int v)
    {
        return matrix[u][v];
    }

    /**
     * @brief 두 정점 사이의 간선을 추가한다.
     * 
     * @param u 정점
     * @param v 정점
     * @param w 간선의 가중치
     */
    void setEdge(int u, int v, int w)
    {
        matrix[u][v] = w;
    }

    /**
     * @brief 그래프에 정점을 추가한다.
     * 
     * @param name 새 정점의 이름.
     */
    void insertVertex(char name)
    {
        if (isFull())
            throw "AdjacentMatrixGraph is full!";
        vertices[size++] = name;
    }

    /**
     * @brief 무방향 그래프에 새 간선을 추가한다. (두 정점 사이에 양방향으로 저장한다.)
     * 
     * @param u 정점
     * @param v 정점
     * @param w 간선의 가중치. 기본값은 1이다.
     */
    void insertEdgeUndirected(int u, int v, int w = 1)
    {
        setEdge(u, v, w);
        setEdge(v, u, w);
    }

    /**
     * @brief 방향 그래프에 새 간선을 추가한다. (u->v 간선만 추가한다.)
     * 
     * @param u 정점
     * @param v 정점
     * @param w 간선의 가중치. 기본값은 1이다.
     */
    void insertEdgeDirected(int u, int v, int w = 1)
    {
        setEdge(u, v, w);
    }

    /**
     * @brief 그래프를 초기화한다.
     */
    void reset()
    {
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++)
                setEdge(i, j, 0);
        size = 0;
    }

    void display()
    {
        printf("Vertex size : %d\n", size);

        putchar(' ');
        for (int i = 0; i < size; i++)
            printf(" %c", getVertex(i));
        putchar('\n');

        for (int i = 0; i < size; i++)
        {
            printf("%c ", getVertex(i));
            for (int j = 0; j < size; j++)
                printf("%d ", getEdge(i, j));
            putchar('\n');
        }
    }
};

#ifndef INCLUDE_ADJACENTMATRIXGRAPH      // 타 코드에서 include하지 않는 경우에만 main을 포함.
int main(void)
{
    AdjacentMatrixGraph graph;

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