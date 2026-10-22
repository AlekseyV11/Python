n = int(input())
words = set()
for _ in range(n):
    words.add(input().strip())
print(len(words))