from sys import stdin, maxsize

min_burger: int = maxsize
min_drink: int = maxsize
for _ in range(3):
    burger: int = int(stdin.readline())
    if burger < min_burger:
        min_burger = burger
for _ in range(2):
    drink: int = int(stdin.readline())
    if drink < min_drink:
        min_drink = drink
print(min_burger + min_drink - 50)
