input = open(0).readline

while True:
    line = input().strip()

    if line.startswith("#"):
        break

    name, age, weight = line.split()
    if int(age) > 17 or int(weight) >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")
