import os
import time
import random
from colorama import init
from colorama import Fore, Back, Style

init()
while True:
    os.system('cls')
    print("\n    Запомни последовательность чисел за 3 секунд,\n"
          " после введи их через пробел.\n")
    sp = []
    sp_inp = []
    while sp == list(sp_inp):
        sp.append(random.randint(0, 9))
        print(sp)
        time.sleep(3)  # полностью останавливает программу на 3 сек
        os.system('cls')
        sp_inp = map(int, input(' ').split())
    # os.system('cls')
    print(Fore.CYAN + Style.NORMAL + '\nТы ошибся!\n'
                                     'Правильно: ' + Style.RESET_ALL + str(
        sp) + '\n' + Fore.GREEN + Style.BRIGHT + "\nТвой LVL = " + str(len(sp) - 1))
    print(Fore.RED + Style.BRIGHT + "\n### GAME OVER! ###" + Style.RESET_ALL)
    # a = input()
    if input('\nПовторить?(y/n)') == 'n':
        break
