import random, math
from colored import fore, back, style

number = int(math.ceil(random.randint(1,20)))
with open("splashes.txt") as splashes:
    splash = splashes.readlines()
    if number == 1:
        print(random.choice(splash))
    elif number == 2:
        print(fore.BLUE + random.choice(splash) + style.RESET)
    elif number == 3:
        print(fore.GREEN + random.choice(splash) + style.RESET)
    elif number == 4:
        print(fore.RED + random.choice(splash) + style.RESET)
    elif number == 5:
        print(fore.MAGENTA + random.choice(splash) + style.RESET)
    elif number == 6:
        print(fore.YELLOW + random.choice(splash) + style.RESET)
    elif number == 7:
        print(fore.PURPLE_3 + random.choice(splash) + style.RESET)
    elif number == 8:
        print(fore.DARK_GREEN + random.choice(splash) + style.RESET)
    elif number == 9:
        print(fore.PINK_1 + random.choice(splash) + style.RESET)
    elif number == 10:
        print(fore.ORANGE_1 + random.choice(splash) + style.RESET)
    elif number == 11:
        print(fore.CYAN + random.choice(splash) + style.RESET)
    elif number == 12:
        print(fore.TURQUOISE_2 + random.choice(splash) + style.RESET)
    elif number == 13:
        print(fore.GOLD_1 + random.choice(splash) + style.RESET)
    elif number == 14:
        print(fore.SKY_BLUE_1 + random.choice(splash) + style.RESET)
    elif number == 15:
        print(fore.LIGHT_BLUE + random.choice(splash) + style.RESET)
    elif number == 16:
        print(fore.LIGHT_GREEN + random.choice(splash) + style.RESET)
    elif number == 17:
        print(fore.LIGHT_RED + random.choice(splash) + style.RESET)
    elif number == 18:
        print(fore.LIGHT_CORAL + random.choice(splash) + style.RESET)
    elif number == 19:
        print(fore.DARK_RED_1 + random.choice(splash) + style.RESET)
    elif number == 20:
        print(fore.TAN + random.choice(splash) + style.RESET)
