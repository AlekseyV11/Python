n = int(input())
nums = [int(input()) for _ in range(n)]
result = []
for i in range(n - 1):
    result.append(str(nums[i] + nums[i + 1]))
print(' '.join(result))