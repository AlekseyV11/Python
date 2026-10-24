n = int(input())
people = []
for _ in range(n):
    name, height = input().split()
    people.append((int(height), name))
people.sort(reverse=True)
for height, name in people:
    print(name, height)