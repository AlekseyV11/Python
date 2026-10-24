n = int(input())
nums = [int(input()) for _ in range(n)]
result = [str(x * 3) for x in nums]
print(' '.join(result))