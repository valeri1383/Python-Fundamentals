command = input()
city_dict = {}
while command != 'Sail':
    token = command.split('||')
    city = token[0]
    population = int(token[1])
    gold = int(token[2])
    if city not in city_dict:
        city_dict[city] = {}
        city_dict[city]['population'] = population
        city_dict[city]['gold'] = gold
    else:
        city_dict[city]['population'] += population
        city_dict[city]['gold'] += gold

    command = input()

new_command = input()
while new_command != 'End':
    new_token = new_command.split('=>')
    action = new_token[0]
    town = new_token[1]
    if action == 'Plunder':
        people = int(new_token[2])
        gold = int(new_token[3])
        city_dict[town]['population'] -= people
        city_dict[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if city_dict[town]['population'] <= 0 or city_dict[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del city_dict[town]

    elif action == 'Prosper':
        gold = int(new_token[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_dict[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_dict[town]['gold']} gold.")

    new_command = input()

sorted_city = sorted(city_dict.keys(), key=lambda x: (-city_dict[x]['gold'], x))
print(f'Ahoy, Captain! There are {len(sorted_city)} wealthy settlements to go to:')
if len(sorted_city) > 0:
    for x in sorted_city:
        print(f"{x} -> Population: {city_dict[x]['population']} citizens, Gold: {city_dict[x]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")