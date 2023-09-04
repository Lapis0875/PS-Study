from sys import stdin

yeondu: str = stdin.readline()[:-1]
yeondu_count: list[int] = [0, 0, 0, 0]
for c in yeondu:
    if c == "L":
        yeondu_count[0] += 1
    elif c == "O":
        yeondu_count[1] += 1
    elif c == "V":
        yeondu_count[2] += 1
    elif c == "E":
        yeondu_count[3] += 1

N: int = int(stdin.readline())
names: list[str] = sorted(stdin.readline()[:-1] for _ in range(N))
percentage: list[int] = []


def calc_percentage(name: str) -> int:
    L, O, V, E = yeondu_count
    for c in name:
        if c == "L":
            L += 1
        elif c == "O":
            O += 1
        elif c == "V":
            V += 1
        elif c == "E":
            E += 1
            
    # print(name, L, O, V, E)
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

for name in names:  # 사전순으로 정렬된 이름들을 가지고
    percentage.append(calc_percentage(name))

max_percentage: int = 0
max_name: str = names[0]
for i, p in enumerate(percentage):
    if p > max_percentage:      # 더 우승 확률이 높은 경우에만 이름을 갱신한다. 확률이 같은 경우, 이전 이름이 사전상 앞이므로 갱신하지 않는다.
        max_percentage = p
        max_name = names[i]

# print(yeondu_count)
# print(names)
# print(percentage)
print(max_name)
