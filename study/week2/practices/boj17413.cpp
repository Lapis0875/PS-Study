#include <iostream>

using namespace std;

class Character
{
public:
    char data;
    Character* prev;
    Character(char data): data(data), prev(nullptr) {}
};

class CharStack
{
private:
    Character* top;
public:
    CharStack(): top(nullptr) {}
    ~CharStack()
    {
        empty();
    }

    bool isEmpty()
    {
        return top == nullptr;
    }

    void empty()
    {
        Character *current = top, *prev = nullptr;
        while (current != nullptr)
        {
            prev = current->prev;
            delete current;
            current = prev;
        }
    }

    void push(char c)
    {
        Character* entry = new Character(c);
        entry->prev = top;
        top = entry;
    }

    char pop()
    {
        Character* entry = top;
        char d = entry->data;
        top = top->prev;
        delete entry;
        return d;
    }
};

int main(void)
{
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    string str;
    char c;
    bool inTag = false;
    CharStack word;
    getline(cin, str);

    for (int i = 0; i < str.size(); i++)
    {
        c = str[i];
        if (inTag)
        {
            if (c == '>')
            {
                inTag = false;
            }
            
            cout << c;
        }
        else
        {
            if (c == '<')
            {
                inTag = true;
                while (!word.isEmpty())
                {
                    cout << word.pop();
                }
                cout << c;
            }
            else if (c == ' ')
            {
                while (!word.isEmpty())
                {
                    cout << word.pop();
                }
                cout << c;
            }
            else
            {
                word.push(c);
            }
        }
    }
    while (!word.isEmpty())
    {
        cout << word.pop();
    }
    cout << '\n';

    return 0;
}