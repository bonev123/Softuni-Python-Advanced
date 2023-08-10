n = int(input())
guest_list = set()
attended = set()

for _ in range(n):
    num = input()
    guest_list.add(num)


while True:
    command = input()
    if command == 'END':
        break
    attended.add(command)

unattended = guest_list - attended
print(len(unattended))
print(f"\n".join(sorted(unattended)))