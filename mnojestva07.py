n = int(input())
surnames = []
for _ in range(n):
    surnames.append(input().strip())

seen = set()
repeated = set()
for s in surnames:
    if s in seen:
        repeated.add(s)
    else:
        seen.add(s)

# количество людей с повторяющимися фамилиями
count = sum(1 for s in surnames if s in repeated)
print(count)