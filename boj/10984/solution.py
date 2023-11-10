from sys import stdin

T: int = int(stdin.readline())

for _ in range(T):
    N: int = int(stdin.readline())
    C: int = 0
    G: float = 0.0
    
    for _ in range(N):
        c = int(stdin.read(1))
        g = float(stdin.readline())
        C += c
        G += g * c
    print(f"{C} {G / C:.1f}")