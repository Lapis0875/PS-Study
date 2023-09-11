#include <iostream>

using namespace std;

/**
 * @brief 배열 기반 큐 클래스.
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class ArrayQueue
{
private:
    T* arr;
    int front;
    int rear;
    int capacity;
public:
    ArrayQueue(int capacity): capacity(capacity), front(-1), rear(-1)
    {
        arr = new T[capacity];
    }

    ~ArrayQueue()
    {
        delete[] arr;
    }

    /**
     * @brief 큐가 가득 찼는지 검사한다.
     * 
     * @return true 큐가 가득 찼거나 배열을 벗어난 경우
     * @return false 아직 큐에 더 저장할 수 있는 경우우
     */
    bool isFull()
    {
        return rear >= capacity - 1;
    }

    /**
     * @brief 큐가 비어있는지 검사한다.
     * 
     * @return true 시작 인덱스와 끝 인덱스 같은 경우 (큐에 요소가 없다).
     * @return false 큐에 요소가 하나라도 있는 경우.
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
        arr[++rear] = e;
    }

    /**
     * @brief 큐에서 요소를 하나 제거한다.
     * 
     * @return T 제거된 전단 요소
     */
    T dequeue()
    {
        if (isEmpty())
            throw "Queue is empty";
        return arr[++front];
    }
};

int main(void)
{
    const int queueSize = 10;
    ArrayQueue<int> queue(queueSize);

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