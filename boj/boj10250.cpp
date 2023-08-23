#include <iostream>

using namespace std;

inline void hotel(int H, int W, int N)
{
    int idx = 1;
    for (int w = 1; w <= W; w++)
        for (int h = 1; h <= H; h++)
        {
            if (idx == N)
            {
                cout << h * 100 + w << endl;
                return;
            }
            idx++;
        }
}

int main(void)
{
    int case_size, h, w, n;
    cin >> case_size;

    for (int i = 0; i < case_size; i++)
    {
        cin >> h;
        cin >> w;
        cin >> n;
        hotel(h, w, n);
    }

    return 0;
}