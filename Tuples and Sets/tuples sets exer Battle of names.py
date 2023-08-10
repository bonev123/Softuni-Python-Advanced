n = int(input())

odd_nums, even_nums = set(), set()

for i in range(n):
    name = input()
    result = 0
    for letter in name:

        result += ord(letter)
    result = result // (i + 1)

    if result % 2 == 0:
        even_nums.add(result)
    else:
        odd_nums.add(result)
odd_sum = sum(odd_nums)
even_sum = sum(even_nums)

if odd_sum == even_sum:
    result = odd_nums.union(even_nums)
elif odd_sum < even_sum:
    result = odd_nums.symmetric_difference(even_nums)
else:
    result = odd_nums.difference(even_nums)
print(', '.join([str(x) for x in result]))

