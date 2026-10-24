n = int(input())
nums = [int(input()) for _ in range(n)]
p = int(input())
q = int(input())
print(sum(nums[p:q + 1]))