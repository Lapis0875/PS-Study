input = open(0).readline
xor = 0
sum = 0

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "3":
        print(sum)
    elif cmd[0] == "4":
        print(xor)
    elif cmd[0] == "1":
        x = int(cmd[1])
        sum += x
        xor ^= x
    elif cmd[0] == "2":
        x = int(cmd[1])
        sum -= x
        xor ^= x
