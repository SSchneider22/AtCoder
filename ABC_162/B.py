import sys
input = sys.stdin.readline  # 改行コード「\n」を呼んでしまうため、文字数など、注意！！

n = int(input().replace("\n",""))

anslist = []

for i in range(1, n+1):
    # print(i)
    if i % 15 == 0:
        continue
        # print('FizzBuzz', end=' ')
    elif i % 3 == 0:
        continue
        # print('Fizz', end=' ')
    elif i % 5 == 0:
        continue
        # print('Buzz', end=' ')
    else:
        anslist.append(i)
        # print(i, end=' ')

print(sum(anslist))