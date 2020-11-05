n = int(input())
hero_dict = {}
for i in range(n):
    token = input().split(' ')
    hero_name = token[0]
    HP = int(token[1])
    MP = int(token[2])
    hero_dict[hero_name] = {}
    hero_dict[hero_name]['HP'] = HP
    hero_dict[hero_name]['MP'] = MP

command = input()
while command != 'End':
    token_2 = command.split(' - ')
    hero_name = token_2[1]

    if token_2[0] == 'CastSpell':
        MP_needed = int(token_2[2])
        spell_name = token_2[3]
        if hero_dict[hero_name]['MP'] >= MP_needed:
            hero_dict[hero_name]['MP'] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif token_2[0] == 'TakeDamage':
        damage = int(token_2[2])
        attacker = token_2[3]
        if hero_dict[hero_name]['HP'] - damage > 0:
            hero_dict[hero_name]['HP'] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['HP']} HP left!")
        else:
            del hero_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif token_2[0] == 'Recharge':
        amount = int(token_2[2])
        amount_recovered = 0
        if hero_dict[hero_name]['MP'] + amount >= 200:
            amount_recovered = 200 - hero_dict[hero_name]['MP']
            hero_dict[hero_name]['MP'] = 200
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        else:
            hero_dict[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif token_2[0] == 'Heal':
        amount = int(token_2[2])
        amount_recovered = 0
        if hero_dict[hero_name]['HP'] + amount >= 100:
            amount_recovered = 100 - hero_dict[hero_name]['HP']
            hero_dict[hero_name]['HP'] = 100
            print(f"{hero_name} healed for {amount_recovered} HP!")
        else:
            hero_dict[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")

    command = input()

sorted_heros = sorted(hero_dict.keys(), key=lambda x: (-hero_dict[x]['HP'], x))

for x in sorted_heros:
    print(x)
    print(f"  HP: {hero_dict[x]['HP']}")
    print(f"  MP: {hero_dict[x]['MP']}")