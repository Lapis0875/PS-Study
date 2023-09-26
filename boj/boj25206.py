from sys import stdin

total_score: float = 0.0
total_time: float = 0.0

score_map: dict[str, float] = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

for _ in range(20):
    name, time, score = stdin.readline().split()
    if score == "P":
        continue
    time = float(time)
    total_score += score_map[score] * time
    total_time += time

print(total_score / total_time)
