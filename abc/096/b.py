A, B, C = map(int, input().split())
K = int(input())

m = max(A, B, C)
print(sum([A, B, C]) - m + m * (2 ** K))