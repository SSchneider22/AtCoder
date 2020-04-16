import sys
input = sys.stdin.readline  # 改行コード「\n」を呼んでしまうため、文字数など、注意！！

n = str(input().replace("\n",""))

if '7' in n:
    print('Yes')
else:
    print('No')