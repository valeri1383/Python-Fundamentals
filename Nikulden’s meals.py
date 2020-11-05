command = input()
guest_dict = {}
disliked_dishes = []
while command != 'Stop':
    token = command.split('-')

    if token[0] == 'Like':
        guest = token[1]
        meal = token[2]
        if guest not in guest_dict:
            guest_dict[guest] = []

        if meal not in guest_dict[guest]:
            guest_dict[guest].append(meal)

    elif token[0] == 'Unlike':
        guest = token[1]
        meal = token[2]
        if guest not in guest_dict:
            print(f"{guest} is not at the party.")
        else:
            if meal not in guest_dict[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                disliked_dishes.append(meal)
                guest_dict[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")

    command = input()

sorted_guest = sorted(guest_dict.keys(), key=lambda x: (-len(guest_dict[x]), x))
for i in sorted_guest:
    print(f"{i}: {', '.join(guest_dict[i])}")
print(f"Unliked meals: {len(disliked_dishes)}")