nums = [int(el) for el in input().split(',')]

ans = [1]
cur = 1
for i in range(1, len(nums)):
    cur *= nums[i - 1]
    ans.append(cur)
cur = 1
for i in range(len(nums) - 2, -1, -1):
    cur *= nums[i + 1]
    ans[i] = ans[i] * cur

print(ans)