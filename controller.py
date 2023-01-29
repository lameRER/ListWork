from view import render_menu, render_message, render_message_input, out_red
from colorama import Fore

menu_dict = {
    1: 'Демонстрация списка',
    2: 'Добавить элемент в список',
    3: 'Удалить элемента из списка',
    4: 'Выход'
}

ls = []


def default_controller():
    return render_menu(menu_dict)


def get_item():
    render_message(ls, Fore.GREEN)
    return None, None

def add():
    inp = render_menu({1: 'Добавить элемент в конец списка', 2: 'Добавить элемент по индексу'})
    controller = get_controller(inp, controller_add_dict)
    controller()
    return None, None

def add_item():
    inp = render_message_input("Введите значение: ")
    ls.append(inp)
    render_message('Элемент добавлен в конец списка', Fore.GREEN)
    return None, None

def add_item_index():
    index, value = render_message_input("Введите индекс и значение(через пробел): ").split()
    ls.insert(int(index), value)
    render_message('Элемент добавлен по указанному индексу', Fore.GREEN)
    return None, None



def remove():
    inp = render_menu({1: 'Удалить последний элемент в списке', 2: 'Удалить элемент по индексу'})
    controller = get_controller(inp, controller_remove_dict)
    controller()
    return None, None

def remove_item_index():
    index = render_message_input("Введите индекс: ")
    ls.pop(int(index))
    render_message('Удалент элемент из писка по индексу', Fore.GREEN)

def remove_item():
    ls.pop()
    render_message('Последний элемент списка удален', Fore.GREEN)
    return None, None


def get_controller(state, menu_dict=None):
    if menu_dict is None:
        menu_dict = controller_dict
    if state in menu_dict.keys() or state is None:
        return menu_dict.get(state, default_controller)
    else:
        out_red('Введено неверное значение!!!')
        return controller_dict.get(state, default_controller)



controller_dict = {
    '1': get_item,
    '2': add,
    '3': remove,
    '4': exit
}

controller_add_dict = {
    '1': add_item,
    '2': add_item_index
}

controller_remove_dict = {
    '1': remove_item,
    '2': remove_item_index
}
