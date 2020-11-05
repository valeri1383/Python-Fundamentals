command = input()
username_dict = {}
while command != 'Statistics':
    token = command.split('->')
    username = token[1]

    if token[0] == 'Add':
        if username in username_dict:
            print(f"{username} is already registered")
        else:
            username_dict[username] = []

    elif token[0] == 'Send':
        email = token[2]
        username_dict[username].append(email)

    elif token[0] == 'Delete':
        if username not in username_dict:
            print(f"{username} not found!")
        else:
            del username_dict[username]

    command = input()

sorted_users = sorted(username_dict.keys(), key=lambda x: (-len(username_dict[x]), x))
print(f'Users count: {len(sorted_users)}')
for i in sorted_users:
    print(i)
    for x in username_dict[i]:
        print(f" - {x}")