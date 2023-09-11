#include <iostream>

using namespace std;

/**
 * @brief 두 변수의 값을 바꾸는 함수 (inline 함수이므로 실제 호출 구문에서 대치됨.)
 * 
 * @param a 변수 1
 * @param b 변수 2
 */
inline void swap(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}

/**
 * @brief 일차원 배열을 출력하는 함수
 * 
 * @param N 배열의 크기
 * @param arr 배열 (포인터)
 */
inline void display(int N, int* arr)
{
    for (int i = 0; i < N; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main(void)
{
    int N, reverse, start, end, half;       // 변수 초기화
    cin >> N;                               // 배열 크기 입력
    int* arr = new int[N];                  // 배열 생성
    
    for (int i = 0; i < N; i++)             // 배열에 값 입력
        cin >> arr[i];

    #ifdef DEBUG                            // 디버그 코드: 초기 배열 출력
    cout << "initial" << endl;
    display(N, arr);
    #endif // DEBUG

    cin >> reverse;                         // 뒤집기 정보의 개수 입력
    for (int i = 0; i < reverse; i++)
    {
        cin >> start;                       // 뒤집기 정보: 시작 인덱스 입력
        cin >> end;                         // 뒤집기 정보: 끝 인덱스 입력

        #ifdef DEBUG                        // 디버그 코드: 뒤집기 정보 출력
        cout << "start = " << start << ", end = " << end << endl;
        #endif // DEBUG

        half = (start + end - 1) / 2;       // 중간 인덱스 계산
        for (int j = start; j <= half; j++)         // 뒤집을 범위의 시작부터 중간까지 반복
            swap(arr[j], arr[end - j + start]);     // 중간을 기준으로, 양쪽의 변수 값 교체
        
        #ifdef DEBUG                        // 디버그 코드: 현재 뒤집기 정보를 적용한 배열 출력
        display(N, arr);
        #endif // DEBUG
    }

    #ifdef DEBUG                            // 디버그 코드: 디버깅 시 결과 출력을 구분하기 위함
    cout << "---\nresult" << endl;
    #endif // DEBUG
    
    display(N, arr);                        // 결과 출력
    return 0;
}