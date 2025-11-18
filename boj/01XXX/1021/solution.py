input = open(0).readline
N, M = map(int, input().split())

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [i for i in range(1, size + 1)]
        self.head = 0

    def rotate_clockwise(self, target):
        count = 0
        while self.queue[(self.head + count) % self.size] != target:
            count += 1
        return count

    def rotate_anticlockwise(self, target):
        count = 0
        while self.queue[(self.head - count) % self.size] != target:
            count += 1
        return count

    def find_minimum_rotation(self, target):
        clockwise = self.rotate_clockwise(target)
        anticlockwise = self.rotate_anticlockwise(target)
        
        if clockwise <= anticlockwise:
            self.head = (self.head + clockwise) % self.size
            self.queue.pop(self.head)
            self.size -= 1
            return clockwise
        else:
            self.head = (self.head - anticlockwise) % self.size
            self.queue.pop(self.head)
            self.size -= 1
            return anticlockwise


queue = CircularQueue(N)
count = 0
for index in map(int, input().split()):
    count += queue.find_minimum_rotation(index)

print(count)