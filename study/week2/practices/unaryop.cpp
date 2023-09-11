#include <iostream>

using namespace std;

int main(void)
{
    int a = 0, b = 0, c = 0;

    c = --a + --b;          // a += 1, b += 1, c = 1 + 1

    // [0] ()
    // [1] a++, a--
    // [2] ++a, --a
    // ...
    // + - * /

    cout << "c: " << c << endl;
    cout << "a: " << a << endl;
    cout << "b: " << b << endl;

    return 0;
}