import sys
sys.stdin = open("input.txt", "r")
trans = str.maketrans("1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./", "`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.")

while True:
    try:
        print(input().translate(trans))
    except:
        break
