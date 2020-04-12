"""早くするための基本"""
# 「ループ」は基本的にfor。whileは遅い
#  Atcoderで動かすときは、Pypy3使うと早い


"""参考URL"""
# Pythonの知っておくと良い細かい処理速度の違い8個
# https://www.kumilog.net/entry/python-speed-comp


"""標準入力"""
# 必須の文章、これにすることでかなり高速化する
import sys
input = sys.stdin.readline  # 改行コード「\n」を呼んでしまうため、文字数など、注意！！


# 整数を1つ、文字列を1行ずつ入力するとき
# （入力例）
# N
# S
n = int(input().replace("\n",""))
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



"""アルファベット"""
al=[chr(ord('a') + i) for i in range(26)]
print(al)


"""複数の文字列を置換"""
S='54IZSB'
S = S.translate(str.maketrans("ODIZSB","001258"))
print(S)




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


"""複数の文字列を置換"""
S='54IZSB'
S = S.translate(str.maketrans("ODIZSB","001258"))
print(S)


"""全探索　全列挙(たいていの場合、ただの多重ループでいける)"""



"""全探索　ビット内全探索"""
# https://qiita.com/gogotealove/items/11f9e83218926211083a



"""順列全探索"""



"""二分探索"""


"""最短経路"""
ys,xs=2,2
yg,xg=4,5
a=['########', '#......#', '#.######', '#..#...#', '#..##..#', '##.....#', '########']
n=[(ys-1,xs-1)]
route={n[0]:0}
p=[[1,0],[0,1],[-1,0],[0,-1]]
count=1
while route.get((yg-1,xg-1),0)==0 and count != 10000:
    n2=[]
    for i in n:
        for j in p:
            np=(i[0]+j[0],i[1]+j[1])
            if a[np[0]][np[1]]=='.' and route.get(np,-1)==-1:
                n2.append(np)
                route[np]=count
    n=n2
    count+=1
print(n,route)　



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

n=int(input())
a=list(map(int, input().split()))

count=0
right=0
m=dict()
for left in range(n):
    while right<n and m.get(a[right],0)==0:
        m[a[right]]=m.get(a[right],0)+1
        right+=1
    count=max(count,right-left)
    m[a[left]]=m.get(a[left],1)-1
print(count)


"""動的計画法（DP）　ナップサックDP（部分和問題・最小共通部分列などは全てこれに含まれます）"""
n=6
w=8
weight=[2,1,3,2,1,5]
value=[3,2,6,1,3,85]

dp=[[0 for i in range(w+1)] for j in range(n+1)]
for i in range(n):
    for j in range(w+1):
        if j>=weight[i] : dp[i+1][j]=max(dp[i][j-weight[i]]+value[i],dp[i][j])
        else: dp[i+1][j]=dp[i][j]
    print(dp[:i+2])
print(dp[n][w]) 　

"""動的計画法（DP）　区間DP"""


"""動的計画法（DP）　bitDP"""
# https://qiita.com/masayoshi361/items/0be4bce77783b6013b34

"""ダイクストラ法：負のループがない2点間距離、NN 頂点 MM 辺のグラフにおける頂点 11 から各頂点への最短経路長を、O(MlogN)O(Mlog⁡N) で計算するアルゴリズム"""
mp2=[[2, 4, 2], [3, 4, 5], [3, 2, 1], [1, 3, 2], [2, 0, 8], [0, 2, 8], [1, 2, 4], [0, 1, 3]]

from heapq import heappop, heappush
inf=float('inf')
d=[inf for i in range(5)]
d[0]=0
prev=[None]*5
p=dict()
for i,j,k in mp2: p[i]=p.get(i,[])+[(j,k)]
print(p)

q=[]
heappush(q,(d[0],0))
while q:
    print(q,d,prev)
    du, u = heappop(q)
    if d[u]<du: continue
    for v,weight in p.get(u,[]):
        alt=du+weight
        if d[v]>alt:
            d[v]=alt
            prev[v]=u
            heappush(q, (alt,v))

p=[4]
while prev[p[-1]]!=None: p.append(prev[p[-1]])
print('最短経路',*p[::-1])
print('最短距離',d)

"""ワーシャルフロイド法：すべての2点間の最短距離を求める"""

n=int(input())
#c=[[random.randint(1, 10) for i in range(n)] for i in range(n)]
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

"""逆元を高速に計算するアルゴリズム"""


"""累積和"""
a=list(range(1,30))
a2=[0]
for i in a:a2.append(a2[-1]+i)


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


"""キュー"""


"""ヒープ"""


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