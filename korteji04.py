n = int(input())
words = [input() for _ in range(n)]
for w in sorted(words, key=lambda x: (len(x), x)):
    print(w)