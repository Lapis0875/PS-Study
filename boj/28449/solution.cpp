#include <bits/stdc++.h>
using namespace std;

int N, M;
int HI[100000];     // HI 팀의 점수를 저장한다. 입력받은 뒤 정렬된다.
int ARC[100000];    // ARC팀의 점수를 저장한다. 정렬하지 않는다.
long long drawCache[100001];   // ARC팀의 각 선수와 비기는 선수들의 수를 미리 기록해 둔다.

/**
 * @brief 이분 탐색을 통해 상한을 찾는다. (Upper-Bound)
 * 주어진 배열에서 특정 값보다 큰 값이 처음으로 나오는 위치의 인덱스를 반환한다.
 * 
 * @param low 탐색 범위의 하한
 * @param high 탐색 범위의 상한
 * @param target 찾고자 하는 값
 * 
 * @return int target 보다 큰 값이 처음 나오는 위치의 인덱스
 */
int upperBound(int low, int high, int target)
{
    int mid;
    while (low != high)
    {
        mid = (low + high) / 2;
        printf("low = %d, high = %d, mid = %d\n", low, high, mid);
        if (HI[mid] <= target)       // target보다 "큰" 값이 필요하므로, low ~ mid까지의 범위는 불필요하다.
            low = mid + 1;
        else
            high = mid;         // target보다 "큰" 값이 필요하고, 가장 처음 나온 인덱스가 필요하므로, mid + 1 ~ high까지의 범위는 불필요하다.
    }
    return low;
}

int main()
{
    long long arcWin = 0, hiWin = 0, draw = 0;          // ARC의 승리, 무승부, 패배 횟수를 저장한다.

    scanf("%d %d", &N, &M);                             // 1. N과 M 입력받기.

    for (int i = 0; i < N; i++)                         // 2. HI 배열 입력받기.
    {
        scanf("%d", &HI[i]);
        drawCache[HI[i]]++;                             // 2-1. HI팀의 선수들의 코딩력을 기준으로 선수들의 수를 센다.
    }
    
    for (int i = 0; i < M; i++)                         // 3. ARC 배열 입력받기.
        scanf("%d", &ARC[i]);

    sort(HI, HI + N);                                   // 4. HI 배열 정렬하기.

    for (int i = 0; i < M; i++)                         // 5. Solve.
    {
        int upper = upperBound(0, N, ARC[i]);       // ARC[i]의 코딩력보다 큰 HI팀의 최소 번호.
        int d = drawCache[ARC[i]];                  // ARC[i]의 코딩력과 같은 코딩력을 가진 HI팀의 수.
        draw += d;                                  // 미리 기록해둔 비기는 인원 수를 더한다.
        hiWin += N - upper;                     // HI팀의 이긴 인원수는 (HI팀의 인원수) - (ARC[i]에게 패배한 인원수) - (ARC[i]와 비긴 인원수) 이다..
        arcWin += upper - d;                            // ARC팀의 이긴 인원수는 Upper Bound 탐색의 결과이다.
        printf("ARC[%d] = %d에 대한 코딩력 대결 결과:\n- HI승 = %d\n- ARC승 =  %d\n- 무승부 =  %d\n\n", i, ARC[i], N - upper - d, upper, d);
    }

    printf("%lld %lld %lld\n", hiWin, arcWin, draw);    // 6. 결과 출력하기.
    return 0;
}