# Migrated from ./boj/boj1620.py by boj_validator
from sys import stdin


N, M = map(int, stdin.readline().split())
pokemon: dict[str, int] = {}
pokemon_ids: list[str] = [""]   # 0번 인덱스는 사용하지 않는다.
for i in range(1, N + 1):
    name: str = stdin.readline()[:-1]
    pokemon[name] = i
    pokemon_ids.append(name)
for _ in range(M):
    question: str = stdin.readline().rstrip()
    if question.isdigit():
        print(pokemon_ids[int(question)])
    else:
        print(pokemon[question])