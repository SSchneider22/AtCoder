import sys
input = sys.stdin.readline

a, b, n = map(int, input().replace("\n","").split())

ans = 0

#bがnよりも大きい時
if b > n:
    ans = int(a*n/b)
    print(ans)
    exit()

#b==nのときは、終了間際の2個だけ比較する
elif b == n:
    for i in range(n-1,n+1):
        tmpans = int(a*i/b) - (a*int(i/b))
        if tmpans >= ans:
            ans = tmpans
    print(ans)
    exit()

#これ以外の時は、nはb値ごとにスキップする。
else:
    for i in range(int(n/b),n+1,b):
        tmpans = int(a*(i-2)/b) - (a*int((i-2)/b))
        if tmpans >= ans:
            ans = tmpans

print(ans)
