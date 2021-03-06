"""解くための考え"""
# 複数の値があって、ループが必要な場合は、「ある値を固定」することをまず考える。3つの値の二部探索とか
#

"""早くするための基本"""
# 「ループ」は基本的にfor。whileは遅い。range()使うときは、第二引数の値は含まれないことに注意！！！
#  Atcoderで動かすときは、Pypy3使うと早い。ただ、文字列系は遅いかも…とのこと


"""使えるライブラリ"""
# collections：counterで要素のカウント等が出来る
# itertools：順列、組み合わせ、リスト内での累積和などが使える。パターンの羅列を作りたいときに便利
# bisect：二分探索で使える
# heapq：木構造のヒープ、二分ヒープなどで使用。
# math：
# fractions.gcd：Pythonでの最大公約数はこれ



"""標準入力"""
# 必須の文章、これにすることでかなり高速化する
# 改行コード「\n」を呼んでしまうため、文字数など、注意！！
import sys
input = sys.stdin.readline


# 整数を1つ、文字列を1行ずつ入力するとき
# （入力例）
# N
# S
n = int(input())
s = input().replace("\n","")

# 整数を２つ、1行に空白で区切って入力するとき
#（入力例）
# A B
a, b = map(int, input().replace("\n","").split())

# ■整数を１つ、改行後いくつあるかわからない数列を空白で区切って1行で入力するとき
#（入力例）
# N
# a1 a2 a3 … aN
n = int(input())
a = list(map(int, input().replace("\n","").split()))
a = list(set(map(int, input().replace("\n","").split())))  # 入力時点でリスト内重複削除したい場合

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
    t, x, y = map(int, input().replace("\n","").split())

# 整数を１つ入力し、その数だけデータをいれてから、処理を行うとき
#（入力例）
# M
# t1 x1 y1
# t2 x2 y2
# :
# tN xN yN
m = int(input())
p = [[int(j) for j in input().replace("\n","").split()] for i in range(m)]

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
    tasklist.append(list(map(int, input().replace("\n","").split())))

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
n, m = map(int, input().replace("\n","").split())
log_list = [input().replace("\n","") for i in range(n)]


# 入力値が0 0になるまで、入力に対応し続ける
while True:
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break

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


"""再帰呼び出し回数の上限変更 ※デフォルトが1000らしい"""
import sys
sys.setrecursionlimit(10**6)


"""リストの初期化"""
# 1次元リスト
None * N

# 2次元配列
[[None] * N for _ in range(N)]


"""リストの値を一つずつ参照"""
# リストを直接参照するほうが、range()でindex作るより早い
for a in A:
    print(a)

# 以下は文字列ver
n = str(input().replace("\n",""))

if '7' in n:
    print('Yes')
else:
    print('No')


"""リストの定義"""
# append()は遅い
# 方法その1：値代入
A = [None] * N
for i in range(N):
    A[i] = i

# 方法その2：内包表記
A = [i for i in range(N)]


"""リスト内の要素の並び替え"""
a = [2, 5, 1, 4, 3]
b = sorted(a)

print(a)    # [2, 5, 1, 4, 3] a自体は変更なし
print(b)    # [1, 2, 3, 4, 5]

a.sort()
print(a)    # [1, 2, 3, 4, 5] a自体がソートされている

b = sorted(a, reverse=True)
print(b)    # [5, 4, 3, 2, 1] 降順ソート


"""大文字・小文字を考慮してソートするかしないか"""
a = ['e', 'B', 'd', 'C', 'a']
print(sorted(a))
# ['B', 'C', 'a', 'd', 'e']普通にソートすると大文字，小文字それぞれでソートされます．
print(sorted(a, key=lambda x: x.upper()))
# ['a', 'B', 'C', 'd', 'e']比較時に大文字に変換してソートするので，結果大文字・小文字あわせてソートされます．



"""二次元リストの並び替え"""
from operator import itemgetter
B =[[5,8], [6,10], [7,2],[4,1], [3,11],[9,0]]
# B =[(5,8), (6,10), (7,2),(4,1), (3,11),(9,0)]
print(sorted(B, key = itemgetter(0))) #第1変数で昇順ソートしてる
#[(3, 11), (4, 1), (5, 8), (6, 10), (7, 2), (9, 0)]
print(sorted(B, key = itemgetter(0),reverse=True)) #第1変数で降順ソートしてる
#[(9, 0), (7, 2), (6, 10), (5, 8), (4, 1), (3, 11)]
print(sorted(B, key = itemgetter(1))) #第2変数で昇順ソートしてる
#[(9, 0), (4, 1), (7, 2), (5, 8), (6, 10), (3, 11)]
print(sorted(B, key = itemgetter(1),reverse=True)) #第2変数で降順ソートしてる
#[(3, 11), (6, 10), (5, 8), (7, 2), (4, 1), (9, 0)]


"""多重キーの多次元リストの並び替え"""
a = [(1, 'One', '1'), (1, 'One', '01'),
     (2, 'Two', '2'), (2, 'Two', '02'),
     (3, 'Three', '3'), (3, 'Three', '03')]
print(sorted(a, key=lambda x: (x[1], x[2], x[0])))
# 内部のタプルの1要素目（アルファベット），2要素目（数字），0要素目（数値）の順に比較してソート
# [(1, 'One', '01'), (1, 'One', '1'), (3, 'Three', '03'), (3, 'Three', '3'), (2, 'Two', '02'), (2, 'Two', '2')]


"""二次元リストの行列を入れ替える"""
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose = [x for x in zip(*data)]
print(transpose)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


"""和集合と積集合"""
a = [2, 4, 6, 8]
b = [3, 6, 9]

print(list(set(a) | set(b)))  # 和集合 [2, 3, 4, 6, 8, 9]
print(list(set(a) & set(b)))  # 積集合 [6]


"""リストのコピー 基本deepcopyを使うこと"""
from copy import deepcopy

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = deepcopy(a)     # ディープコピー
b[0].append(0)      # b[0]（内部のリスト）はaとは別のオブジェクト

print(a)            # aに影響はない [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(b)            # [[1, 2, 3, 0], [4, 5, 6], [7, 8, 9]]


"""combinations、組み合わせ、順列"""
from itertools import permutations, combinations,combinations_with_replacement,product
tmp = ['a','b','C']
print(list(permutations(tmp)))
# [('a', 'b', 'C'), ('a', 'C', 'b'), ('b', 'a', 'C'), ('b', 'C', 'a'), ('C', 'a', 'b'), ('C', 'b', 'a')]
print(list(combinations(tmp, 2)))
# [('a', 'b'), ('a', 'C'), ('b', 'C')]
print(list(combinations_with_replacement(tmp, 3)))
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
l=['a','b','b','c','b','a','c','c','b','c','b','a']
S=Counter(l)#カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
print(S.most_common(2)) #[('b', 5), ('c', 4)]
print(S.keys()) #dict_keys(['a', 'b', 'c'])
print(S.values()) #dict_values([3, 5, 4])
print(S.items()) #dict_items([('a', 3), ('b', 5), ('c', 4)])
print(S['a']) # 3

intl = [1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4]
ints = Counter(intl)
print(ints[1]) # 3


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

# 2進数、10進数、16進数については以下でも可能
print(bin(255))                 # 10進数 -> 2進数
print(hex(255))                 # 10進数 -> 16進数

# 10進数への変換はint()関数の第2引数に基数を渡して行います．
print(int('0b11111111', 2))     # 2進数 -> 10進数
print(int('0xff', 16))          # 16進数 -> 10進数


"""アルファベットの羅列の作成"""
al=[chr(ord('a') + i) for i in range(26)]
print(al)


"""複数の文字列をまとめて置換"""
S='54IZSB'
S = S.translate(str.maketrans("ODIZSB","001258"))
print(S) # 541258


"""大文字・小文字への変換"""
b = 'aBCdEfg'
print(b.upper()) # ABCDEFG
print(b.lower()) # abcdefg


"""文字列の反転"""
s = 'ABCDEFG'
print(s[::-1]) # GFEDCBA


"""dropwhileとtakewhile"""
# dropwhileは先頭から与えられた条件が真である限り除外して，それ以降の要素を戻します．takewhileはその逆で先頭から与えられた条件が真であるところまでの要素を戻します．
from itertools import dropwhile, takewhile
a = [3, 6, 1, 7, 2, 5]
b = dropwhile(lambda x: x != 1, a)  # 1が出るまでを除外する
print(list(b)) # [1, 7, 2, 5]
c = takewhile(lambda x: x != 1, a)  # 1が出るまでを取り出す
print(list(c)) # [3, 6]


"""groupby"""
# 連続する要素をグループ化します．ただし同じ要素でも連続していないものはグループ化しません．
from itertools import groupby

a = [1, 1, 2, 3, 3, 3, 1, 2, 2]
gr = groupby(a)

for key, value in gr:
    print(key, list(value))

# 1 [1, 1]
# 2 [2]
# 3 [3, 3, 3]
# 1 [1]
# 2 [2, 2]

# 先頭から順に、keyに2の余りを算出するラムダを指定して，奇数・偶数ごとにグループ化
from itertools import groupby
a = [1, 3, 2, 4, 3, 1, 1, 2, 4]
for key, value in groupby(a, key=lambda x: x % 2):
    print(key, list(value))
# 1 [1, 3]
# 0 [2, 4]
# 1 [3, 1, 1]
# 0 [2, 4]

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
for i in range(1, 51"""n+1"""):
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
a,b = map(int, input().split())
f = fractions.gcd(a,b)
f2 = a*b//f
print(f,f2)

# 最大公約数　その２
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(1274,975))

# 最大公約数　複数Ver
import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)


"""素数判定 prime"""
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 1 == 0:
            return False
    return True


"""素因数分解"""
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table




"""全探索　全列挙(たいていの場合、ただの多重ループでいける)"""



"""全探索　ビット内全探索"""
# https://qiita.com/gogotealove/items/11f9e83218926211083a



"""順列全探索"""



"""二分探索 pythonだと、bisectがかなり使えそう"""
# bisect_left(L,x) xをLに挿入できる点(の番号)を探し当てる、ただしLにxがある場合は一番左になるようにする。
# bisect_right(L,x), bisect(L,x) xをLに挿入できる点(の番号)を探し当てる、ただしLにxがある場合は一番右になるようにする。
from bisect import bisect_left,bisect_right
# e869120_recommend100の、20.pyあたりの二分探索問題を参考にする


"""最短経路"""




"""深さ優先探索（DFS）目的のほうへ進めるだけ進んで、進めなくなったら戻る方法を深さ優先探索という。木構造の上から順に、一番下まで下りて、そのあとに一つ上に戻ってすぐ下りれそうなら下りて、を繰り返す"""
tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]
# ０～１４と書かれたノードがあり、リストではそのノードにぶら下がっているノードをリストとして持っている。例えば、0のノードには１，２がぶら下がっているため、[1,2]と記している
data = [0]
while len(data) > 0:
    pos = data.pop() # 末尾から取り出す
    print(pos, end = ' ')
    for i in tree[pos]:
        data.append(i) # 末尾に追加



"""幅優先探索（BFS） 探索を開始するところから近いものをリストアップし、さらにそれぞれを細かく調べていく方法。木構造の上から順に、その階層の要素をすべて確認してから、下の階層を見ていく"""
tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]
# ０～１４と書かれたノードがあり、リストではそのノードにぶら下がっているノードをリストとして持っている。例えば、0のノードには１，２がぶら下がっているため、[1,2]と記している
data = [0]
while len(data) > 0:
    pos = data.pop(0) # 先頭から取り出す
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i) # 末尾に追加


"""しゃくとり：しゃくとり法とは、ある配列が与えられたときに、「その配列の区間で(配列の連続する部分列)  で、とある条件を満たすような区間」を求める時に使います。"""
"""「区間」が「尺取り虫」という伸び縮みしながら進む虫に例えられており、尺取虫が配列を先頭から最後まで条件を満たすように伸び縮みしながら進んでいくようなイメージです。"""



"""動的計画法（DP）　ナップサックDP（部分和問題・最小共通部分列などは全てこれに含まれます）"""


"""動的計画法（DP）　区間DP"""


"""動的計画法（DP）　bitDP"""
# https://qiita.com/masayoshi361/items/0be4bce77783b6013b34


"""ダイクストラ法：負のループがない2点間距離、NN 頂点 MM 辺のグラフにおける頂点 11 から各頂点への最短経路長を、O(MlogN)O(Mlog⁡N) で計算するアルゴリズム"""


"""ワーシャルフロイド法：すべての2点間の最短距離を求める"""

n=int(input())
c=[[random.randint(1, 10) for i in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            c[i][j]=min(c[i][j],c[i][k]+c[k][j])
for i in c:
    print(i)

from scipy.sparse.csgraph import floyd_warshall
cost=floyd_warshall(c)

"""ベルマンフォード法：任意の2点間の距離、辺の値が負でも使える"""
def BF(p,n,s):
    inf=float("inf")
    d=[inf for i in range(n)]
    d[s-1]=0
    for i in range(n+1):
        for e in p:
            if e[0]!=inf and d[e[1]-1]>d[e[0]-1]+e[2]:
                d[e[1]-1] = d[e[0]-1] + e[2]
        if i==n-1:t=d[-1]
        if i==n and t!=d[-1]:
            return [0,'inf']
    return list(map(lambda x:-x, d))

n,m=map(int, input().split())
a=[list(map(int, input().split())) for i in range(m)]
a=[[x,y,-z] for x,y,z in a]
print(BF(a, n, 1)[-1])

"""クラスカル法：最小全域木を解くアルゴリズム"""


"""べき乗を高速に計算するアルゴリズム"""
def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x

"""二項係数nCrを高速に計算する"""



"""逆元を高速に計算するアルゴリズム"""
# https://cocoinit23.com/ncr-mod-1000000007/
# すべて累積した後に10^9+7でわると、計算ができない場合に用いる。
# （例）
# nCr mod 1000000007 の場合、
# 分母 denominator で割り算してmodを取ることと、
# denominator^(1000000007-2)を掛け算してmodを取ることは等しくなる。
numerator * pow(denominator, mod - 2, mod) % mod


# n^mをpで割ったあまりを求める
pow(n,m,p)

# pが素数の時、nのmod pでの逆元はフェルマーの小定理より
pow(n,p-2,p)


"""累積和"""
from itertools import accumulate
A=[1,4,3,4,6,5]
print(list(accumulate(A))) #[1, 5, 8, 12, 18, 23]
# itertoolsの戻り値はイテレータとなっているので必要に応じてlist化します．

# 文字列でも使用可能
s = ['ab', 'bc', 'cd']
print(list(itertools.accumulate(s)))
# -> ['ab', 'abbc', 'abbccd']


"""拡張ユークリッド互除法"""
# gcd(a,b) と ax + by = gcd(a,b) の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

"""いもす法"""



""""""
"""各種データ構造"""
""""""

"""ソート"""
# Pythonのソートは、リストについてる標準のsortが、最も高速

"""グラフ"""


"""スタック"""
stack = [1,2,3,4]
# push
stack.append(5)  # stack = [1,2,3,4,5]
# pop
stack.pop()  # stack = [1,2,3,4]


"""キュー"""
from collections import deque

l = [0,1,2,3]
q = deque(l)
q.append(4)  # 後ろから4を挿入, l=deque([0,1,2,3,4])
q.appendleft(5)  # 前から5を挿入, l=deque([5,0,1,2,3,4])
x = q.pop()  # 後ろの要素を取り出す, x=4, l=deque([5,0,1,2,3])
y = q.popleft()  # 前の要素を取り出す, y=5, l = deque([0,1,2,3])


"""ヒープ"""
# 木構造で構成され、子ノードの値は親ノードよりも、「常に大きいか等しい」or「常に小さいか等しい」もの
# また、各ノードが最大で２つの子ノードを持つものを二分ヒープという。
# プライオリティーキューのことです(Pythonだとヒープキューっていうらしい)。プライオリティーキューとは
# - 計算量O(logN)O(log⁡N)で要素を挿入
# - 計算量O(logN)O(log⁡N)で最小値を取り出す
# ができるデータ構造です。最短経路を求めるダイクストラ法でお世話になります。

from heapq import heappop,heappush
L=[3,0,2,5,7,2]
H=[]
for l in L:
    heappush(H,l)
print(H) #[0, 3, 2, 5, 7, 2]
print(heappop(H)) #0
print(heappop(H)) #2
print(heappop(H)) #2


"""木：NN 頂点 N−1N−1 辺の連結なグラフ"""


"""Union-Find"""
class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

n,m=5, 3 #map(int, input().split()) n:ノードの数, m:パスの数
uf1=UnionFind(n)
for i,j in [[1, 2],[5, 4],[4, 1]]:  # range(m):
    a,b=i,j #map(int, input().split()) #a,b:つながっている辺
    uf1.union(a-1,b-1)

for i in range(n):uf1.find(i)  # 一周findすることによって接続漏れをなくす。
print(uf1.par) #[4, 4, 2, 4, 4]