#include <bits/stdc++.h>
using namespace std;

int world[50][50];
bool visited[50][50];

int directions[8][2] = {
    {1, 0},
    {0, 1},
    {0, -1},
    {-1, 0},
    {1, 1},
    {-1, -1},
    {1, -1},
    {-1, 1}
};

int w, h;

int DFS(int x, int y)
{
    #ifdef DEBUG
        printf("DFS(%d, %d)\n", x, y);
    #endif
    visited[y][x] = true;
    int cnt = 1;

    int nx, ny;
    for (int i = 0; i < 8; i++)
    {
        nx = x + directions[i][0];
        ny = y + directions[i][1];

        if ((nx >= 0 && nx < w) && (ny >= 0 && ny < h) && world[ny][nx] == 1 && !visited[ny][nx])
            cnt += DFS(nx, ny);
    }
    return cnt;
}

int main()
{
    int case_cnt = 1;
    while (true)
    {
        scanf("%d %d", &w, &h);

        if (w == 0)
        {
            #ifdef DEBUG
                printf("Exit!\n");
            #endif
            break;
        }

        #ifdef DEBUG
            printf("Case %d\n", case_cnt++);
            printf("w: %d, h: %d\n", w, h);
        #endif
        // 초기화.
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                scanf("%d", &world[i][j]);    // 지도 읽기.
                visited[i][j] = false;      // 방문 여부 초기화.
            }
            getchar();      // 개행 제거.
        }

        const int max_visit = w * h;
        int visit_cnt = 0;
        int islands = 0;
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                if (world[i][j] == 1 && !visited[i][j])
                {
                    visit_cnt += DFS(j, i);
                    islands++;
                    #ifdef DEBUG
                        printf("방문한 좌표 개수: %d\n", visit_cnt);
                        printf("섬 개수: %d\n", islands);
                    #endif
                }
                if (visit_cnt == max_visit)
                    break;
            }
        }
        printf("%d\n", islands);
    }
    return 0;
}