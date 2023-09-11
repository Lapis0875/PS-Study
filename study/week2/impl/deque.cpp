#include <iostream>

using namespace std;

/**
 * @brief 덱의 노드 클래스.
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class Node
{
public:
    T data;
    Node<T>* prev;
    Node<T>* next;
    Node(T value): data(value), prev(nullptr), next(nullptr) {}
};

/**
 * @brief 덱 클래스.
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class Deque
{
private:
    Node<T>* front;
    Node<T>* rear;
public:
    Deque(): front(nullptr), rear(nullptr) {}

    ~Deque()
    {
        Node<T>* current = front, *next = nullptr;
        while (current != nullptr)
        {
            next = current->next;
            delete current;
            current = next;
        }
    }

    bool isEmpty()
    {
        return front == nullptr || rear == nullptr;
    }

    void insertFront(T v)
    {
        Node<T>* entry = new Node<T>(v);
        if (isEmpty())
        {
            front = entry;
            rear = entry;
        }
        else
        {
            front->prev = entry;
            entry->next = front;
            front = entry;
        }
    }

    void insertRear(T v)
    {
        Node<T>* entry = new Node<T>(v);
        if (isEmpty())
        {
            front = entry;
            rear = entry;
        }
        else
        {
            rear->next = entry;
            entry->prev = rear;
            rear = entry;
        }
    }

    T removeFront()
    {
        if (isEmpty())
            throw "Deque is empty";
        
        Node<T>* entry = front;

        printf("removeFront() : entry = Node<int>(%d) : %p\n\n", entry->data, entry);

        T data = entry->data;
        front = front->next;

        if (front != nullptr)
            front->prev = nullptr;
        else    // 마지막 요소를 제거한 경우
            rear = nullptr;
        delete entry;

        printf("removeFront() : new front = Node<int>(%d) : %p\n\n", front->data, front);

        return data;
    }

    T removeRear()
    {
        if (isEmpty())
            throw "Deque is empty";
        
        Node<T>* entry = rear;

        printf("removeRear() : entry = Node<int>(%d) : %p\n\n", entry->data, entry);

        T data = entry->data;

        data == 3 && cout << "- removeRear() : data retrieved.\n" << endl;

        rear = rear->prev;

        data == 3 && cout << "- removeRear() : new rear retrieved.\n" << endl;

        if (rear != nullptr)
            rear->next = nullptr;
        else    // 마지막 요소를 제거한 경우
            front = nullptr;

        data == 3 && cout << "- removeRear() : handle rear adjustment.\n" << endl;

        delete entry;

        printf("removeRear() : new rear = Node<int>(%d) : %p\n\n", rear->data, rear);
        
        return data;
    }

    T peekFront()
    {
        if (isEmpty())
            throw "Deque is empty";
        
        return front->data;
    }

    T peekRear()
    {
        if (isEmpty())
            throw "Deque is empty";
        
        return rear->data;
    }

    void debugDeque()
    {
        Node<T>* current = front;
        while (current != nullptr)
        {
            printf("Node<int>(%d) : %p\n", current->data, current);
            current = current->next;
        }
        cout << endl;
    }
};

int main(void)
{
    Deque<int> deque;
    int N, v;

    cout << "Enter the number of elements: " << endl;;
    cin >> N;

    cout << "Enter " << N << " elements: " << endl;;
    for (int i = 0; i < N; i++)
    {
        cin >> v;
        deque.insertRear(v);
    }
    deque.debugDeque();
    cout << "Select print mode:\n";
    cout << "1. FIFO (Queue)\n";
    cout << "2. LIFO (Stack)\n";
    cout << "3. Shuffle (front-rear-front-rear-...)" << endl;
    cin >> v;
    switch (v)
    {
    case 1:
        while (!deque.isEmpty())
            cout << deque.removeFront() << " ";
        cout << endl;
        break;
    case 2:
        while (!deque.isEmpty())
            cout << deque.removeRear() << " ";
        cout << endl;
        break;
    case 3:
        for (int i = 0; !deque.isEmpty(); i++)
        {
            if (i % 2)
                cout << deque.removeRear() << " ";
            else
                cout << deque.removeFront() << " ";
        }
        cout << endl;
        break;
    }

    return 0;
}