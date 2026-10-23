s = input()
vowels = 'аеёиоуыэюя'
count = 0
for c in s:
    if c in vowels:
        count += 1
print(count)