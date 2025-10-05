input = open(0).readline
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

base = B1 * B2 // gcd(B1, B2) # lcm
over = A1 * (base // B1) + A2 * (base // B2)

g = gcd(over, base)
print(f"{over // g} {base // g}")