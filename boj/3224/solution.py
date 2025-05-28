class Stack:
    """Fixed size stack implementation."""
    def __init__(self, max_size, default_value = 0):
        self.stack = [default_value for _ in range(max_size)]
        self.size = 0

    def push(self, item):
        if self.size + 1 > len(self.stack):
            raise OverflowError("push() to full stack")
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop() from empty stack")
        self.size -= 1
        return self.stack[self.size]

    def top(self):
        if self.size == 0:
            raise IndexError("top() from empty stack")
        return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.size = 0

input = open(0).readline
N = int(input())
numbers = [0 for _ in range(N)]
groups = [[0, 0] for _ in range(N)]
results = []

def merge_groups(idx1, idx2, min, max):
    """두 그룹을 병합하고 결과를 기록한다."""
    groups[idx1][0] = groups[idx2][0] = min
    groups[idx1][1] = groups[idx2][1] = max
    results.append(f"{min} {max}")
    # print(f">>> merge! ({min}, {max})")

# 초기 상태에는 모든 숫자가 각자 자신의 그룹에 속해 있다.
for idx, num in zip(range(N), map(int, input().split())):
    numbers[idx] = num
    groups[idx][0] = groups[idx][1] = num

stack = Stack(N, 0)
stack.push(0)   # 스택에 첫번째 원소의 인덱스를 넣는다.
for idx in range(1, N):   # 먼저 배열을 순회하며 가능한 만큼 병합하고 나머지는 스택에 쌓는다.
    while not stack.is_empty(): # 다음 원소가 현재 그룹과 연속되는 수인 경우 병합할 수 있다.
        min, max = groups[stack.top()]
        # print(f"comp ({numbers[stack.top()]}, {numbers[idx]})")
        # print(f"- stack.top(): [{min}, {max}]")
        # print(f"- from array: {groups[idx]}")
        if abs(min - groups[idx][0]) == 1 or abs(max - groups[idx][1]) == 1:
            if min > groups[idx][0]:
                min = groups[idx][0]
            if max < groups[idx][1]:
                max = groups[idx][1]
            prev = stack.pop()
            merge_groups(prev, idx, min, max)
        elif abs(min - groups[idx][1]) == 1:
            min = groups[idx][0]
            prev = stack.pop()
            merge_groups(prev, idx, min, max)
        elif abs(max - groups[idx][0]) == 1:
            max = groups[idx][1]
            prev = stack.pop()
            merge_groups(prev, idx, min, max)
        else:
            break
    # print(f">>> push! {numbers[idx]} ({groups[idx]})")
    stack.push(idx)

if stack.size > 1:
    print("NE")
else:
    print("DA")
    print("\n".join(map(str, results)))
