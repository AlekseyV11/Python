m = int(input())
library = set()
for _ in range(m):
    library.add(input().strip())

n = int(input())
for _ in range(n):
    book = input().strip()
    print("YES" if book in library else "NO")