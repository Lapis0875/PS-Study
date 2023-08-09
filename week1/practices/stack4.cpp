#include <iostream>

/**
 * @brief 괄호를 저장할 스택의 노드 클래스
 */
class Parentheses
{
public:
    char data;
    Parentheses* prev;
    Parentheses(char data): data(data), prev(nullptr) {}
};

/**
 * @brief 괄호를 저장할 연결 리스트 기반 스택
 */
class LinkedStack
{
private:
    Parentheses* top;
public:
    /**
     * @brief 스택의 생성자.
     */
    LinkedStack(): top(nullptr) {}
    
    /**
     * @brief 스택의 소멸자.
     * 
     */
    ~LinkedStack()
    {
        empty();
    }

    /**
     * @brief 스택이 비어있는지 확인합니다.
     * 
     * @return true 스택이 비어있습니다.
     * @return false 스택이 비어있지 않습니다.
     */
    bool isEmpty()
    {
        return top == nullptr;
    }

    /**
     * @brief 스택에 새 요소를 추가합니다.
     * 
     * @param p 새 요소. '(' 나 ')' 중 하나입니다.
     */
    void push(char p)
    {
        Parentheses* elem = new Parentheses(p);
        elem->prev = top;
        top = elem;
    }

    /**
     * @brief 스택의 말단 요소를 제거하고 반환합니다.
     * 
     * @return char 말단 요소. '(' 나 ')' 중 하나입니다.
     */
    char pop()
    {
        Parentheses* e = top;

        if (isEmpty())
            return -1;
        char d = e->data;
        top = top->prev;
        delete e;
        return d;
    }

    /**
     * @brief 스택의 말단 요소를 제거하지 않고 반환합니다.
     * 
     * @return char 말단 요소. '(' 나 ')' 중 하나입니다.
     */
    char peek()
    {
        return isEmpty() ? -1 : top->data;
    }

    /**
     * @brief 현재 스택을 비웁니다.
     */
    void empty()
    {
        while (top != nullptr)
        {
            pop();
        }
    }
};

using namespace std;

int main(void)
{
    int T;
    cin >> T;                                               // 검사할 괄호 문자열의 개수 입력.
    string str;                                             // 문자열 입력받을 변수 선언.
    LinkedStack stack;                                      // 스택 생성.
    for (int i = 0; i < T; i++)
    {
        cin >> str;                                         // 문자열 입력. (괄호 문자열)
        
        char c = str[0];
        for (int i = 0; i < str.size(); i++, c = str[i])    // 스택 문자열 순회하며 검사.
        {
            if (stack.isEmpty())                            // 스택이 비었을 경우, 요소 추가.
                stack.push(c);
            else if (stack.peek() == '(' && c == ')')       // 스택에 '(' 가 있고, 현재 문자가 ')' 일 경우, '(' 제거.
                stack.pop();
            else
                stack.push(c);                              // 스택에 요소 추가.
        }
        cout << (stack.isEmpty() ? "YES" : "NO") << '\n';   // 스택에 요소가 남아있을 경우, 잘못된 괄호 문자열.
        stack.empty();                                      // 다음 검사를 위해 스택을 비운다.
    }
    return 0;
}