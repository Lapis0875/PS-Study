from sys import stdin

N: int = int(stdin.readline())

classes: list[dict[int, list[int]]] = [{}, {}, {}, {}, {}]  # [grade <int>: {class <int>: [student <int>]: list<int>}: dict<int, list<int>]

for i in range(N):
    for grade, clazz in enumerate(map(int, stdin.readline().split())):
        try:
            classes[grade][clazz].append(i)
        except KeyError:
            classes[grade][clazz] = [i]

for grade in range(5):
    print(f"grade: {grade}")
    for clazz, students in classes[grade].items():
        print(f"{clazz} = {students}")

max_met: int = 0
temp_president: int = -1

for i in range(N):      # 학생별로 순회하며...
    has_met: list[bool] = [False for _ in range(N)]

    for grade in classes:
        if len(grade) < 5:
            for clazz in grade:
                if i in grade[clazz]:
                    for student in grade[clazz]:
                        has_met[student] = True

    s = sum(has_met)
    print(i, s)
    if s > max_met:
        max_met = s
        temp_president = i

print(temp_president)