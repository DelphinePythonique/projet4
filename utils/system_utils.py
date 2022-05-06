from os import system, name as os_name


def clear_screen():
    if os_name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
