#include <iostream>
#define PUSH '+'
#define POP '-'

using namespace std;

class ArrayStack
{
private:
    int* arr;
    int top;
    int capacity;
public:
    ArrayStack(int capacity): capacity(capacity), top(-1)
    {
        arr = new int[capacity];
    }
    
    ~ArrayStack()
    {
        delete[] arr;
    }

    void push(int e)
    {
        arr[++top] = e;
    }

    int pop()
    {
        return arr[top--];
    }

    int peek()
    {
        return arr[top];
    }

    bool isEmpty()
    {
        return top == -1;
    }
};

int main(void)
{
    int N, v;
    cin >> N;
    
    int* ascending = new int[N];
    int* target = new int[N];
    int* res = new int[N];
    char* action = new char[2 * N];
    ArrayStack stack(N);

    for (int i = 0; i < N; i++)
        ascending[i] = i + 1;
    
    for (int i = 0; i < N; i++)
        cin >> target[i];

    int ai = 0, i = 0, ri = 0;
    for (; i < N; i++)
    {
        #ifdef DEBUG
        cout << "ascending[" << ai << "] = " << ascending[ai] << ',';
        cout << "target[" << i << "] = " << target[i] << '\n';
        
        cout << ">>> check if unreachable number in target...\n";
        #endif
        if (ascending[ai] > target[i])
        {
            cout << "NO\n";
            return 0;
        }

        #ifdef DEBUG
        cout << ">>> check if target number is larger then current ascending number...\n";
        #endif
        if (ascending[ai] < target[i])
        {
            for (;ascending[ai] != target[i];ai++)
            {
                stack.push(ascending[ai]);
                action[ai] = PUSH;
            }
            ai--;
        }

        #ifdef DEBUG
        cout << ">>> check if target number is eqaul to current ascending number...\n";
        #endif
        if (ascending[i] == target[i])
        {
            res[ri++] = stack.pop();
            action[ai++] = POP;
        }
    }
    
    #ifdef DEBUG
    cout << ">>> flush remaining numbers in stack...\n";
    #endif
    while (!stack.isEmpty())
    {
        res[ri++] = stack.pop();
        action[ai++] = POP;
    }

    for(int i = 0; i < N; i++)
    {
        if (target[i] != res[i])
        {
            cout << "NO\n";
            return 0;
        }
    }
    for (int i = 0; i < N; i++)
        cout << action[i] << '\n';

    return 0;
}