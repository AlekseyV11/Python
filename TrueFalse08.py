found = False
while True:
    s = input()
    if s == 'СТОП':
        break
    if 'пёс' in s or 'Пёс' in s:
        found = False
    elif 'кот' in s or 'Кот' in s:
        found = True
if found:
    print('МЯУ')
else:
    print('НЕТ')