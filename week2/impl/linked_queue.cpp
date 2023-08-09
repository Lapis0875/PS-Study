#include <iostream>

using namespace std;

/**
 * @brief 연결 리스트 기반 큐 클래스.
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class Entry
{
public:
    T data;
    Entry<T>* next;
    Entry(T value): data(value), next(nullptr) {}
};

template <typename T>
class LinkedQueue
{
private:
    Entry<T>* front;
    Entry<T>* rear;
public:
    LinkedQueue(): front(nullptr), rear(nullptr) {}

    ~LinkedQueue()
    {
        Entry<T>* current = front, *next = nullptr;
        while (current != nullptr)
        {
            next = current->next;
            delete current;
            current = next;
        }
    }

    bool isEmpty()
    {
        return front == nullptr;
    }

    /**
     * @brief 큐에 새 요소를 추가한다.
     * 
     * @param v 새 요소.
     */
    void enqueue(T v)
    {
        Entry<T>* e = new Entry<T>(v);
        if (rear == nullptr)
        {
            front = rear = e;
        }
        else
        {
            rear->next = e;
            rear = e;
        }
    }

    /**
     * @brief 큐에서 요소를 하나 제거한다.
     * 
     * @return T 제거된 말단 요소.
     */
    T dequeue()
    {
        if (front == nullptr)
            throw "Queue is empty or corrupted.";
        
        Entry<T>* del = front;
        T data = del->data;
        front = front->next;
        delete del;

        if (front == nullptr)   // 마지막 요소를 삭제한 경우
            rear = nullptr;     // 후단 포인터도 null로 설정.

        return data;
    }
};

int main(void)
{
    const int queueSize = 10;
    LinkedQueue<int> queue;

    int i = 0;
    for (; i < queueSize; i++)
    {
        queue.enqueue(i);
    }

    i = 0;
    while (!queue.isEmpty())
    {
        printf("[%d] %d\n", i, queue.dequeue());
        i++;
    }
    return 0;
}