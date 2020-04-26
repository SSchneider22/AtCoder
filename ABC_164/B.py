import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().replace("\n","").split())

takahashihp = a
aokihp = c

while True:
    aokihp -= b
    if aokihp < 1:
        print("Yes")
        break
    takahashihp -= d
    if takahashihp < 1:
        print("No")
        break