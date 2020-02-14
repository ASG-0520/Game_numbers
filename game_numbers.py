import os
import time
import random
from colorama import init  # https://pypi.org/project/colorama/
from colorama import Fore, Back, Style

init()
print(Fore.CYAN + Style.DIM + "\n    Запомни последовательность чисел за 3 секунды,\n"
                              " как экран очистится введи их через пробел.\n" + Style.RESET_ALL)
input(" Для начала игры нажмите <ENTER>")

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
    print(Fore.CYAN + Style.NORMAL + '\nТы ошибся!\n'
                                     'Правильно: ' + Style.RESET_ALL + str(sp) +
          '\n' + Fore.GREEN + Style.BRIGHT + "\nТвой LVL = " + str(len(sp) - 1))
    print(Fore.RED + Style.BRIGHT + "\n### GAME OVER! ###" + Style.RESET_ALL)
    if input('\nПовторить?(y/n)') == 'n':
        break
