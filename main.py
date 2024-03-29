colors = True # If colored text can be used

import sys
try:
    import math, random
    from colored import fore, back, style
except ImportError:
    colors = False

path = sys.argv
path[0] = str(path[0])[:-7]
if colors == True:
    number = int(math.ceil(random.randint(1,19)))
    with open(str(path[0]) + "splashes.txt") as splashes:
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
            print(fore.TAN + random.choice(splash) + style.RESET)
else:
    with open(str(path[0]) + "splashes.txt") as splashes:
        splash = splashes.readlines()
        print(random.choice(splash))
