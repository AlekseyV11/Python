n = int(input())
cities = set()
for _ in range(n):
    cities.add(input().strip())

new_city = input().strip()
if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")