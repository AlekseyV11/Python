n = int(input())
nums = [int(input()) for _ in range(n)]
target = nums[-1]
found = False
for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if nums[i] * nums[j] == target:
            found = True
            break
    if found:
        break
print('ДА' if found else 'НЕТ')