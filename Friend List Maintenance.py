friends_list = input().split(', ')
command = input()
blacklisted = []
lost = []

while command != 'Report':
    token = command.split(' ')

    if token[0] == 'Blacklist':
        name = token[1]
        if name in friends_list:
            blacklisted.append(name)
            idx = friends_list.index(name)
            print(f"{name} was blacklisted.")
            friends_list[idx] = 'Blacklisted'
        else:
            lost.append(name)
            print(f"{name} was not found." )

    elif token[0] == 'Error':
        idx = int(token[1])
        if friends_list[idx] != 'Blacklisted' and friends_list[idx] != 'Lost':
            print(f'{friends_list[idx]} was lost due to an error.')
            lost.append(friends_list[idx])
            friends_list[idx] = 'Lost'

    elif token[0] == 'Change':
        idx = int(token[1])
        new_name = token[2]
        if 0 <= idx < len(friends_list):
            current_name = friends_list[idx]
            print(f"{current_name} changed his username to {new_name}.")
            friends_list[idx] = new_name


    command = input()

print(f"Blacklisted names: {len(blacklisted)}")
print(f"Lost names: {len(lost)}")
print(f" ".join(friends_list))
