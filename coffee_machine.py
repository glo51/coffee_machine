level = {
    'water': 400,
    'milk': 540,
    'beans': 120,
    'cups': 9,
    'money': 550
}


def print_level():
    print('\nThe coffee machine has:')
    print(f"{level['water']} of water")
    print(f"{level['milk']} of milk")
    print(f"{level['beans']} of coffee beans")
    print(f"{level['cups']} of disposable cups")
    print(f"{level['money']} of money\n")


def fill():
    level['water'] += int(input('Write how many ml of water do you want to add: '))
    level['milk'] += int(input('Write how many ml of milk do you want to add: '))
    level['beans'] += int(input('Write how many grams of coffee do you want to add: '))
    level['cups'] += int(input('Write how many disposable cups of coffee do you want to add: '))


def buy(coffee_type):
    if level['cups'] > 0:
        if coffee_type == 'espresso':
            if level['water'] - 250 >= 0 and level['beans'] - 16 >= 0:
                level['water'] -= 250
                level['beans'] -= 16
                level['money'] += 4
                level['cups'] -= 1
                print('I have enough resources, making you a coffee!')
            else:
                print('Not enough ingredients')
        elif coffee_type == 'latte':
            if level['water'] - 350 >= 0 and level['milk'] - 75 >= 0 and level['beans'] - 20 >= 0:
                level['water'] -= 350
                level['milk'] -= 75
                level['beans'] -= 20
                level['money'] += 7
                level['cups'] -= 1
                print('I have enough resources, making you a coffee!')
            else:
                print('Not enough ingredients')
        else:
            if level['water'] - 200 >= 0 and level['milk'] - 100 >= 0 and level['beans'] - 12 >= 0:
                level['water'] -= 200
                level['milk'] -= 100
                level['beans'] -= 12
                level['money'] += 6
                level['cups'] -= 1
                print('I have enough resources, making you a coffee!')
            else:
                print('Not enough ingredients')
    else:
        print('Not enough cups')


while True:
    answer = input('Write action (buy, fill, take, remaining, exit): ')
    if answer == 'buy':
        answer = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if answer == '1':
            buy('espresso')
        elif answer == '2':
            buy('latte')
        elif answer == '3':
            buy('cappuccino')
        elif answer == 'back':
            continue
        else:
            print('You typed in wrong option')
    elif answer == 'fill':
        fill()
    elif answer == 'take':
        print(f"I gave you ${level['money']}")
        level['money'] = 0
    elif answer == 'remaining':
        print_level()
    elif answer == 'exit':
        break
    else:
        print('You typed in wrong option')
