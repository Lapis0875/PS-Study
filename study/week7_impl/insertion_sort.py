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

def insertionSort(array: list[C]):
    N: Final[int] = len(array)
    for i in range(1, N):  # array의 인덱스 0 ~ N-2 까지 총 (N-1회) 반복
        key: C = array[i]
        j: int = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

target: list[int] = list(range(1, 16))
print(f"Goal: {target}")

shuffle(target)
print(f"Before sort : {target}")

insertionSort(target)
print(f"After sort : {target}")