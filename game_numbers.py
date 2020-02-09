import os
import time
import random
from colorama import init  #https://pypi.org/project/colorama/
from colorama import Fore, Back, Style

init()
while True:
    os.system('cls')
    print("\n    Запомни последовательность чисел за 3 секунды,\n"
          " после введи их через пробел.\n")
    input("Для начала игры нажминте <ENTER>")
    os.system('cls')
    sp = []
    sp_inp = []
    while sp == list(sp_inp):
        sp.append(random.randint(0, 9))
        print(sp)
        time.sleep(3)
        os.system('cls')
        sp_inp = map(int, input(' ').split())
    # os.system('cls')
    print(Fore.CYAN + Style.NORMAL + '\nТы ошибся!\n'
                                     'Правильно: ' + Style.RESET_ALL + str(sp) + '\n' + Fore.GREEN + Style.BRIGHT + "\nТвой LVL = " + str(len(sp) - 1))
    print(Fore.RED + Style.BRIGHT + "\n### GAME OVER! ###" + Style.RESET_ALL)
    # a = input()
    if input('\nПовторить?(y/n)') == 'n':
        break
