n, m = tuple([int(x) for x in input().split()])

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

set_intersec = n_set & m_set

for el in set_intersec:
    print(el)
