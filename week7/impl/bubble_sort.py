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

def bubbleSort(array: list[C]):
    N: Final[int] = len(array)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if array[j] > array[j + 1]:
                tmp: C = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
            

target: list[int] = list(range(1, 16))
print(f"Goal: {target}")

shuffle(target)
print(f"Before sort : {target}")

bubbleSort(target)
print(f"After sort : {target}")