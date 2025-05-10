# Migrated from ./boj/boj15947.py by boj_validator
from typing import Final


N: Final[int] = int(input())

BASE_WORDS: Final[list[str]] = [
    "baby",
    "sukhwan",
    "tururu",
    "turu",
    "very",
    "cute",
    "tururu",
    "turu",
    "in",
    "bed",
    "tururu",
    "turu",
    "baby",
    "sukhwan"
]
BASE_LEN: Final[int] = 14

def genRepeated(repeat: int) -> list[str]:
    repeated: list[str] = []
    for w in BASE_WORDS:
        if w == "tururu":  # 특별한 반복 조건이 있는 단어
            if (repeat >= 3):   # tururu에는 이미 2번의 ru가 포함
                w = f"tu+ru*{repeat + 2}"
            else:
                w += "ru" * repeat
        elif w == "turu":
            if (repeat >= 4):   # turu에는 이미 1번의 ru가 포함
                w = f"tu+ru*{repeat + 1}"
            else:
                w += "ru" * repeat
        repeated.append(w)
    return repeated

index: int = N % BASE_LEN
repeat: int = N // BASE_LEN

print(genRepeated(repeat)[index - 1])