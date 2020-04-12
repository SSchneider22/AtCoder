# https://atcoder.jp/contests/abc095/tasks/arc096_a

a, b, c, x, y = map(int, input().replace("\n","").split())
ans = 0

for i in range(0,100001):
    tmp = 2*c*i + max(0,x-i)*a + max(0,y-i)*b
    if ans == 0 or tmp < ans:
        ans = tmp

print(ans)


"""
# ABミックス（C円）2枚が、A1枚よりも安く、B1枚よりも安いか？⇒安いならば、すべてABミックスでそろえる
if (2*c < a) and (2*c < b):
    if x > y:

    elif x < y:

    elif x == y:


# ABミックス（C円）2枚が、A1枚よりも安いか？⇒安いならば、AはすべてABミックスでそろえる
elif 2*c < a:

# ABミックス（C円）2枚が、B1枚よりも安いか？⇒安いならば、BはすべてABミックスでそろえる
elif 2*c < b:
"""











"""
【解説】
まず、AB ピザを奇数枚買って 1 枚余らせるのは無意味なので、AB ピザは 2 枚 1 組で考えます。つまり、
2C 円で A ピザ 1 枚と B ピザ 1 枚を買えると考えることにし、この 2 枚の組み合わせをこれ以降 AB セッ
トと呼ぶことにします。
この問題の重要な制約は、X, Y ≤ 105 です。これは、A ピザ、B ピザ、AB セットのどれについても、買
う個数は 10 万個以下でよいことを意味します。したがって、この三種類のうちどれか一種類を選んで、それ
を買う個数を 0 から 10 万まですべて試す、という方針が考えられます。*4
さて、三つのうちどれについて購入個数を全列挙するべきでしょうか？結論を述べると、AB セットです。
AB セットを i 個 (0 ≤ i ≤ 105
) 購入した場合、i ≥ X であれば A ピザを買い増す必要はなく、i < X であれ
ば A ピザを X −i 枚買い増す必要があります。これらをまとめて、買い増すべき A ピザの数は max(0, X −i)
枚であるということもできます。同様に、B ピザを max(0, Y − i) 枚買い増す必要があります。以上から、
AB セットを i 枚購入した場合の所要金額は i × 2C + max(0, X − i) × A + max(0, Y − i) × B 円であり、こ
の値を 0 以上 10 万以下のすべての整数 i について計算して最小値を取ることで答えが求まります。
なお、定数時間で答えを求めることもできます。練習問題として解説は省きます。


*4 なお、二種類を選んでしまうと考慮する可能性の数が約 100 億通りになり、2018 年現在の一般的な計算機が 2 秒で探索するには
厳しいです。今日の一般的な計算機が 1 秒あたりに処理できる式の数はおよそ 1 億個といったところで、短い単純な式であれば
10 億個程度まで伸び、逆に実数の割り算など複雑な演算を伴う場合は数千万個程度に落ちます。

"""