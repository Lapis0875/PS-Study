#include <bits/stdc++.h>
using namespace std;

int N;

/**
 * @brief 하노이 탑 알고리즘을 재귀를 이용해 해결합니다.
 * 
 * @param plate 현재 호출에서 옮겨야 하는 원판의 개수.
 * @param from 이번 호출에서 원판을 옮겨야 하는 출발 지점.
 * @param via 이번 호출에서 원판을 옮기는 도중에 거칠 수 있는 중간 지점.
 * @param to 이번 호출에서 원판을 옮길 도착 지점.
 * @return int 원판을 옮긴 횟수.
 */
void hanoi(int plate, int from, int via, int to)
{
    if (plate == 1)                                     // 1개의 원판을 옮기는 경우 (재귀 종료 조건)
    {
        printf("%d %d\n", from, to);                    // 옮긴 경로를 출력한다. 중간지점 없이 바로 from -> to 할 수 있다.
        return;                                       // 옮긴 횟수.
    }
    hanoi(plate - 1, from, to, via);           // n-1개의 원판을 1에서 3을 거쳐 2로 옮김.
    hanoi(1, from, via, to);                   // 가장 큰 마지막 원판을 1에서 2를 거쳐 3으로 옮김.
    hanoi(plate - 1, via, from, to);           // 앞서 옮겨둔 n-1개의 원판을 다시 2에서 1을 거쳐 3으로 옮김.
}

int main()
{
    scanf("%d", &N);
    printf("%d\n", (1 << N) - 1);
    hanoi(N, 1, 2, 3);
    return 0;
}
