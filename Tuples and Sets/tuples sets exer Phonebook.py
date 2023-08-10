phonebook = {}

user_number = input()

while not user_number.isdigit():
    user_number = user_number.split('-')
    user, number = user_number
    if user not in phonebook:
        phonebook[user] = 0
    phonebook[user] = number
    user_number = input()
else:
    for i in range(int(user_number)):
        user_calling = input()
        if user_calling in phonebook:
            print(f"{user_calling} -> {phonebook[user_calling]}")
        else:
            print(f"Contact {user_calling} does not exist.")