num = 0
found_num = -1
while True:
    s = input()
    if s == 'СТОП':
        break
    num += 1
    if ('кот' in s or 'Кот' in s) and found_num == -1:
        found_num = num
print(found_num)