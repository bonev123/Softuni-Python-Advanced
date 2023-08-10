n, m = tuple([int(x) for x in input().split()])

n_set = set()
m_set = set()

for i in range(n):
    n_set.add(input())
for i in range(m):
    m_set.add(input())
set_intersec = n_set & m_set

for num in set_intersec:
    print(num)