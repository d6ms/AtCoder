N, K = map(int, input().split())

# a+b, b+c, c+a が全てKの倍数になるのは、
# 1. (a%K, b%K, c%K) = (0, 0, 0)
# 2. (a%K, b%K, c%K) = (K/2, K/2, K/2) の時だけ
# このうち、2の条件はKが奇数の時成立しないので、Kの偶奇で分けてそれぞれの条件を考える

# 1の条件: a, b, c は N以下のKの倍数 なので、その個数の3乗
cnt = int(N / K) ** 3

# 2の条件: N以下のKで割ってK/2余る数 = N+K/2以下のKの倍数 の個数の3乗
if K % 2 == 0:
    cnt += int((N + K / 2) / K) ** 3

print(cnt)
