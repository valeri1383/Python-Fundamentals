capacity = int(input())
command = input()
message_dict = {}
while command != 'Statistics':
    token = command.split('=')

    if token[0] == 'Add':
        username = token[1]
        sent = int(token[2])
        received = int(token[3])
        if username not in message_dict:
            message_dict[username] = {}
            message_dict[username]['sent'] = sent
            message_dict[username]['received'] = received

    elif token[0] == 'Message':
        sender = token[1]
        receiver = token[2]
        if sender in message_dict and receiver in message_dict:
            message_dict[sender]['sent'] += 1
            message_dict[receiver]['received'] += 1
            if message_dict[sender]['sent'] + message_dict[sender]['received'] == capacity:
                print(f"{sender} reached the capacity!")
                del message_dict[sender]
            if message_dict[receiver]['sent'] + message_dict[receiver]['received'] == capacity:
                del message_dict[receiver]
                print(f"{receiver} reached the capacity!")

    elif token[0] == 'Empty':
        username = token[1]
        if username in message_dict:
            del message_dict[username]
        if username == 'All':
            del message_dict
            message_dict = {}

    command = input()

sorted_message = sorted(message_dict.keys(), key=lambda x: (-message_dict[x]['received'], x))
print(f'Users count: {len(sorted_message)}')
for i in sorted_message:
    print(f"{i} - {message_dict[i]['received'] + message_dict[i]['sent']}")