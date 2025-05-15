input = open(0).readline
M = int(input())

ingredients = {}
for _ in range(M):
    ingredient, amount = input().rstrip().split()
    try:
        ingredients[ingredient] += int(amount)
    except KeyError:
        ingredients[ingredient] = int(amount)

amounts = sorted(ingredients.values())
result = False
for i in range(len(amounts) - 1):
    for j in range(i + 1, len(amounts)):
        if amounts[i] * 1618 // 1000 == amounts[j]:
            result = True
            break

print("Delicious!" if result else "Not Delicious...")