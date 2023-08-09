#include <iostream>

using namespace std;

/**
 * @brief 스택의 요소를 저장할 노드 클래스.
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class Element
{
public:
    T data;
    Element<T>* prev;
    Element(T data): data(data), prev(nullptr) {}
};

/**
 * @brief 연결 리스트로 구현한 스택
 * 
 * @tparam T 요소의 타입.
 */
template <typename T>
class LinkedStack
{
private:
    Element<T>* top;
public:
    LinkedStack(): top(nullptr) {}
    ~LinkedStack()
    {
        Element<T>* cur = top, *below = nullptr;
        while (cur != nullptr)          // 현재 노드가 nullptr이 될 때 까지 반복.
        {
            below = cur->prev;          // 다음 노드를 미리 저장.
            delete cur;                 // 현재 노드 삭제.
            cur = below;                // cur에 다음 노드 주소 저장.
        }

    }

    /**
     * @brief 스택에 새 요소를 삽입한다.
     * 
     * @param e 새 요소
     */
    void push(T e)
    {
        Element<T>* elem = new Element<T>(e);
        elem->prev = top;
        top = elem;
    }

    /**
     * @brief 스택의 말단 요소를 제거하고 반환한다.
     * 
     * @return T 스택의 말단 요소.
     */
    T pop()
    {
        Element<T>* e = top;
        T data = e->data;
        top = e->prev;
        delete e;
        return data;
    }

    /**
     * @brief 스택의 말단 요소를 제거하지 않고 반환한다.
     * 
     * @return T 스택의 말단 요소.
     */
    T peek()
    {
        return top->data;
    }

    bool isEmpty()
    {
        return top == nullptr;
    }
};

int main(void)
{
    LinkedStack<int> stack;

    for (int i = 0; i < 10; i++)
        stack.push(i);
    
    for (int i = 0; i < 10; i++)
        cout << stack.pop() << endl;

    return 0;
}