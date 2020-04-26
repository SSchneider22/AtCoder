import sys
input = sys.stdin.readline
import itertools

def digits_of(n): # nの桁の数字のリストを出力する関数｡ nは自然数
    digits = [] # nの桁の数字を入れるリスト
    while n != 0:
        r = n % 10 # 10で割った余り
        digits.append(r) # リストに加える
        n = n // 10 # nを10で割った整数に置き換える
    return digits

def is_multiple_of_2019(n): # nは自然数
    sum = 0 # 各桁の数字の合計をもとめる
    for i in digits_of(n):
        sum += i
    return sum % 2019 == 0 # もし合計が2019の倍数ならTrue, そうでないならFalse

s = input().replace("\n","")

dig = digits_of(int(s))
result = []
for n in range(1,len(dig)+1):
    for conb in itertools.combinations(dig, n):
        result.append(list(conb)) #タプルをリスト型に変換
print(result)

print(dig)




"""
import sys
input = sys.stdin.readline

s = input().replace("\n","")

ans = 0
for i in range(len(s)-4):
    for j in range(3,len(s)):
        if len(s[i:j+1]) >= 4:
            # print(s[i:j+1])
            if int(s[i:j+1]) % 2019 == 0:
                ans += 1

print(ans)
"""

"""
2019
4038
6057
8076
10095
12114
14133
16152
18171
20190
22209
24228

2000の倍数＋19の倍数

"""