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
class CircularLinkedList
{
private:
    Node<T>* head;
public:
    CircularLinkedList(): head(nullptr) {}
    ~CircularLinkedList()
    {
        // head 노드로부터 연결된 모든 노드를 해제할 때까지 반복.
        Node<T>* cur = head->next, *next = nullptr;
        while (cur != head)
        {
            next = cur->next;
            delete cur;
            cur = next;
        }
        delete head;
    }

    Node<T>* GetHead()
    {
        return head;
    }

    void Append(Node<T>* node)
    {
        if (head == nullptr)        // head가 노드를 가리키고 있지 않음.
        {
            head = node;            // head가 새 노드를 가리키게 함.
            node->next = head;
        }
        else
        {
            Node<T>* cur = head;
            while (cur->next != head)
                cur = cur->next;
            node->next = cur->next;
            cur->next = node;
        }
    }

    void Append(T value)
    {
        return Append(new Node<T>(value));
    }

    /**
     * @brief 리스트에 새 노드를 삽입한다.
     * 
     * @param p 이전 노드.
     * @param n 삽입할 새 노드.
     */
    void Insert(Node<T>* p, Node<T>* n)
    {
        n->next = p->next;
        p->next = n;
    }

    /**
     * @brief 리스트의 @arg index 위치에 @arg node를 삽입한다.
     * 
     * @param index 새 노드를 삽입할 위치
     * @param node 새 노드
     */
    void Insert(int index, Node<T>* node)
    {
        if (head != nullptr)
        {
            Node<T>* cur = head;
            for (int i = 0; i < index && cur->next != nullptr; cur = cur->next, i++);
            Insert(cur, node);
        }
    }

    /**
     * @brief 리스트의 @arg index 위치에 @arg data의 노드를 삽입한다.
     * 
     * @param index 새 노드를 삽입할 위치
     * @param data 새 데이터
     */
    void Insert(int index, T data)
    {
        Insert(index, new Node<T>(data));
    }

    Node<T>* Search(T value)
    {
        for(Node<T>* cur = head->next; cur != head; cur = cur->next)
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
        Node<T>* cur = head;
        while (true)
        {
            cout << cur->data << " ";
            cur = cur->next;
            if (cur == head)
                break;
        }
        cout << endl;
    }
};

template <typename T>
void TestCircularLinkedList(CircularLinkedList<T> list)
{
    int i = 0;
    Node<T>* head = list.GetHead(), *cur = head;
    // 연결리스트를 2회 순회하기
    while (true)
    {
        cout << cur->data << " ";
        cur = cur->next;
        if (cur == head)
            i++;
        if (i > 1)
            break;
    }
}

int main(void)
{
    CircularLinkedList<int> list;
    list.Append(1);
    list.Append(2);
    list.Append(3);
    list.Display();
    
    list.Insert(1, 4);
    list.Display();

    list.Delete(2);
    list.Display();

    TestCircularLinkedList(list);
    return 0;
}