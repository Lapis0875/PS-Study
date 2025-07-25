# Migrated from ./boj/boj2672.py by boj_validator
from sys import stdin
from typing import Final


class VerticalLine:
    """사각형의 세로 변을 나타내는 객체입니다. 모든 좌표는 10을 곱해 정수화 되었습니다."""
    x: Final[int]                     # 이 세로 변의 x 좌표
    y_low: Final[int]                 # 이 세로 변의 아래쪽 y 좌표
    y_high: Final[int]                # 이 세로 변의 위쪽 y 좌표
    height: Final[int]                # 이 세로 변의 높이
    
    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y_low = y
        self.y_high = y + height
        self.height = height
    
    @classmethod
    def parse_rectangle(cls, line: str) -> tuple["VerticalLine", "VerticalLine"]:
        """문자열을 파싱해 VerticalLine 객체로 만듭니다.

        Args:
            line (str): '{x} {y} {width} {height}' 형식의 사각형 정보 문자열

        Returns:
            _type_: tuple[VerticalLine, VerticalLine] : 왼쪽 변과 오른쪽 변을 각각 반환합니다.
        """
        x, y, width, height = map(lambda v: int(float(v) * 10), line.split())
        return cls(x, y, height), cls(x + width, y, height)
    
    def __gt__(self, other: "VerticalLine") -> bool:
        if isinstance(other, VerticalLine):
            return self.x > other.x
        else:
            return NotImplemented
        

N: int = int(stdin.readline())

vertical_lines: list[VerticalLine] = []  # 사각형 데이터를 세로선으로 변환해 저장한다.
for _ in range(N):
    left, right = VerticalLine.parse_rectangle(stdin.readline())
    vertical_lines.append(left)
    vertical_lines.append(right)

vertical_lines.sort()

area: int = 0
height: int = vertical_lines[0].height
for i in range(N - 1):     # 세로선을 2개씩 순회하기 위해서, N - 1번 순회한다.
    v1 = vertical_lines[i]
    v2 = vertical_lines[i + 1]
    
    area += (v2.x - v1.x) * height
    
    if v2.y_high < v1.y_high and v2.y_low < v1.y_low:           # 다음 세로 변이 기존 세로 변과 아래쪽으로 일부 겹친다면
        height += v1.y_low - v2.y_low
    elif v2.y_high > v1.y_high and v2.y_low > v1.y_low:         # 다음 세로 변이 기존 세로 변과 위쪽으로 일부 겹친다면
        height += v2.y_high - v1.y_high
    elif v2.y_high <= v1.y_low or v2.y_low >= v1.y_high:        # 다음 세로 변이 기존 세로 변에 포함되지 않는다면
        height = v2.height
        
        
# 소수점 두자리까지 출력 or 소수점없이 출력 처리
print(area // 100)
