n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
for x in a:
    print(x)