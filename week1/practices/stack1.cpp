#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

class Char
{
public:
    char data;
    Char* prev;
    Char(char data): data(data), prev(nullptr) {}
};

class LinkedStack
{
private:
    Char* top;
    int size;
public:
    LinkedStack(): top(nullptr), size(0) {}
    ~LinkedStack()
    {
        Char* cur = top, *below = nullptr;
        while (cur != nullptr)
        {
            below = cur->prev;
            delete cur;
            cur = below;
        }
    }

    void push(char e)
    {
        Char* elem = new Char(e);
        elem->prev = top;
        top = elem;
        size++;
    }

    char pop()
    {
        Char* e = top;

        if (e == nullptr)
            return -1;
        size--;
        char d = e->data;
        top = top->prev;
        delete e;
        return d;
    }

    string* flatten()
    {
        char c = pop(), arr[size];
        int i = 0;
        while (c != -1)
        {
            arr[i] = c;

            // increment
            c = pop();
            i++;
        }
        return new string(arr);
    }
};

int main(void)
{

    string text;
    getline(cin, text);
    LinkedStack stack;

    for (int i = 0; i < text.size(); i++)
        stack.push(text[i]);
    
    puts(stack.flatten()->append("\n").c_str());        // 뒤집어진 문자열 뒤에 개행문자 붙이고 puts()에 쓰기 위해 char*로 변경.

    return 0;
}