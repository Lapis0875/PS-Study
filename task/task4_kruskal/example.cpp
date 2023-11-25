#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

typedef int index;              // 의사코드에 쓰이는 index 타입 선언

/**
 * @brief disjoint set structure (2)
 */
const int n = 5;                // 정점의 개수
typedef index set_pointer;          // disjoint set structure에 사용되는 set_pointer 타입 선언

/**
 * @brief disjoint set structure (2) 에서 사용할 노드의 구조체.
 */
typedef struct nodetype
{
    index parent;
    int depth;
} nodetype;

typedef nodetype universe[n + 1];   // 인덱스를 1부터 사용하기 위해, n + 1개의 원소를 가지는 universe 배열 선언
universe U;                         // 정점별 노드를 저장할 universe 배열

/**
 * @brief i번 정점을 유일한 원소로 가지는 집합을 생성한다.
 * 
 * @param i 생성할 집합의 원소
 */
void makeset(index i)
{
    U[i].parent = i;
    U[i].depth = 0;
}

/**
 * @brief n개의 정점을 원소로 가지는 universe 배열을 초기화한다.
 * 
 * @param n 정점의 개수
 */
void initial(int n)
{
    for (index i = 1; i <= n; i++)
        makeset(i);
}

/**
 * @brief 두 집합 p, q가 같은 집합인지 확인한다.
 * 
 * @param p p 집합을 가리키는 정수
 * @param q q 집합을 가리키는 정수
 * @return true 두 집합이 같다.
 * @return false 두 집합이 다르다.
 */
bool equal(set_pointer p, set_pointer q)
{
    // 의사 코드처럼 직접 true, false를 반환해도 되지만, 사실 p == q라는 비교문 자체가 이미 true, false 값을 결정.
    return p == q;
}

/**
 * @brief i번 집합의 최상위 부모 노드를 탐색한다.
 * 
 * @param i 찾고자 하는 노드(집합)
 * @return set_pointer i번 집합의 최상위 부모 노드
 */
set_pointer find(index i)
{
    index j = i;
    while (U[j].parent != j)
        j = U[j].parent;
    return j;
}

/**
 * @brief 두 집합을 병합한다.
 * 
 * @param p p 집합을 가리키는 정수
 * @param q q 집합을 가리키는 정수
 */
void merge(set_pointer p, set_pointer q)
{
    if (U[p].depth == U[q].depth)
    {
        U[p].depth += 1;
        U[q].parent = p;
    }
    else if (U[p].depth < U[q].depth)
        U[p].parent = q;
    else
        U[q].parent = p;
}

/**
 * @brief Kruskal's algorithm 
 */

typedef tuple<int, int, int> edge;      // (v1, v2, weight) 의 3개 원소를 가진다.
typedef vector<edge> set_of_edges;

/**
 * @brief set_of_edges 집합을 가중치가 작은 순으로 간선을 정렬한다.
 * 
 * @param u 집합 내의 간선
 * @param v 집합 내의 간선
 * @return true 간선 u의 가중치가 v보다 작은 경우
 * @return false 간선 u의 가중치가 v보다 같거나 큰 경우
 */
bool compare(const edge& u, const edge& v)
{
    return get<2>(u) < get<2>(v);
}

/**
 * @brief vector<edge> 의 원소들을 queue<edge>로 옮긴다.
 * 
 * @param E 옮길 요소들을 가지고 있는 vector<edge> 객체.
 * @param queue_E 요소들을 옮겨 저장할 queue<edge> 객체.
 */
void convert_queue(const set_of_edges& E, queue<edge>& queue_E)
{
    for (index i = 0; i < E.size(); i++)
        queue_E.push(E.at(i));
}

/**
 * @brief 크루스칼 알고리즘
 * 
 * @param n 정점의 개수
 * @param m 간선의 개수
 * @param E 간선의 집합
 * @param F MST(최소 신장 트리)에 속하는 간선들의 집합. 이 함수의 출력으로 사용한다.
 */
void kruskal(int n, int m, set_of_edges E, set_of_edges& F)
{
    index i, j;
    set_pointer p, q;

    sort(E.begin(), E.end(), compare);      // 1. E를 가중치의 오름차순으로 정렬
    queue<edge> queue_E;
    convert_queue(E, queue_E);
    F.clear();                              // 2. F를 공집합으로 초기화

    initial(n);                             // 3. union-find 알고리즘을 위해 disjoint set을 초기화한다.

    while (F.size() < n - 1)
    {
        edge e = queue_E.front();           // 4. E에서 가장 작은 가중치를 가진 간선 e를 가져옴
        queue_E.pop();
        i = get<0>(e);                      // e의 두 정점을 i, j에 저장
        j = get<1>(e);
        
        p = find(i);                        // 5. i, j 정점이 속한 집합을 찾는다.
        q = find(j);

        if (!equal(p, q))                   // p와 q가 다른 집합이다, 즉 간선 e를 MST에 추가해도 사이클이 생기지 않는다.
        {
            merge(p, q);                    // 6. p와 q를 합친다.
            F.push_back(e);                 // 7. 간선 e를 MST 에 추가한다.
        }
    }
}

/**
 * @brief 실제 알고리즘 코드를 동작시킬 main 함수
 * 
 * @return int 종료 코드.
 */
int main(void)
{
    set_of_edges E;                         // 간선의 집합 E
    set_of_edges F;                         // MST에 포함되는 간선의 집합

    int m = 7;                              // 간선의 개수

    // 간선 집합에 그래프의 간선들을 추가한다.
    E.push_back(make_tuple(1, 2, 1));            // v1 - v2 (1)
    E.push_back(make_tuple(1, 3, 3));            // v1 - v3 (3)
    E.push_back(make_tuple(2, 3, 3));            // v2 - v3 (3)
    E.push_back(make_tuple(2, 4, 6));            // v2 - v4 (6)
    E.push_back(make_tuple(3, 4, 4));            // v3 - v4 (4)
    E.push_back(make_tuple(3, 5, 2));            // v3 - v5 (2)
    E.push_back(make_tuple(4, 5, 5));            // v4 - v5 (5)

    kruskal(n, m, E, F);                    // 크루스칼 알고리즘을 수행한다.

    // MST에 포함되는 간선들을 출력한다.
    int u, v, w;
    for (index i = 0; i < F.size(); i++)
    {
        tie(u, v, w) = F.at(i);
        printf("v%d - v%d (%d)\n", u, v, w);
    }
}
