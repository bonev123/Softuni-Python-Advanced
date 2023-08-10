n = int(input())

set = set()
for _ in range(n):
    command = input().split()
    for el in command:
        set.add(el)

print(f"\n".join(set))