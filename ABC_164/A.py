import sys
input = sys.stdin.readline

s, w = map(int, input().replace("\n","").split())

if s > w:
    print("safe")
else:
    print("unsafe")