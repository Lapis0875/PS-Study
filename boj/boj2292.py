from sys import stdin

N = int(stdin.readline())

row: int = 1
lastRoomInRow: int = 1
while True:
    if N <= lastRoomInRow:
        print(row)
        break
    lastRoomInRow += 6 * row
    row += 1
