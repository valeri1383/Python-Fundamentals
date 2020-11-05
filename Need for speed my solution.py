n = int(input())
cars_dict = {}
for i in range(n):
    token = input().split('|')
    car = token[0]
    mileage = int(token[1])
    fuel = int(token[2])
    if car not in cars_dict:
        cars_dict[car] = {}
    cars_dict[car]['mileage'] = mileage
    cars_dict[car]['fuel'] = fuel

command = input()
while command != 'Stop':
    token_2 = command.split(' : ')

    if token_2[0] == 'Drive':
        car = token_2[1]
        distance = int(token_2[2])
        needed_fuel = int(token_2[3])

        if cars_dict[car]['fuel'] < needed_fuel:
            print('Not enough fuel to make that ride')
        if cars_dict[car]['fuel'] >= needed_fuel:
            cars_dict[car]['mileage'] += distance
            cars_dict[car]['fuel'] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if cars_dict[car]['mileage'] >= 100000:
            print(f'Time to sell the {car}!')
            del cars_dict[car]

    elif token_2[0] == 'Refuel':
        car = token_2[1]
        fuel = int(token_2[2])
        fuel_difference = 0
        if cars_dict[car]['fuel'] + fuel > 75:
            fuel_difference = 75 - cars_dict[car]['fuel']
            cars_dict[car]['fuel'] = 75
        else:
            fuel_difference = fuel
            cars_dict[car]['fuel'] += fuel
        print(f'{car} refueled with {fuel_difference} liters')


    elif token_2[0] == 'Revert':
        car = token_2[1]
        kilometers = int(token_2[2])
        if cars_dict[car]['mileage'] - kilometers < 10000:
            cars_dict[car]['mileage'] = 10000
        else:
            cars_dict[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_cars = sorted(cars_dict.keys(), key=lambda u: (-cars_dict[u]['mileage'], u))

for x in sorted_cars:
    print(f"{x} -> Mileage: {cars_dict[x]['mileage']} kms, Fuel in the tank: {cars_dict[x]['fuel']} lt.")