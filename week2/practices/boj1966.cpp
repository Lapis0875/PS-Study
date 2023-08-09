#include <iostream>
#include <list>

using namespace std;

class Document
{
public:
    int index;
    int priority;
    Document(int index, int priority): index(index), priority(priority) {}
};

/**
 * @brief 현재 프린터 큐와, 찾고자 하는 문서의 인덱스를 받아 해당 프린터 큐에 대해 문제를 푼다.
 * 
 * @param q 현재 프린터 큐를 나타내는 list<Document> 객체.
 * @param M 몇 번째에 출력되는지 알고 싶은 문서의 인덱스.
 * @return int @a M번째 문서가 몇 번째에 출력되는지 반환한다.
 */
int solve(list<Document> q, int M)
{
    int curPriority, count = 0;     // curPriority는 현재 큐의 앞에 위치한 문서의 중요도. count는 찾고자 하는 문서의 출력 순서를 기록하는 변수.
    bool popDoc;                    // 큐의 첫번째에 위치한 문서가 재배치 되었는가? 를 나타내는 flag 변수.

    while (!q.empty())
    {
        curPriority = q.front().priority;
        popDoc = false;
        /*
            C++ stl에서 사용할 수 있는 iterator 구문. 익혀두자.
            list<T>::iterater iter : T 타입의 요소를 가지는 list의 iterator 타입.
            iterator 타입의 객체는 ++ 연산으로 뒤로 이동 가능.
            동등비교 (==)로 타 iterator와 비교할 수 있어, list<T>::end()로 얻은 iterator와 비교해 같을때까지 반복하면 된다.
        */
        for(list<Document>::iterator iter = q.begin(); iter != q.end(); iter++)
        {
            if (iter->priority > curPriority)
            {
                q.push_back(q.front());
                q.pop_front();
                popDoc = true;
                break;
            }
        }

        if (!popDoc)                    // 앞 문서의 재배치가 이루어지지 않은 반복에만
        {
            count++;                    // 찾고자 하는 문서의 출력 순서 증가.
            if (q.front().index == M)   // 만약 찾고자 하는 문서가 출력될 차례라면,
                return count;           // 순서 반환.
            q.pop_front();              // 그렇지 않으면, 해당 문서를 출력 후 앞의 과정 반복.
        }
    }
    return -1;                          // 도달할 리 없으나, 올바른 함수 구성을 위해 기본 반환값으로 둔다.
}

int main(void)
{
    int T, N, M, p;
    list<Document> q;                   // list<T> stl을 사용한다.

    scanf("%d\n", &T);                  // 테스트 케이스 수 입력.
    for (int i = 0; i < T; i++)
    {
        scanf("%d %d\n", &N, &M);       // 문서의 수와 찾고자 하는 문서의 인덱스 입력.
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &p);            // 각 문서의 중요도 입력.
            q.push_back(Document(j, p));    // 리스트에 문서 추가.
        }
        printf("%d\n", solve(q, M));    // 각 케이스의 실행 결과를 출력.
        q.clear();
    }
    return 0;
}