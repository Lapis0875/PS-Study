# Migrated from ./boj/boj2622.c by boj_validator
#include <stdio.h>

int max(int a, int b)
{
    return a > b ? a : b;
}

int main()
{
    int N, remaining, k, count = 0;
    scanf("%d", &N);

    for (int i = 1; i < N / 3 + 1; i++)
    {
        remaining = N - i;
        for (int j = 1; j < max(remaining, i); j++)
        {
            k = remaining - j;

            if (k < j)
                break;
            
            if (k < i + j && i <= j)
                count++;
        }
    }
    printf("%d\n", count);
    return 0;
}