m = int(input())
english = set()
for _ in range(m):
    english.add(input().strip())

n = int(input())
german = set()
for _ in range(n):
    german.add(input().strip())

only_one = (english - german) | (german - english)
if only_one:
    print(len(only_one))
else:
    print("NO")