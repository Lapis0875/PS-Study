from sys import stdin
from collections import deque

N = int(stdin.readline())
queries = stdin.readlines()

waiting = deque()    # 대기줄에 있는 학생들
A = deque()          # 원하는 음식을 먹은 학생들
B = deque()          # 원하는 음식을 먹지 못한 학생들

for query in queries:
    query_type = query[0]
    match query_type:
        case "1":
            # 학생이 대기줄에 들어옴.
            _, student_id, food_id = query.strip().split()
            waiting.append((student_id, food_id))
        case "2":
            # 음식이 배식됨.
            _, food_id = query.strip().split()
            student = waiting.popleft()
            if student[1] == food_id:
                A.append(int(student[0]))
            else:
                B.append(int(student[0]))

# 모든 출력은 오름차순 정렬 후
print(" ".join(map(str, sorted(A))) if len(A) > 0 else "None")
print(" ".join(map(str, sorted(B))) if len(B) > 0 else "None")
print(" ".join(map(str, sorted(map(lambda s: int(s[0]), waiting)))) if len(waiting) > 0 else "None")
