n = int(input())

unique_users = set()

for _ in range(n):
    username = input()
    unique_users.add(username)

for username in unique_users:
    print(username)
