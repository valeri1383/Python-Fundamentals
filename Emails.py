class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'


emails = []

line = input()
while line != 'Stop':
    token = line.split(' ', maxsplit=2)
    sender = token[0]
    receiver = token[1]
    content = token[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    line = input()

send_emails = list(map(int, input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())