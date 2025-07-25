#include <bits/stdc++.h>
using namespace std;

vector<int>* graph;
bool* visited;

void DFS(int v)
{   
    visited[v] = true;
    printf("%d ", v);

    for (int i = 0; i < graph[v].size(); i++)   // 정렬을 통해 작은 번호부터 방문함이 보장됨.
    {
        int u = graph[v].at(i);
        if (!visited[u])
            DFS(u);
    }
}

void BFS(int v)
{
    queue<int> q;
    q.push(v);
    int u;
    while (q.size() != 0)
    {
        v = q.front();
        q.pop();

        if (visited[v])
            continue;
        
        visited[v] = true;
        printf("%d ", v);
        for (int i = 0; i < graph[v].size(); i++)
        {
            u = graph[v][i];
            if (!visited[u])
                q.push(u);    
        }
    }
}

int main()
{
    int N, M, V, u, v;
    scanf("%d %d %d\n", &N, &M, &V);

    graph = new vector<int>[N + 1];
    visited = new bool[N + 1];

    for (int i = 0; i < M; i++)
    {
        scanf("%d %d\n", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= N; i++)
        sort(graph[i].begin(), graph[i].end());
    
    DFS(V);
    printf("\n");
    
    // 정점의 방문 표기 초기화.
    for (int i = 1; i <= N; i++)
        visited[i] = false;
    BFS(V);
    printf("\n");

    return 0;
}