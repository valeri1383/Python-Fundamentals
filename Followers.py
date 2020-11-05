command = input()
followers_dict = {}

while command != 'Log out':
    token = command.split(': ')
    username = token[1]

    if token[0] == 'New follower':
        if username not in followers_dict:
            followers_dict[username] = {}
            followers_dict[username]['likes'] = 0
            followers_dict[username]['comments'] = 0

    elif token[0] == 'Like':
        count = int(token[2])
        if username not in followers_dict:
            followers_dict[username] = {}
            followers_dict[username]['likes'] = 0
            followers_dict[username]['comments'] = 0
            followers_dict[username]['likes'] = count
        else:
            followers_dict[username]['likes'] += count

    elif token[0] == 'Comment':
        if username not in followers_dict:
            followers_dict[username] = {}
            followers_dict[username]['likes'] = 0
            followers_dict[username]['comments'] = 1
        else:
            followers_dict[username]['comments'] += 1

    elif token[0] == 'Blocked':
        if username in followers_dict:
            del followers_dict[username]
        else:
            print(f"{username} doesn't exist.")

    command = input()

sorted_followers = sorted(followers_dict.keys(), key=lambda x: (-followers_dict[x]['likes'], x))
print(f"{len(sorted_followers)} followers")

for i in sorted_followers:
    print(f"{i}: {followers_dict[i]['likes'] + followers_dict[i]['comments']}")