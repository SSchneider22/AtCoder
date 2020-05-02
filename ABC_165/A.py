import sys
input = sys.stdin.readline

k = int(input())
a, b = map(int, input().replace("\n","").split())

if a == b:
    if a % k == 0:
        print("OK")
        exit()

for i in range(a,b+1):
    if i % k == 0:
        print("OK")
        exit()

print("NG")
