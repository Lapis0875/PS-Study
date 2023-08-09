#include <iostream>

using namespace std;

/**
 * @brief 스택의 각 요소를 저장할 노드.
 * 
 */
class Element
{
public:
    char data;
    Element* prev;
    Element(char data): data(data), prev(nullptr) {}
};

/**
 * @brief 연결 리스트 기반 스택.
 */
class LinkedStack
{
private:
    Element* top;
public:
    /**
     * @brief 생성자.
     */
    LinkedStack() : top(nullptr) {}

    ~LinkedStack()
    {
        empty();
    }

    /**
     * @brief 스택이 비어있는지 검사한다.
     * 
     * @return true 스택이 비어있다.
     * @return false 스택이 비어있지 않다.
     */
    bool isEmpty()
    {
        return top == nullptr;
    }

    /**
     * @brief 스택에 새 요소를 추가한다.
     * 
     * @param c 새 요소.
     */
    void push(char c)
    {
        Element* elem = new Element(c);
        elem->prev = top;
        top = elem;
    }

    /**
     * @brief 스택의 말단 요소를 제거하고 반환한다.
     * 
     * @return char 스택의 말단 요소.
     */
    char pop()
    {
        if (isEmpty())
            return -1;

        Element* e = top;
        char c = top->data;
        top = top->prev;

        delete e;
        return c;
    }

    /**
     * @brief 스택의 말단 요소를 제거하지 않고 반환한다.
     * 
     * @return char 스택의 말단 요소.
     */
    char peek()
    {
        return isEmpty() ? -1 : top->data;
    }

    /**
     * @brief 현재 스택을 비운다.
     */
    void empty()
    {
        while (top != nullptr)
        {
            pop();
        }
    }
};

int main(void)
{
    string str;
    LinkedStack stack;

    while (true)
    {
        getline(cin, str);

        if (str == ".")
            break;

        int i = 0;
        for (char c = str[0]; i < str.find_first_of("."); c = str[++i])
        {
            if (c == '(' || c == '[')       // 여는 괄호일 경우, 스택에 추가.
            {
                stack.push(c);
            }
            else if (c == ')')              // 닫는 괄호일 경우,
            {
                if (stack.peek() == '(')    // 대응하는 괄호 쌍을 스택에서 찾아보고
                    stack.pop();            // 있을경우 제거.
                else
                    stack.push(c);          // 없을 경우 닫는 괄호를 스택에 추가. (올바르지 않은 괄호 문자열로 판정.)
            }
            else if (c == ']')              // 대응하는 괄호 쌍을 스택에서 찾아보고~ (이하동일).
            {
                if (stack.peek() == '[')
                    stack.pop();
                else
                    stack.push(c);
            }
        }
        cout << (stack.isEmpty() ? "yes\n" : "no\n");       // 스택이 비어있어야 올바른 괄호 문자열.
        stack.empty();
    }

    return 0;
}