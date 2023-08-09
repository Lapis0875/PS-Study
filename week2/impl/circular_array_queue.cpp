#include <iostream>

using namespace std;

/**
 * @brief 원형 큐 클래스.
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class CircularQueue
{
private:
    T* arr;
    int front;
    int rear;
    int capacity;
public:
    CircularQueue(int capacity): capacity(capacity), front(0), rear(0)
    {
        arr = new T[capacity];
    }

    ~CircularQueue()
    {
        delete[] arr;
    }

    /**
     * @brief 큐가 가득 찼는지 검사한다.
     * 
     * @return true 큐가 가득찼다. (다음 rear 인덱스가 현재 front의 인덱스와 같을 때)
     * @return false 큐에 아직 여백이 있다.
     */
    bool isFull()
    {
        // 증가한 rear가 front와 같아질 경우 큐가 가득 찬 것으로 간주한다.
        // 이렇게 비교할 경우, 실제 배열에서 한 칸은 구현상 비워두게 된다.
        // 하지만 구현의 편의를 위해 이렇게 하자..
        return (rear + 1) % capacity == front;
    }

    /**
     * @brief 큐가 비어있는지 검사한다.
     * 
     * @return true 큐가 비어있다. (front == rear)
     * @return false 큐가 비어있지 않다.
     */
    bool isEmpty()
    {
        return front == rear;
    }

    /**
     * @brief 큐에 새 요소를 추가한다.
     * 
     * @param e 새 요소
     */
    void enqueue(T e)
    {
        if (isFull())
            throw "Queue is full";
        
        arr[rear] = e;
        rear = (rear + 1) % capacity;
        cout << "rear = " << rear << ", front = " << front << (!isFull() ? ": queue has spaces" : ": queue is full") << endl;
    }

    /**
     * @brief 큐에서 요소를 제거한다.
     * 
     * @return T 제거된 전단 요소.
     */
    T dequeue()
    {
        if (isEmpty())
            throw "Queue is empty";
        int entry = arr[front];
        front = (front + 1) % capacity;
        return entry;
    }

    /**
     * @brief 큐의 요소의 개수를 센다.
     * 
     * @return int 큐의 요소 개수
     */
    int count()
    {
        return ( ( rear - front ) + capacity ) % capacity;
    }
};

int main(void)
{
    const int queueSize = 10;
    CircularQueue<int> queue(queueSize);

    int i = 0;
    while (!queue.isFull())
    {
        queue.enqueue(i);
        i++;
    }

    cout << "queue entry count: " << queue.count() << endl;

    i = 0;
    while (!queue.isEmpty())
    {
        printf("[%d] %d\n", i, queue.dequeue());
        i++;
    }
    return 0;
}