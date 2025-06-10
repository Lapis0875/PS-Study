from collections import deque
S, E = map(int, input().strip().split())
queue = deque([S, S + 1, S + 2])

def FizzBuzz():
    for i in queue:
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
    print(i + 1)
    print("---")

for i in range(S + 3, E + 1):
    FizzBuzz()
    queue.popleft()
    queue.append(i)

# Output example:
# Buzz (10)
# 11
# Fizz
# ---   (Seperator btw input & output.)
# 13    (Answer Value.)
# ---   (Seprator for each test case data.)