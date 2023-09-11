#include <iostream>

using namespace std;

/**
 * @brief 연결리스트의 노드 클래스
 */
class Node
{
public:
    string data;    // 각 노드가 저장할 문자열
    Node* next;     // 다음 노드의 주소
    Node(string v, Node* n = nullptr): data(v), next(n) {}      // 생성자
};

/**
 * @brief 연결리스트 클래스
 */
class LinkedList
{
    Node* head;         // 연결리스트의 head 노드 포인터.
    Node* tail;         // insert의 편의를 위한 tail 노드 포인터.
public:
    LinkedList(): head(nullptr), tail(nullptr) {}               // 생성자
    ~LinkedList()                                               // 소멸자
    {
        Node* cur = head, *next = nullptr;                      // 노드 포인터 변수 초기화
        while (cur != nullptr)                                  // cur 포인터가 nullptr일때까지
        {
            next = cur->next;                                   // 다음 노드로 이동하고
            delete cur;                                         // 현재 노드를 삭제한 뒤
            cur = next;                                         // cur 포인터에 다음 노드의 주소 저장
        }
    }

    /**
     * @brief 새 노드를 삽입하는 연산
     * 
     * @param node 새 노드
     */
    void insert(Node* node)
    {
        if (head == nullptr)
        {
            head = node;
            tail = node;
        }
        else
        {
            tail->next = node;
            tail = node;
        }
    }

    /**
     * @brief 리스트를 출력하는 함수
     */
    void display()
    {
        Node* cur = head;               // 현재 노드의 포인터
        while(cur != nullptr)
        {
            cout << cur->data.append("\n");
            cur = cur->next;
        }
    }
};

int main(void)
{
    string input;                       // 콘솔 입력을 저장할 문자열 변수
    LinkedList list;                    // 리스트 객체 생성
    while (true)                        // quit 문자를 받을때까지 무한반복
    {
        cin >> input;                   // 콘솔에서 문자열 입력받기
        if (input == "quit")            // 반복 종료
            break;
        list.insert(new Node(input));   // 입력받은 문자열을 리스트에 추가
    }
    list.display();                     // 리스트의 모든 노드 출력
    return 0;
}