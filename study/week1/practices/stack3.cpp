#include <iostream>

using namespace std;

/**
 * @brief 배열로 구현한 스택
 */
class ArrayStack
{
private:
    int* arr;               // 스택의 요소들을 저장할 배열의 포인터.
    int top;                // 스택의 말단 요소의 인덱스.
    int capacity;           // 스택의 용량.
public:
    /**
     * @brief 스택의 생성자.
     * 
     * @param capacity 스택의 용량.
     */
    ArrayStack(int capacity): capacity(capacity), top(-1)
    {
        arr = new int[capacity];
    }

    /**
     * @brief 스택의 소멸자.
     */
    ~ArrayStack()
    {
        delete[] arr;
    }

    /**
     * @brief 스택이 비어있는지 확인한다.
     * 
     * @return true 스택이 비어있다.
     * @return false 스택이 비어있지 않다.
     */
    bool isEmpty()
    {
        return top == -1;
    }

    /**
     * @brief 스택에 새 요소를 추가한다.
     * 
     * @param e 새 요소.
     */
    void push(int e)
    {
        arr[++top] = e;
    }

    /**
     * @brief 스택의 말단 요소를 제거하고 반환한다.
     * 
     * @return int 스택의 말단 요소
     */
    int pop()
    {
        return isEmpty() ? -1 : arr[top--];
    }

    /**
     * @brief 스택의 말단 요소를 제거하지 않고 반환한다.
     * 
     * @return int 스택의 말단 요소
     */
    int peek()
    {
        return isEmpty() ? -1 : arr[top];
    }

    /**
     * @brief 스택의 크기를 반환한다.
     * 
     * @return int 스택의 요소 개수.
     */
    int size()
    {
        return top + 1;
    }
};

int main(void)
{
    int K, v;
    cin >> K;
    ArrayStack stack(K);

    for (int i = 0; i < K; i++)
    {
        cin >> v;
        if (v == 0)
            stack.pop();
        else
            stack.push(v);
    }

    int sum = 0, size = stack.size();

    for (int i = 0; i < size; i++)
        sum += stack.pop();
    cout << sum << '\n';
    return 0;
}