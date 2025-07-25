#include <bits/stdc++.h>
using namespace std;

int cnt;        // 호출 횟수를 세는 변수. 각각의 case마다 0으로 초기화 후 recursion 호출마다 1씩 증가한다.
string s;       // 회문인지 판단할 문자열을 저장하는 변수. getline()의 편의상 string으로 선언 후 사용한다.

/**
 * @brief 재귀를 이용해 회문인지 판단한다.
 * 
 * @param s 
 * @param l 
 * @param r 
 * @return int 
 */
int recursion(string& s, int l, int r) {
    cnt += 1;
    if (l >= r)
        return 1;
    else if (s[l] != s[r])
        return 0;
    else
        return recursion(s, l+1, r-1);
}

int isPalindrome(string& s) {
    return recursion(s, 0, s.length()-1);
}

int main(){
    int T;
    scanf("%d\n", &T);
    for (int i = 0; i < T; i++)
    {
        getline(cin, s);
        #ifdef DEBUG
            printf("[i=%d] s: %s\n", i, s.c_str());
        #endif
        int res = isPalindrome(s);
        printf("%d %d\n", res, cnt);
        cnt = 0;
    }
}