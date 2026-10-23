shift = int(input())
s = input()
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
result = ''
for c in s:
    if c in alphabet:
        idx = alphabet.index(c)
        new_idx = (idx + shift) % 33
        result += alphabet[new_idx]
    else:
        result += c
print(result)