import os
import time
import random
import Rus
import Eng
from colorama import init  # https://pypi.org/project/colorama/
from colorama import Fore, Back, Style

os.system('cls' if os.name == 'nt' else 'clear')
language = int(input("Язык / language: \n"
                     "1 Ru  \n"
                     "2 Eng \n"))
if language == 1:
    text = Rus
elif language == 2:
    text = Eng
os.system('cls' if os.name == 'nt' else 'clear')
init()
print(Fore.CYAN + Style.DIM + text.rules + Style.RESET_ALL)
input(text.start)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    sp = []
    sp_inp = []
    while sp == list(sp_inp):
        sp.append(random.randint(0, 9))
        print(sp)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        sp_inp = map(int, input(' ').split())
    print(Fore.CYAN + Style.NORMAL + text.error + Style.RESET_ALL + str(sp) +
          '\n' + Fore.GREEN + Style.BRIGHT + text.lvl + str(len(sp) - 1))
    print(Fore.RED + Style.BRIGHT + text.gameover + Style.RESET_ALL)

    file = open('Saves.txt', 'a')
    file.write(' ' + str(len(sp) - 1) + ' lvl ' + input(text.name) + '\n')
    file.close()

    file = open("Saves.txt", "r")
    data = file.readlines()
    print(text.record + '\n\n' + max(data))
    file.close()

    if input(text.repeat) == 'y':
        print()
    else:
        break

    # repeat = (input(text.repeat))
    #
    # if repeat == "y":
    #     print("next")
    # elif repeat == "n":
    #     break
    # else:
    #     break
