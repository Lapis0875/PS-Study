#include <iostream>

using namespace std;

class Entry
{
public:
    int data;
    Entry* prev;
    Entry* next;
    Entry(int data): data(data), prev(nullptr), next(nullptr) {}
};

class LinkedDeque
{
private:
    Entry* front;
    Entry* rear;
public:
    int size;
    LinkedDeque(): front(nullptr), rear(nullptr), size(0) {}
    ~LinkedDeque()
    {
        Entry* cur = front, *next = nullptr;
        while (cur != nullptr)
        {
            next = cur->next;
            delete cur;
            cur = next;
        }
    }

    bool isEmpty()
    {
        return size == 0;
    }

    void push_front(int x)
    {
        Entry* e = new Entry(x);
        if (isEmpty())
        {
            front = e;
            rear = e;
        }
        else
        {
            front->prev = e;
            e->next = front;
            front = e;
        }
        size++;
    }

    void push_back(int x)
    {
        Entry* e = new Entry(x);
        if (isEmpty())
        {
            front = e;
            rear = e;
        }
        else
        {
            rear->next = e;
            e->prev = rear;
            rear = e;
        }
        size++;
    }

    int pop_front()
    {
        if (isEmpty())
            return -1;
        
        Entry* e = front;
        int d = front->data;
        front = front->next;

        if (front != nullptr)
            front->prev = nullptr;
        else
            rear = nullptr;
        
        delete e;
        --size;

        return d;
    }

    int pop_back()
    {
        if (isEmpty())
            return -1;
        
        Entry* e = rear;
        int d = rear->data;
        rear = rear->prev;

        if (rear != nullptr)
            rear->next = nullptr;
        else
            front = nullptr;
        delete e;
        --size;

        return d;
    }

    int peek_front()
    {
        return isEmpty() ? -1 : front->data;
    }

    int peek_back()
    {
        return isEmpty() ? -1 : rear->data;
    }
};

/**
 * @brief main 함수.
 * 빠른 입출력을 위해 cin, cout 대신 scanf, getchar, printf를 사용했다.
 * 
 * @return int 
 */
int main(void)
{
    int N, x;
    char cmd_raw[11];
    string cmd;
    scanf("%d", &N);
    getchar();              // 개행문자 비우기
    LinkedDeque deque;

    for (int i = 0; i < N; i++)
    {
        scanf("%s", cmd_raw);
        cmd = string(cmd_raw);
        if (cmd == "push_front")
        {
            scanf("%d", &x);
            deque.push_front(x);
        }
        else if (cmd == "push_back")
        {
            scanf("%d", &x);
            deque.push_back(x);
        }
        else if (cmd == "pop_front")
            printf("%d\n", deque.pop_front());
        else if (cmd == "pop_back")
            printf("%d\n", deque.pop_back());
        else if (cmd == "front")
            printf("%d\n", deque.peek_front());
        else if (cmd == "back")
            printf("%d\n", deque.peek_back());
        else if (cmd == "empty")
            printf("%c\n", deque.isEmpty() ? '1' : '0');
        else if (cmd == "size")
            printf("%d\n", deque.size);
    }
    return 0;
}