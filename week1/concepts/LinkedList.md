# 2. 연결리스트

연결리스트는 `노드(Node)` 라고 불리는 데이터 덩어리를 연결해 데이터를 저장하는 **선형 자료구조**이다.

## 배열과의 차이점?

배열의 경우, 처음 선언할 시점에 크기가 고정된다. 하지만 연결 리스트의 경우 계속해서 노드를 할당해, 크기를 동적으로 변경할 수 있다.

또, 배열의 경우 요소들이 메모리 상에 연속적으로 저장되어 있어 임의 위치에 빠르게 접근할 수 있으나 연결 리스트의 경우 임의의 인덱스에 접근하려면 그 만큼 노드의 포인터를 따라가야 한다.

## 시간복잡도

- 조회(read) : $O(N)$
  - 주소 연산을 사용해 상수 시간에 요소에 접근할 수 있던 배열과 달리, 연결 리스트는 특정 위치를 찾기 위해서도 탐색을 수행해야 한다.
- 탐색(search) : $O(N)$
  - 연결리스트를 순회하며 값을 비교해야 하기 때문이다.
- 삽입(insert) : $O(1)$
  - 이전 노드와 새 노드의 포인터만 적절히 바꿔주면 되기 때문에, 별도로 연결리스트를 순회할 필요가 없다.
- 삭제(delete) : $O(1)$
  - 이전 노드와 새 노드의 포인터만 적절히 바꿔주면 되기 때문에, 별도로 연결리스트를 순회할 필요가 없다.

## 구현 방법

1. 단일 연결 리스트

데이터와, 다음 노드를 가리키는 포인터 하나로 구성된 노드로 연결 리스트를 구성한다.

```cpp
#include <iostream>

using namespace std;

template <typename T>
class Node
{
public:
    T data;
    Node<T>* next;
    Node(T v): data(v), next(nullptr) {}
};

template <typename T>
class LinkedList
{
private:
    Node<T>* head;
public:
    LinkedList(): head(nullptr) {}
    ~LinkedList()
    {
        // head 노드로부터 연결된 모든 노드를 해제할 때까지 반복.
        Node<T>* cur = head, *next = nullptr;
        while (cur != nullptr)
        {
            next = cur->next;
            delete cur;
            cur = next;
        }
    }

    void Append(Node<T>* node)
    {
        if (head == nullptr)        // head가 노드를 가리키고 있지 않음.
            head = node;            // head가 새 노드를 가리키게 함.
        else
        {
            Node<T>* cur = head;
            while (cur->next != nullptr)
                cur = cur->next;
            cur->next = node;
        }
    }

    void Append(T value)
    {
        return Append(new Node<T>(value));
    }

    void Insert(int index, Node<T>* node)
    {
        if (head != nullptr)
        {
            Node<T>* cur = head;
            for (int i = 0; i < index && cur->next != nullptr; cur = cur->next, i++);
            node->next = cur->next;     // 기존 노드의 다음 노드를 새 노드가 가리키게 한다.
            cur->next = node;           // 기존 노드가 새 노드를 다음 노드로 가리키게 한다.
        }
    }

    void Insert(int index, T data)
    {
        return Insert(index, new Node<T>(data));
    }

    Node<T>* Search(T value)
    {
        for(Node<T>* cur = head; cur != nullptr; cur = cur->next)
            if (cur->data == value)
                return cur;
        return nullptr;     // 리스트 내에 해당 값이 존재하지 않음.
    }

    void Delete(T value)
    {
        Node<T>* prev = head, *cur = head->next;
        for (; cur != nullptr; prev = cur, cur = cur->next)
        {
            if (cur->data == value)
            {
                prev->next = cur->next;
                delete cur;
                return;
            }
        }
    }

    void Display()
    {
        for(Node<T>* cur = head; cur != nullptr; cur = cur->next)
            cout << cur->data << " ";
        cout << endl;
    }
};

int main(void)
{
    LinkedList<int> list;
    list.Append(1);
    list.Append(2);
    list.Append(3);
    list.Display();
    
    list.Insert(1, 4);
    list.Display();

    list.Delete(2);
    list.Display();
    return 0;
}
```

2. 이중 연결 리스트

앞서 만들었던 단일 연결 리스트에서, 노드가 이전 노드 또한 가리키는 구조를 가지는 연결 리스트의 구현체이다.

