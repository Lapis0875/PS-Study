#include <iostream>
#define DEFAULT -1

using namespace std;

/**
 * @brief 정수 요소를 다루는 원형 큐 클래스.
 */
class CircularQueue
{
private:
    int* arr;
    int front;
    int rear;
    const int capacity;
public:
    CircularQueue(int capacity): capacity(capacity), front(0), rear(0)
    {
        arr = new int[capacity];
    }

    ~CircularQueue()
    {
        delete[] arr;
    }

    bool isEmpty()
    {
        return front == rear;
    }

    bool isFull()
    {
        return (rear + 1) % capacity == front;
    }

    int size()
    {
        return (rear - front + capacity) % capacity;
    }

    void push(int x)
    {
        if (isFull())
            return;     // 원형 큐는 꽉 찼을 때 더 이상 삽입할 수 없다.
        
        arr[rear] = x;
        rear = (rear + 1) % capacity;
    }

    int pop()
    {
        if (isEmpty())
            return DEFAULT;
        
        int e = arr[front];
        front = (front + 1) % capacity;
        return e;
    }

    int getFront()
    {
        return isEmpty() ? DEFAULT : arr[front];
    }

    int getRear()
    {
        return isEmpty() ? DEFAULT : arr[rear - 1];
    }
};

int main(void)
{
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int N, x;
    string cmd;

    cin >> N;
    CircularQueue q(N + 1);     // 원형 큐 구현상 배열의 인덱스 한칸은 사용하지 않는다.

    for (int i = 0; i < N; i++)
    {
        cin >> cmd;
        if (cmd == "push")
        {
            cin >> x;
            q.push(x);
        }
        else if (cmd == "pop")
        {
            cout << q.pop() << '\n';
        }
        else if (cmd == "size")
        {
            cout << q.size() << '\n';
        }
        else if (cmd == "empty")
        {
            cout << (q.isEmpty() ? "1\n" : "0\n");
        }
        else if (cmd == "front")
        {
            cout << q.getFront() << '\n';
        }
        else if (cmd == "back")
        {
            cout << q.getRear() << '\n';
        }
    }
    return 0;
}