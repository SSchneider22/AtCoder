"""早くするための基本"""
# 「ループ」は基本的にfor。whileは遅い
#  Atcoderで動かすときは、Pypy3使うと早い


"""参考URL"""
# Pythonの知っておくと良い細かい処理速度の違い8個
# https://www.kumilog.net/entry/python-speed-comp


"""標準入力"""
# 必須の文章、これにすることでかなり高速化する
import sys
input = sys.stdin.readline # 改行コード「\n」を呼んでしまうため、文字列数など、注意！！


# 整数を1つ、文字列を1行ずつ入力するとき
# （入力例）
# N
# S
n = int(input())
s = input()

# 整数を２つ、1行に空白で区切って入力するとき
#（入力例）
# A B
a, b = map(int, input().split())

# ■整数を１つ、改行後いくつあるかわからない数列を空白で区切って1行で入力するとき
#（入力例）
# N
# a1 a2 a3 … aN
n = int(input())
a = list(map(int, input().split()))
a = list(set(map(int, input().split())))  # 入力時点でリスト内重複削除したい場合

# 整数を１つ入力し、その後入力された1行ずつに対して処理を行う
#（入力例）
# N
# t1 x1 y1
# t2 x2 y2
# :
# tN xN yN
n = int(input())
flg = 0
for i in range(n):
    t, x, y = map(int, input().split())

# 整数を１つ入力し、N分データをいれてから、処理を行うとき
#（入力例）
# M
# t1 x1 y1
# t2 x2 y2
# :
# tN xN yN
m = int(input())
p = [[int(j) for j in input().split()] for i in range(m)]

# 入力されたものを分割してリスト化したいとき
# (入力例)
# 5
# 2 4
# 1 9
# 1 8
# 4 9
# 3 12
# [[2, 4], [1, 9], [1, 8], [4, 9], [3, 12]]
n = int(input())
tasklist = []
for i in range(n):
    tasklist.append(list(map(int, input().split())))

# 入力されたものを1行ずつリストに格納する
#（入力例）
# 5 2
# 2016-01-01 00:00:00 177
# 2016-01-01 00:39:49 133
# 2016-01-01 01:35:41 488
# 2016-01-01 01:46:43 740
# 2016-01-01 02:05:34 465
# （出力例）
# ['', '2016-01-01 00:00:00 177', '2016-01-01 00:39:49 133', '2016-01-01 01:35:41 488', '2016-01-01 01:46:43 740']
n, m = map(int, input().split())
log_list = [input() for i in range(n)]

# 入力行数制限なしで、標準入力をリスト化する　※Yahooで出た。これでもEnter2回押さないといけない
a = []

while True:
    line = sys.stdin.readline()
    if not line:
        break
    if line == '\n':
        break
    a.append(line)

"""print"""
# 「'文字列'.format」として記述。
a = 'abcde'
b = len(a)
c = a[2:5]
print('a={}, b={}, c={}'.format(a, b, c))


"""リストの初期化"""
# 1次元リスト
None * N

# 2次元配列
[[None] * N for _ in range(N)]


"""リストの値を一つずつ参照"""
# リストを直接参照するほうが、range()でindex作るより早い
for a in A:
    print(a)


"""リストへの値追加"""
# append()は遅い
# 方法その1：値代入
A = [None] * N
for i in range(N):
    A[i] = i

# 方法その2：内包表記
A = [i for i in range(N)]


""""""
"""各種アルゴリズム"""
""""""

"""フィボナッチ数列"""
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""FizzBuzz"""
for i in range(1, 51):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')


"""素数判定 prime"""
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 1 == 0:
            return False
    return True


"""