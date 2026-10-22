a = set(map(int, input().split()))
b = set(map(int, input().split()))

symm = a ^ b
if symm:
    print(" ".join(map(str, sorted(symm))))
else:
    print("EMPTY")