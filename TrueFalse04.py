num = 0
count = 0
first = -1
while True:
    s = input()
    if s == 'СТОП':
        break
    num += 1
    if 'кот' in s or 'Кот' in s:
        count += 1
        if first == -1:
            first = num
print(count)
print(first)