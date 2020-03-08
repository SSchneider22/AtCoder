import sys
input = sys.stdin.readline

a, b, m = map(int, input().split())

alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

ans = min(alist) + min(blist)

for i in range(m):
    x, y, c = map(int, input().split())
    x -= 1  # リストは0番目から始まるため、合わせる
    y -= 1  # リストは0番目から始まるため、合わせる
    if alist[x] + blist[y] - c < ans:
        ans = alist[x] + blist[y] - c
    else:
        continue

print(ans)
