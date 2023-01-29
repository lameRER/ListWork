from view import render_menu, render_message, render_message_input, out_red
from colorama import Fore

menu_dict = {
    1: 'Демонстрация списка',
    2: 'Добавление элемента в конец списка',
    3: 'Удаление последнего элемента из списка',
    4: 'Выход'
}

ls = []


def default_controller():
    return render_menu(menu_dict)


def get_item():
    render_message(ls, Fore.GREEN)
    return None, None


def add_item():
    inp = render_message_input("Введите значение: ")
    ls.append(inp)
    render_message('Элемент добавлен в конец списка', Fore.GREEN)
    return None, None


def remove_item():
    ls.pop()
    render_message('Последний элемент списка удален', Fore.GREEN)
    return None, None


def get_controller(state):
    if state in controller_dict.keys() or state is None:
    # print(state)
        return controller_dict.get(state, default_controller)
    else:
        out_red('Введено неверное значение!!!')
        return controller_dict.get(state, default_controller)



controller_dict = {
    '1': get_item,
    '2': add_item,
    '3': remove_item,
    '4': exit
}
