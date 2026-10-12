print('Ты любишь Python? (да/нет)')
answer1 = input()
print('Ты уже решал задачи на условия? (да/нет)')
answer2 = input()

if answer1 == 'да' and answer2 == 'да':
    print('Ты уже почти профи!')
elif answer1 == 'да' and answer2 == 'нет':
    print('Отличное начало, продолжай в том же духе!')
elif answer1 == 'нет' and answer2 == 'да':
    print('Странно, но интересно...')
else:
    print('Самое время начать учить Python!')