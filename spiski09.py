whitelist = []
while True:
    s = input()
    if s == '':
        break
    whitelist.append(s)

while True:
    query = input()
    if query == '':
        break
    if query in whitelist:
        print(query)