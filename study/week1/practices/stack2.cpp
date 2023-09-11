#include <iostream>

using namespace std;

/**
 * @brief 배열 기반의 스택
 */
class ArrayStack
{
private:
    int* arr;               // 스택의 요소를 저장할 배열.
    int top;                // 스택의 말단 요소의 인덱스.
    int capacity;           // 스택의 총 용량. arr이 가리키는 배열의 크기와 같다.
public:
    /**
     * @brief 스택을 생성한다.
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
     * @return int 스택의 말단 요소.
     */
    int pop()
    {
        return top > -1 ? arr[top--] : -1;
    }


    /**
     * @brief 스택의 말단 요소를 제거하지 않고 반환한다.
     * 
     * @return int 스택의 말단 요소.
     */
    int peek()
    {
        return top > -1 ? arr[top] : -1;
    }

    /**
     * @brief 스택의 크기를 반환한다.
     * 
     * @return int 스택의 크기.
     */
    int size()
    {
        return top + 1;
    }

    /**
     * @brief 스택이 비어있는지 확인한다.
     * 
     * @return true 스택이 비어있다.
     * @return false 스택에 요소가 존재한다.
     */
    bool isEmpty()
    {
        return top == -1;
    }
};

/**
 * @brief 메인 함수.
 * 
 * @return int 종료 코드.
 */
int main(void)
{
    // PS용 cin, cout 최적화.
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N, value;               // 변수 선언.
    cin >> N;                   // 총 명령어 개수 입력.
    ArrayStack stack(N);        // 스택 생성.
    string cmd;                 // 명령어 입력받을 변수 선언.

    for (int i = 0; i < N; i++)
    {
        cin >> cmd;                         // 명령어 입력.

        // 명령어에 따라 작업 수행.
        if (cmd == "push")                  // push X
        {
            cin >> value;                   // X 입력.
            stack.push(value);              // 스택에 푸시한다.
        }
        else if (cmd == "pop")              // pop
        {
            cout << stack.pop() << '\n';    // 스택을 pop하고 반환값을 출력한다.
        }
        else if (cmd == "size")             // size
        {
            cout << stack.size() << '\n';   // 스택의 크기를 출력한다.
        }
        else if (cmd == "empty")            // empty
        {
            cout << (stack.isEmpty() ? 1 : 0) << '\n';  // 스택이 비어있으면 1, 아니면 0을 출력한다.
        }
        else if (cmd == "top")              // top
        {
            cout << stack.peek() << '\n';   // 스택을 peek하고 반환값을 출력한다.
        }
    }
    return 0;
}