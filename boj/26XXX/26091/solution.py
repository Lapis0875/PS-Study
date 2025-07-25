input = open(0).readline
N, M = map(int, input().strip().split())
stats = sorted(map(int, input().strip().split()))

def solution():
    teams = 0
    prev_min = 0
    for i in range(N-1, -1, -1):  # 능력치가 높은 쪽에서부터 반복하면서
        j = prev_min    # 높은 쪽 능력치는 작아지므로, 낮은 쪽 능력치는 이전 능력치보다 높은 사람 중에서 골라야 한다.
        while stats[i] + stats[j] < M:
            j += 1
            if j >= N:
                break
        if j >= i:  # 탐색이 종료되는 경우: 오른쪽 포인터(작은쪽 능력치)가 왼쪽(i, 큰쪽 능력치)과 같아지거나 커질 때
            return teams

        if stats[i] + stats[j] >= M:
            teams += 1
        prev_min = j + 1
    return teams

print(solution())