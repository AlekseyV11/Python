s = input()
n = int(input())
if 1 <= n <= len(s):
    print(s[n - 1])
else:
    print('ОШИБКА')