#include <iostream>

using std::cin;
using std::cout;
using std::ios;

/**
 * @brief 노드 클래스. 연결 리스트의 노드를 나타냄.
 */
class Node
{
public:
    int num;                                    // 이 노드가 가지는 숫자값
    Node* next;                                 // 다음 노드의 주소
    Node(int n): num(n), next(nullptr) {}       // 생성자
};

/**
 * @brief 원형 연결 리스트
 */
class CircularList
{
private:
    Node* head;                 // 연결 리스트의 head 노드를 가리키는 포인터.
    Node* tail;                 // insert의 속도 개선을 위한 tail 노드 포인터.
public:
    CircularList(): head(nullptr), tail(nullptr) {}         // 생성자

    /**
     * @brief 새 노드를 삽입하는 함수
     * 
     * @param n 새 노드
     */
    void insert(Node* n)
    {
        if (head == nullptr)        // 리스트가 비어있다면
        {
            head = n;               // 새 노드를 head로 설정
            tail = n;               // 새 노드를 tail로 설정
            n->next = head;         // 새 노드가 자기 자신을 다음 노드로 가리키도록 함 (원형 연결 리스트)
        }
        else                        // 리스트에 기존 노드가 존재한다면
        {
            n->next = tail->next;   // '새 노드'의 '다음 노드'(next) 를 '마지막 노드'가 가리키던 다음 노드(head)로 설정.
            tail->next = n;         // '기존 마지막 노드'가 '새 노드'를 '다음 노드'(next) 로 가리키게 함.
            tail = n;               // '새 노드'를 tail로 설정.
        }
    }

    /**
     * @brief 기존 노드를 삭제하는 함수
     * 
     * @param p 삭제할 노드의 이전 노드
     * @param n 삭제할 노드
     * @return Node* 삭제된 노드
     */
    Node* remove(Node* p, Node* n)
    {
        p->next = n->next;          // 이전 노드가 삭제할 노드가 가리키던 다음 노드를 자신의 다음 노드로 가리키게 함.
        return n;                   // 삭제할 노드 반환.
    }

    /**
     * @brief 요세푸스 순열을 계산하기 위한 함수
     * 
     * @param N 전체 노드의 개수
     * @param K 제거할 노드의 간격
     */
    void josephus(int N, int K)
    {
        Node* cur = head;                           // '현재 노드'의 포인터 변수
        Node* prev = tail;                       // '현재 노드'의 이전 노드를 가리킬 포인터 변수
        Node* del = nullptr;                        // '삭제할 노드'의 포인터 변수
        cout << "<";
        for (int i = 0; i < N; i++)                 // N개의 수를 모두 제거할 때 까지
        {
            // K가 1이면 segfault!
            for (int j = 0; j < K - 1; j++)         // K번째 수를 찾기 위해 현재노드부터 K - 1번 이동 (반복 시작 노드를 포함해 K개)
            {
                prev = cur;
                cur = cur->next;
            }

            cout << cur->num;                       // K번째 수 출력
            if (i < N - 1)                          // 마지막 수가 아니라면, 쉼표(,) 출력
                cout << ", ";
            
            del = remove(prev, cur);                // 현재 노드를 제거
            cur = del->next;                        // '다음 반복을 시작할 노드'를 '제거된 노드의 다음 노드'로 설정
            delete del;                             // 제거된 노드의 할당 해제
        }
        cout << ">\n";
    }
};

// 진짜 어디서 Segfault가 나서 틀리는거지? -> 원인찾음

int main(void)
{
    // cin, cout 속도 개선 구문
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    CircularList list;              // 연결리스트 생성
    int N, K;
    cin >> N >> K;                  // 입력 받기

    for (int i = 1; i <= N; i++)    // 1~N까지 노드 생성
        list.insert(new Node(i));
    
    list.josephus(N, K);            // 요세푸스 순열 풀이
    return 0;
}