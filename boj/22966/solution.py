from sys import stdin

N = int(stdin.readline())
name = ""   # 문제의 제목을 저장. 알파벳 대문자로 10글자까지 가능.
level = 5   # 문제 난이도는 1~4

for _ in range(N):
    problem_name, problem_level = stdin.readline().split()
    problem_level = int(problem_level)
    if problem_level < level:
        name = problem_name
        level = problem_level

print(name)