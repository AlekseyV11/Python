first = set()
while True:
    line = input().strip()
    if line == "":
        break
    for x in line.split():
        first.add(int(x))

second = set()
while True:
    line = input().strip()
    if line == "":
        break
    for x in line.split():
        second.add(int(x))

common = first & second
if common:
    print(" ".join(map(str, sorted(common))))
else:
    print("EMPTY")