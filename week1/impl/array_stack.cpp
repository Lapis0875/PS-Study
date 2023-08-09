#include <iostream>

using namespace std;

/**
 * @brief 배열로 구현한 스택 클래스
 * 
 * @tparam T 스택의 요소 타입
 */
template <typename T>
class ArrayStack
{
private:
    T* arr;             // 스택이 요소를 저장할 내부 배열
    int capacity;       // 스택의 용량
    int top;            // 스택의 말단 요소의 인덱스. -1이면 스택이 비어있음을 의미.
public:
    /**
     * @brief 배열에 기반한 스택을 생성한다.
     * 
     * @param capacity 스택에 사용될 배열의 크기.
     */
    ArrayStack(int capacity) {
        this->capacity = capacity;          // 용량 저장
        this->arr = new T[capacity];        // 배열 생성
        this->top = -1;                     // 초기값은 -1.
    }

    /**
     * @brief 스택의 소멸자. 동적할당한 배열을 해제한다.
     */
    ~ArrayStack() {
        delete[] this->arr;
    }

    /**
     * @brief 스택에 새 요소를 추가한다.
     * 
     * @param e 새 요소
     */
    void push(T e)
    {
        this->arr[++top] = e;
    }

    /**
     * @brief 스택의 말단 요소를 제거한다.
     * 
     * @return T 제거된 말단 요소.
     */
    T pop()
    {
        return this->arr[top--];
    }
    
    /**
     * @brief 스택의 말단 요소를 제거하지 않고 반환한다.
     * 
     * @return T 스택의 말단 요소.
     */
    T peek()
    {
        return this->arr[top];
    }

    /**
     * @brief 스택이 비어있는지 확인한다.
     * 
     * @return true 비어있다.
     * @return false 비어있지 않다.
     */
    bool isEmpty()
    {
        return top == -1;
    }

    /**
     * @brief 스택이 가득 찼는지 확인한다.
     * 
     * @return true 가득 찼다.
     * @return false 여유가 있다.
     */
    bool isFull()
    {
        return top == capacity - 1;
    }
};

int main(void)
{
    const int size = 10;
    ArrayStack<int> stack(size);

    for (int i = 0; i < size; i++)
        stack.push(i);

    for (int i = 0; i < size; i++)
        cout << stack.pop() << endl;
    return 0;
}