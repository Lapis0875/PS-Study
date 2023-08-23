from sys import stdin

sieve: list[bool] = [False, False]  # default for 0, 1
lastN: int = 1

while (s := stdin.readline()) != "-1\n":
    n: int = int(s)
    factors: list[int] = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    if n == sum(factors):
        print(f"{n} = {' + '.join(map(str, factors))}")
    else:
        print(f"{n} is NOT perfect.")
