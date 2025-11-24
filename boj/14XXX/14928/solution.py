input = open(0).readline
N = input().strip()

temp = 0
for c in N:
    temp = (temp * 10 + int(c)) % 20000303 # c: 0~9 / temp : 0 ~ 200000302 => additional mod not required.
print(temp)

# Only Python
print(int(input()) % 20000303) # Python is good language for big integer.