INF = 10 ** 9 + 7
N, K = map(int, input().split())


def create_factorial(n):
    """
    階乗を事前計算した配列を作成します。
    :param n: [0, n]の配列を作成します
    """
    f = list()
    for i in range(n + 1):
        if i in [0, 1]:
            f.append(1)
        else:
            f.append(f[i - 1] * i)
    return f


def combination(n, m, factorial):
    """
    nCmの値を計算します。
    nCm = n! / (m! * (n-m)!) より階乗計算が必要なため、階乗を事前に計算して渡してください。
    """
    if n == m:
        return 1
    else:
        return factorial[n] // factorial[m] // factorial[n - m]


f = create_factorial(2000)

for i in range(1, K + 1):
    print(combination(N - K + 1, i, f) * combination(K - 1, i - 1, f) % INF)