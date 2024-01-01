#include <bits/stdc++.h>
using namespace std;

const int line = 88;            // 반복되는 한 줄의 길이.
long long messi[41] = {0, 5, 13, }; // 각 레벨별 길이
string base = "Messi Gimossi";

/**
 * @brief 기분 좋은 메시의 외침에서, M번째 글자를 반환한다.
 * 
 * @param m 구할 글자의 위치
 * @return char m번째 위치의 글자.
 */
char getCharAt(long long m, int n)
{
    // 범위를 어떻게 쪼개야 할까?
    // messi(N) = messi(N-1) + ' ' + messi(N-2)
    // 3가지 경우?
    // 1. M <= messi(N-1)
    // 2. M == messi(N-1) + 1
    // 3. M > messi(N-1) + 1 && M <= messi(N)

    if (n <= 2)              // 종료조건. m이 13 이내인 경우는 n이 얼마인지와 무관하게 항상 Messi Gimossi 안에서 찾게된다.
    {
        #ifdef DEBUG
            printf("return => %c\n", base[m-1]);
        #endif
        return base[m-1];
    }

    if (m <= messi[n-1])                // 1. M <= messi(N-1)
    {
        #ifdef DEBUG
            printf("Case 1: messi(N-1)\n");
        #endif
        return getCharAt(m, n-1);
    }
    else if (m == messi[n-1] + 1)       // 2. M == messi(N-1) + 1
    {
        #ifdef DEBUG
            printf("Case 2: messi(N-1) + ' '\nreturn => ' '\n");
        #endif
        return ' ';
    }
    else                                // M > messi(N-1) + 1 && M <= messi(N)
    {
        #ifdef DEBUG
            printf("Case 3: messi(N-1) messi(N-2)\n");
        #endif
        return getCharAt(m - messi[n-1] - 1, n-2);
    }
}

int main()
{
    long long M;
    scanf("%lld", &M);
    #ifdef DEBUG
        printf(">>> received M.\n");
    #endif
    int N = 2;
    while (messi[N] < M)
    {
        #ifdef DEBUG
            printf("messi(%d) = %lld\n", N, messi[N]);
        #endif
        messi[N+1] = messi[N] + messi[N-1] + 1;
        N++;
    }
    #ifdef DEBUG
        printf(">>> calculated N.\n");
        printf("N = %d\n", N);
    #endif
    char at = getCharAt(M, N);
    #ifdef DEBUG
        printf(">>> char at %lld = %c\n", M, at);
    #endif
    if (at == ' ')
        printf("Messi Messi Gimossi\n");
    else
        printf("%c\n", at);
    return 0;
}