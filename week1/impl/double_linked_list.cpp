#include <iostream>

using namespace std;

template <typename T>
class Node
{
public:
    T data;
    Node<T>* prev;
    Node<T>* next;
    Node(T v): data(v), next(nullptr), prev(nullptr) {}
};

template <typename T>
class DoubleLinkedList
{
private:
    Node<T>* head;
public:
    DoubleLinkedList(): head(nullptr) {}
    ~DoubleLinkedList()
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

    Node<T>* GetHead()
    {
        return head;
    }

    void Append(Node<T>* node)
    {
        if (head == nullptr)        // head가 노드를 가리키고 있지 않음.
            head = node;            // head가 새 노드를 가리키게 함.
        else
        {
            Node<T>* cur = head, *prev = nullptr;
            while (cur != nullptr)
            {
                prev = cur;
                cur = cur->next;
            }
            prev->next = node;
            node->prev = prev;
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
            /*
            [A] <-> [B]
            ㄴ A -> B
            ㄴ A <- B
            =>
            [A] <-> [C] <-> [B]
            C -> B (c.next = a.next)
            A -> C (a.next = c)
            C <- B (b.prev = c)
            A <- C (c.prev = a)
            */
            n->next = p->next;     // 기존 노드의 다음 노드를 새 노드가 가리키게 한다.
            p->next = n;           // 기존 노드가 새 노드를 다음 노드로 가리키게 한다.
            n->prev = p;           // 새 노드가 이전 노드로 기존 노드를 가리키게 한다.
            n->next->prev = n;    // 기존 노드의 다음 노드가 이전 노드로 새 노드를  가리키게 한다.
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
            
            if (cur == nullptr)
                throw "Index out of range: list does not have enough elements.";
            
            Insert(cur, node);
        }
        else
            throw "Index out of range: head node is empty.";
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
                cur->next->prev = prev;
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

    void Debug()
    {
        int i = 0;
        for(Node<T>* cur = head; cur != nullptr; cur = cur->next, i++)
            cout << "Node[" << i <<  "] data=" << cur->data << " prev=" << cur->prev << " this=" << cur << " next=" << cur->next << endl;
        cout << endl;
    }
};

template <typename T>
void TestDoubleLinkedList(DoubleLinkedList<T> list)
{
    Node<T>* head = list.GetHead(), *node = head, *last = nullptr;
    while (true)
    {
        cout << node->data << " ";
        if (node->next == nullptr)
        {
            last = node;
            break;
        }
        node = node->next;
    }
    for (node = last; node != nullptr; node = node->prev)
        cout << node->data << " ";
    cout << endl;
}

int main(void)
{
    DoubleLinkedList<int> list;
    list.Append(1);
    list.Append(2);
    list.Append(3);
    // list.Debug();
    list.Display();
    
    list.Insert(1, 4);
    // list.Debug();
    list.Display();

    list.Delete(2);
    // list.Debug();
    list.Display();

    // list.Debug();
    TestDoubleLinkedList(list);
    return 0;
}