password = input()
confirm = input()
if len(password) < 8:
    print('Слишком короткий!')
elif password != confirm:
    print('Пароли не совпадают!')
else:
    print('OK')