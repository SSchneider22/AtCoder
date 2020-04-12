import sys
import copy
from math import factorial
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    ans = 0

    # 1つ１つ削除したときのリストを作る
    adel = copy.deepcopy(a)
    del adel[i]

    # setにして、重複を削除しどんな要素があるかを確認
    adelset = list(set(adel))
    # print(adel)
    # print(adelset)

    for j in range(len(adelset)):
        cnt = adel.count(adelset[j])
        # print("{}は{}個".format(j,cnt))
        if cnt > 2:
            ans += factorial(cnt) / factorial(2) / factorial(cnt - 2)
        elif cnt == 2:
            ans += 1
        elif cnt <= 1:
            ans += 0
    print(int(ans))