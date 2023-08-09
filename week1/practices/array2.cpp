#include <iostream>

using namespace std;

/**
 * @brief 배열을 출력하는 함수. (inline 함수이므로 실제 컴파일시 호출 구문을 대치한다.)
 * 
 * @param N 배열의 길이
 * @param arr 배열 포인터
 */
inline void display(int N, int** arr)
{
    for (int i = 0; i < N; i++)             // 행 반복
    {
        for (int j = 0; j < N; j++)         // 열 반복
            printf("%2d ", arr[i][j]);      // 길이 맞춰 출력하기 위해 printf 사용
        cout << '\n';                       // 개행문자 출력
    }
        
}

int main(void)
{
    int N;                                  // 배열 크기
    cin >> N;                               // 배열 크기 입력
    int** arr = new int*[N];                // int*의 1차원 배열 생성

    for (int i = 0; i < N; i++)
    {
        arr[i] = new int[N];                // arr의 각 원소로 다시 int형의 1차원 배열을 만들어 저장. (cf. 배열 이름은 주소값이다.)
        if (i % 2)                                  // 홀수번째 반복일 때
            for (int j = 0; j < N; j++)
                arr[i][j] = (i + 1) * N - j;    // 역순으로 저장
        else                                        // 짝수번째 반복일 때
            for (int j = 0; j < N; j++)
                arr[i][j] = i * N + j + 1;          // 순서대로 저장
    }

    display(N, arr);                        // 배열 출력
    return 0;
}