import os
from colorama import Fore


def clear():
    os.system('cls||clear')


def render_menu(contex=None, color=Fore.WHITE):
    [print(f'{color}{key}: {values}') for key, values in contex.items()]
    return input("Выберите значение: ")


def render_message_input(context=None):
    clear()
    return input(context)


def render_message(context=None, color=Fore.WHITE):
    clear()
    print(color, context)

def out_red(context=None, color=Fore.RED):
    clear()
    print(color, context)
