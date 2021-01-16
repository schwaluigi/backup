import random

def attack(attack_power, percent_to_hit, percent_to_critical):
    """calc dmg based on atk pwr and % to hit

    Parameters:
    attack_power - atk pwr
    percent_to_hit - % to hit

    Optional:
    percent_to_critical - % to crit (default 0.01)

    Returns:
        rtrns dmg    
    """
    damage_value = 0
    critical_strike = 2 * attack_power

    # calc if creture was hit
    chance_to_hit = random.random()
    if chance_to_hit <= percent_to_hit:
        creature_was_hit = True
        damage_value = random.randint(1, attack_power)
        if chance_to_hit <= percent_to_critical:
            print('crit!')
            damage_value = attack_power + damage_value
    else:
        creature_was_hit = False
    
    return damage_value


def print_attack(attack_power, percent_to_hit, percent_to_critical, attack_number):
    print('\natking...')
    for i in range(attack_number):
        print(attack(attack_power, percent_to_hit, percent_to_critical))
    i = input('\natk agn? (y/N) ')
    if i == 'y':
        print_attack(attack_power, percent_to_hit, percent_to_critical, attack_number)


attack_power = int(input('wht is atk pwr? '))
percent_to_hit = float(input('wht is % to hit? '))
percent_to_critical = float(input('wht is % to crit? '))
attack_number = int(input('wht is # of atks? '))
#attack_power = 100
#percent_to_hit = .8
#percent_to_critical = .1

print_attack(attack_power, percent_to_hit, percent_to_critical, attack_number)

"""Describe the function purpose

Parameters:
argument0 - described
argument1 - described

Returns:
Describe what is returned
"""
