from sys import stdin

N = int(stdin.readline().strip())
cnt = 0


def isHansu(x: int) -> bool:
    """입력으로 받은 수가 한수인지 아닌지 판별한다.

    Args:
        x (int): 1 이상 N(<=1000) 이하의 정수

    Returns:
        bool: x가 한수이면 True, 아니면 False
    """
    if x < 100:     # 두 자리 이하의 수는 언제나 각 자리가 등차수열을 이룬다!
        return True
    else:
        x_str = str(x)
        diffs = []
        for i in range(1, len(x_str)):
            diffs.append(int(x_str[i]) - int(x_str[i - 1]))
        for i in range(1, len(diffs)):
            if diffs[i] != diffs[i - 1]:
                return False
        return True


for i in range(1, N + 1):
    if isHansu(i):
        cnt += 1

print(cnt)
