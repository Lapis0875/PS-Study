total: int = int(input())
others: int = sum(int(input()) for _ in range(9))
print(total - others)