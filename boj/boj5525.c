#include <stdio.h>

int main()
{
    int N, M, repeat = 0, count = 0;
    char S[1000001];

    scanf("%d", &N);
    scanf("%d", &M);
    scanf("%s", S);

    for (int i = 0; i < M; i++)
    {
        printf(">>> for (i = %d)\n", i);
        if (S[i] != 'I')
            continue;
        
        repeat = 0;
        while (S[i+1] == 'O' && S[i+2] == 'I')
        {
            repeat++;

            if (repeat == N)
            {
                count++;
                printf(">>> cnt++, i = %d\n", i);
                break;
            }

            i += 2;
        }

    }
    printf("%d\n", count);

    return 0;
}