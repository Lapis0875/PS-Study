#include <bits/stdc++.h>
using namespace std;

long long burger_length[51] = {1, };      // 각 레벨별 버거의 길이
long long patty[51] = {1, };              // 각 레벨별 패티의 개수
int N;                                    // 문제 조건의 N
long long X;                              // 문제 조건의 X


long long res = 0;
/**
 * @brief 현재 레벨에서, length까지의 패티의 개수를 구한다.
 * 
 * @param level 현재 버거의 레벨
 * @param length 현재 버거의 먹은 길이
 */
void count_patty(int level, long long length)
{
    if (length == 1)                                 // (1) B
    {
        #ifdef DEBUG
            printf("Case 1: B =>\n");
            printf("N = %d, X = %lld\n", level, length);
            printf("=> Patty +0\n");
        #endif
        if (level == 0)                             // 레벨 0 버거는 패티뿐.
            res += 1;
        // res += 0;                                // 먹은 패티 수에 변화가 없다.
    }
    else if (length > 1 && length < burger_length[level-1] + 2)       // (2) B (N-1)
    {
        #ifdef DEBUG
            printf("Case 2: B (N-1)\n");
            printf("N = %d, X = %lld\n", level, length);
            printf("=> Patty +?\n");
        #endif
        count_patty(level-1, length-1);
    }
    else if (length == burger_length[level-1] + 2)       // (3) B (N-1) P
    {
        #ifdef DEBUG
            printf("Case 3: B (N-1) P =>\n");
            printf("N = %d, X = %lld\n", level, length);
            printf("=> Patty +%lld\n", patty[level-1] + 1);
        #endif
        res += patty[level-1] + 1;
    }
    else if (length > burger_length[level-1] + 2 && length < burger_length[level])   // (4) B (N-1) P (N-1)
    {
        #ifdef DEBUG
            printf("Case 4: B (N-1) P (N-1)\n");
            printf("N = %d, X = %lld\n", level, length);
            printf("=> Patty +%lld+?\n", patty[level-1] + 1);
        #endif
        res += patty[level-1] + 1;      // 중간 패티까지의 길이를 먼저 반영 후
        count_patty(level-1, length - burger_length[level-1] - 2);      // 나머지 조각에 대한 연산.
    }
    else                                        // (5) B (N-1) P (N-1) B
    {
        #ifdef DEBUG
            printf("Case 5: B (N-1) P (N-1) B =>\n");
            printf("N = %d, X = %lld\n", level, length);
            printf("=> Patty +%lld\n", patty[level]);
        #endif
        res += patty[level];
    }
}

int main()
{
    for (int i = 1; i <= 50; i++)
    {
        // B (i-1) P (i-1) B
        burger_length[i] = burger_length[i-1] * 2 + 3;
        patty[i] = patty[i-1] * 2 + 1;
    }
    
    scanf("%d %lld", &N, &X);
    #ifdef DEBUG
        printf("N = %d, X = %lld\n", N, X);
        printf("length[N] = %lld, patty[N] = %lld\n", burger_length[N], patty[N]);
        printf("---\n");
    #endif
    count_patty(N, X);
    printf("%lld\n", res);

    return 0;
}