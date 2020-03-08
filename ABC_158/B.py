import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

# 青色(0)の色が0個の時は、すぐに終了させる。
if a == 0:
    print("0")
    exit()

# まず、割り算ですぐに出せる青色の数を出す
bluecount1 = a * (n // (a + b))

if (n % (a+b)) == 0:
    seq = (a+b)
else:
    seq = n % (a+b)

if (n > (a+b)) and (n % (a+b)) != 0:
    if seq <= a:
        bluecount2 = seq
    else:
        bluecount2 = a
else:
    bluecount2 = 0

# print(bluecount1)
# print(bluecount2)

ans = bluecount1 + bluecount2
print(ans)


"""
考えられるパターン
１．

２．
３．

"""