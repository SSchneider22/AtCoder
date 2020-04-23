import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
a = list(map(int, input().replace("\n","").split()))

"""
for i in range(1,n+1):
    print(a.count(i))
"""

S = Counter(a)

for i in range(1,n+1):
    print(S[i])




"""
from collections import Counter
l=['a','b','b','c','b','a','c','c','b','c','b','a']
S=Counter(l)#カウンタークラスが作られる。S=Counter({'b': 5, 'c': 4, 'a': 3})
print(S.most_common(2)) #[('b', 5), ('c', 4)]
print(S.keys()) #dict_keys(['a', 'b', 'c'])
print(S.values()) #dict_values([3, 5, 4])
print(S.items()) #dict_items([('a', 3), ('b', 5), ('c', 4)])

"""