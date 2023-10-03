from sys import stdin
from collections import OrderedDict

group: int = 1
students: list[str] = []
papers: OrderedDict[str, list[bool]] = OrderedDict()
nasty: list[tuple[str, str]] = []

while (n := stdin.readline()[:-1]) != "0":
    N: int = int(n)
    
    for _ in range(N):
        stu, *paper = stdin.readline()[:-1].split()
        students.append(stu)
        papers[stu] = [True if p == "P" else False for p in paper]
    
    for base, (stu, paper) in enumerate(papers.items()):
        for i, msg in zip(range(N - 1, 0, -1), paper):
            if not msg:
                nasty.append((students[(base + i) % N], stu))
    
    print(f"Group {group}")
    if len(nasty):
        for a, b in nasty:
            print(f"{a} was nasty about {b}")
    else:
        print("Nobody was nasty")
    print()
    students.clear()
    papers.clear()
    nasty.clear()
    group += 1
