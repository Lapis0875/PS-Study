from sys import stdin

phone_eng: str = stdin.readline()[:-1]

dial: dict[str, int] = {
    "A": 2, "B": 2, "C": 2,
    "D": 3, "E": 3, "F": 3,
    "G": 4, "H": 4, "I": 4,
    "J": 5, "K": 5, "L": 5,
    "M": 6, "N": 6, "O": 6,
    "P": 7, "Q": 7, "R": 7, "S": 7,
    "T": 8, "U": 8, "V": 8,
    "W": 9, "X": 9, "Y": 9, "Z": 9,
}

time: int = 0
for c in phone_eng:
    number: int = dial[c]
    time += number + 1      # 1번 다이얼에 2초, 그 이후 다이얼은 떨어진 거리마다 +1초

print(time)
