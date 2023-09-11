#include <iostream>
#include <stack>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int N;
    char c;
    string text;
    stack<char> stk;

    cin >> N;
    cin.ignore();
    for (int i = 0; i < N; i++)
    {
        getline(cin, text);
        for (int j = 0; j < text.length(); j++)
        {
            c = text[j];
            if (c == ' ')
            {
                while (!stk.empty())
                {
                    cout << stk.top();
                    stk.pop();
                }
                cout << ' ';
            }
            else
                stk.push(c);
        }
        while (!stk.empty())
        {
            cout << stk.top();
            stk.pop();
        }
        cout << '\n';
    }

    return 0;
}