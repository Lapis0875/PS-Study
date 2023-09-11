from random import shuffle
from typing import Final, Protocol, TypeVar


class Comparable(Protocol):
    """비교 가능한 타입에 대한 프로토콜 (인터페이스와 유사한 것)"""
    def __eq__(self, __value) -> bool: ...
    def __ne__(self, __value) -> bool: ...
    def __ge__(self, __value) -> bool: ...
    def __gt__(self, __value) -> bool: ...
    def __le__(self, __value) -> bool: ...
    def __lt__(self, __value) -> bool: ...

C = TypeVar("C", bound=Comparable)      # 비교 가능한 타입에 대한 제네릭 매개변수

def selectionSort(array: list[C]):
    N: Final[int] = len(array)
    for i in range(N - 1):  # array의 인덱스 0 ~ N-2 까지 총 (N-1회) 반복
        least: int = i
        for j in range(i + 1, N):
            if array[j] < array[least]:
                least = j
        tmp: C = array[least]
        array[least] = array[i]
        array[i] = tmp

target: list[int] = list(range(1, 16))
print(f"Goal: {target}")

shuffle(target)
print(f"Before sort : {target}")

selectionSort(target)
print(f"After sort : {target}")