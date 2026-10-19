while True:
    password = input()
    confirm = input()
    if len(password) < 8:
        print('Слишком короткий!')
    elif '123' in password:
        print('Содержит 123!')
    elif password != confirm:
        print('Пароли не совпадают!')
    else:
        print('OK')
        break