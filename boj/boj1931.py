from sys import stdin
from typing import Final, Iterator
from bisect import bisect_left

class Meeting:
    start: int
    end: int
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    @classmethod
    def parse(cls, s: str) -> "Meeting":
        start, end = map(int, s.split())
        return cls(start, end)
    
    def __iter__(self) -> Iterator[int]:
        return (self.start, self.end).__iter__()
    
    def __gt__(self, other: "Meeting | object") -> bool:
        if isinstance(other, Meeting):
            return self.start > other.start
        else:
            return NotImplemented
    
    def __lt__(self, other: "Meeting | object") -> bool:
        if isinstance(other, Meeting):
            return self.start < other.start
        else:
            return NotImplemented
    
    def __repr__(self) -> str:
        return f"Meeting({self.start} ~ {self.end})"

N: Final[int] = int(stdin.readline())

duration_group: dict[int, list[Meeting]] = {}
duration_keys: list[int] = []

for _ in range(N):
    meeting = Meeting.parse(stdin.readline())
    start, end = meeting
    duration: int = end - start
    print(meeting, duration)
    
    try:
        # todo: 이분탐색으로 삽입위치 결정하기
        location: int = bisect_left(duration_group[duration], meeting)
        duration_group[duration].insert(location, meeting)
    except KeyError:
        duration_group[duration] = [meeting]
        duration_keys.insert(bisect_left(duration_keys, duration), duration)

print(duration_group) 

meetings: list[Meeting] = []
for group in duration_keys:
    meetings.extend(duration_group[group])

count: int = 0
next_available: int = 0
schedule: list[Meeting] = []
for meet in meetings:
    start, end = meet
    if start >= next_available:
        count += 1
        next_available = end
        schedule.append(meet)

print(meetings)
print(schedule)
print(count)