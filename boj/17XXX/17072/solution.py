input = open(0).readline

def converter(red, green, blue):
    intensity = 2126 * red + 7152 * green + 722 * blue
    if intensity < 510_000:
        return "#"
    elif intensity < 1_020_000:
        return "o"
    elif intensity < 1_530_000:
        return "+"
    elif intensity < 2_040_000:
        return "-"
    else:
        return "."

N, M = map(int, input().split())
for _ in range(N):
    rgb_values = map(int, input().split())
    for i in range(M):
        print(converter(next(rgb_values), next(rgb_values), next(rgb_values)), end="")
    print()
