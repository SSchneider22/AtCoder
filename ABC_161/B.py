import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().replace("\n","").split()))

count = 0
allhyou = sum(a)

# print(allhyou)

for i in range(len(a)):
    if a[i] >= (allhyou/(4*m)):
        count += 1

if count >= m:
    print("Yes")
else:
    print("No")
