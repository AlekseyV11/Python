n = int(input())
letters = [''] * n
for _ in range(n):
    pos, letter = input().split()
    letters[int(pos) - 1] = letter
print(''.join(letters))