n = int(input())

names = set()

for _ in range(n):
    name = input()
    names.add(name)
print(f"\n".join(names))