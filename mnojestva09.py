m = int(input())
available = set()
for _ in range(m):
    available.add(input().strip())

n = int(input())
cooked = set()
for _ in range(n):
    line = input().strip()
    for dish in line.split():
        cooked.add(dish)

never = available - cooked
for dish in sorted(never):
    print(dish)