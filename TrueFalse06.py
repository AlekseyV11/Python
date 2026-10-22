total = 0
count = 0
found = -1
while True:
    n = int(input())
    if n == 0:
        break
    total += n
    count += 1
    if total == 10 and found == -1:
        found = count
print(found)