#include <bits/stdc++.h>
using namespace std;

int answer[8];
bool used[9];
int M;
int N;


void solve(int i)
{
    if (i == M)
    {
        for (int idx = 0; idx < M; idx++)
            printf("%d ", answer[idx]);
        printf("\n");
        return;
    }
    for (int n = i > 0 ? answer[i-1] : 1; n <= N; n++)
    {
        if (!used[n])
        {
            used[n] = true;
            answer[i] = n;
            solve(i + 1);
            used[n] = false;
        }
    }
}

int main()
{
    scanf("%d %d", &N, &M);
    solve(0);
}