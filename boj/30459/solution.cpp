#include <bits/stdc++.h>
using namespace std;

int N, M, R;
int A[2001];
int B[40001];

int main()
{
    scanf("%d %d %d", &N, &M, &R);                              // 1. 변수 입력받기.
    R *= 2;                                                     // 1-1. 면적을 편리하게 계산하기 위해, 삼각형의 2배인 직사각형으로 계산한다.

    for (int i = 0; i < N; i++)                                 // 2. A 배열 (말뚝) 입력받기.
        scanf("%d", A + i);

    for (int i = 0; i < M; i++)                                 // 3. B 배열 (깃대) 입력받기.
        scanf("%d", B + i);
    
    sort(A, A + N);                                             // 4. A 배열 정렬하기.
    sort(B, B + M);                                             // 5. B 배열 정렬하기.
    
    int w = 0, idx = -1, maxArea = -1, area;

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            w = A[j] - A[i];                                    // 6. 말뚝의 높이 차이를 구한다.
            printf("i = %d, j = %d, w = %d\n", i, j, w);
            idx = upper_bound(B, B + M, R / w) - B - 1;                 // 7. R / w보다 작거나 같은 값들 중 가장 끝 인덱스를 이분탐색으로 구한다.
            printf("upper_bound(...) -> %d\n", idx);
            if (idx != -1)
            {
                maxArea = max(maxArea, w * B[idx]);             // 8. 최대 면적을 구한다.
                printf("최대 면적 갱신됨: %d\n", maxArea);
            }
        }
    }
    if (maxArea == -1)
        printf("-1\n");
    else
        printf("%.1f\n", maxArea / 2.0);
    return 0;
}