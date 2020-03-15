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


"""combinations、組み合わせ、順列"""
from itertools import permutations, combinations,combinations_with_replacement,product
a=['a','b','C']
print(list(permutations(a)))
# [('a', 'b', 'C'), ('a', 'C', 'b'), ('b', 'a', 'C'), ('b', 'C', 'a'), ('C', 'a', 'b'), ('C', 'b', 'a')]
print(list(combinations(a,2)))
# [('a', 'b'), ('a', 'C'), ('b', 'C')]
print(list(combinations_with_replacement(a,3)))
# [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'C'), ('a', 'b', 'b'), ('a', 'b', 'C'), ('a', 'C', 'C'), ('b', 'b', 'b'), ('b', 'b', 'C'), ('b', 'C', 'C'), ('C', 'C', 'C')]


"""bit　ビット演算"""
from itertools import product
a=list(product(['+','-'],repeat=3))
print(a)
# [('+', '+', '+'), ('+', '+', '-'), ('+', '-', '+'), ('+', '-', '-'), ('-', '+', '+'), ('-', '+', '-'), ('-', '-', '+'), ('-', '-', '-')]
s=['5', '5', '3', '4']
for i in a:
    ans=s[0]+i[0]+s[1]+i[1]+s[2]+i[2]+s[3]
    if eval(ans)==7: # 
        print(ans+'=7')
        # 5-5+3+4=7
        break


"""集計　collect"""
from collections import Counter
a=[2,2,2,3,4,3,1,2,1,3,1,2,1,2,2,1,2,1]
a=Counter(a)
for i in a.most_common(3):
    print(i)
    # (2, 8) # リストaの中に、２が８回出ていた、ということを出力
    # (1, 6)
    # (3, 3)


"""n進数変換　１０進数から?進数に変換"""
n = 18

def convert(n, base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

print(convert(n,2))  # 18を２進数表記した、「10010」
print(convert(n,3))  # 18を３進数表記した、「200」


"""n進数変換　2進数から10進数に変換"""
n = '10010'
result = 0
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i -1))
print(result) # 10010を１０進数に変換した、「18」



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


"""最大公約数、最小公倍数"""
import fractions
a,b=map(int, input().split())
f=fractions.gcd(a,b)
f2=a*b//f
print(f,f2)


"""素数判定 prime"""
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 1 == 0:
            return False
    return True


"""全探索　全列挙(たいていの場合、ただの多重ループでいける)"""



"""全探索　ビット内全探索"""
# https://qiita.com/gogotealove/items/11f9e83218926211083a



"""順列全探索"""



"""二分探索"""



"""深さ優先探索（DFS）"""


"""幅優先探索（BFS）"""


"""動的計画法（DP）　ナップサックDP（部分和問題・最小共通部分列などは全てこれに含まれます）"""


"""動的計画法（DP）　区間DP"""


"""動的計画法（DP）　bitDP"""


"""ダイクストラ法"""


"""ワーシャルフロイド法"""


"""クラスカル法"""


"""べき乗を高速に計算するアルゴリズム"""


"""逆元を高速に計算するアルゴリズム"""


"""累積和"""


"""いもす法"""



""""""
"""各種データ構造"""
""""""

"""グラフ"""


"""木"""


"""Union-Find"""