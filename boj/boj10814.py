from sys import stdin
from typing import Final


N: Final[int] = int(stdin.readline())

def parseUser(s: str) -> tuple[int, str]:
    age, name = s.split()
    return int(age), name

def mergeSort(array: list[tuple[int, str]], start: int, end: int):
    if (start < end):
        mid: int = (start + end) // 2
        
        mergeSort(array, start, mid)
        mergeSort(array, mid + 1, end)
        
        # print(f">>> Before ({start} ~ {end}):\n{', '.join(map(lambda user: f'<{user[0]} {user[1]}>', array[start:end+1]))}")
        merge(array, start, mid, end)
        # print(f">>> After ({start} ~ {end}):\n{', '.join(map(lambda user: f'<{user[0]} {user[1]}>', array[start:end+1]))}")

def merge(array: list[tuple[int, str]], start: int, middle: int, end: int):
    temp: list[tuple[int, str]] = []
    l: int = start
    r: int = middle + 1
    
    if (end - start < 2):   # 단순 교환으로 해결 가능한 첫 번째 정복 단계 처리
        # print(array[start:end+1])
        if (array[start][0] > array[end][0]):
            temp.append(array[end])
            temp.append(array[start])
        else:
            temp.append(array[start])
            temp.append(array[end])
        # print(f"=> temp : {temp}")
    else:
        while l <= middle and r <= end:
            if (array[l][0] <= array[r][0]):
                temp.append(array[l])
                l += 1
            else:
                temp.append(array[r])
                r += 1
        # 위에서 병합하고 남은 원소들을 임시배열에 모두 넣어준다. 왼쪽 또는 오른쪽 중 하나는 반드시 위 반복문에서 비워지기 때문이다.
        while (l <= middle):
            temp.append(array[l])
            l += 1
        while (r <= middle):
            temp.append(array[r])
            r += 1
        
    for i, t in zip(range(start, end + 1), temp):
        # print(f"merge({start}, {middle}, {end}) : i = {i}, t = {t}")
        array[i] = t
    # print("\n" * 2)

users: list[tuple[int, str]] = [parseUser(stdin.readline()) for _ in range(N)]

mergeSort(users, 0, N - 1)

for user in users:
    print(user[0], user[1])