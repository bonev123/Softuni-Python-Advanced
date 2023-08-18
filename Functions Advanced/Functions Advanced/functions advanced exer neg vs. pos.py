

nums = [int(x) for x in input().split()]

positives = [num for num in nums if num >= 0]
negatives = [num for num in nums if not num >= 0]

sum_pos = sum(positives)
sum_neg = sum(negatives)

print(sum_neg)
print(sum_pos)
if abs(sum_neg) > sum_pos:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")




