import phone_book as pb


def main_menu():
    print()
    print('------------------------------')
    print('Выберите пункт меню: ')
    print('1. Показать телефонную книгу')
    print('2. Сохранить телефонную книгу')
    print('3. Загрузить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения\n')
    return input_menu()


def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice not in range(0, 8):
                print('Такого пункта меню нет.')
            else:
                return choice
        except ValueError:
            print('Ошибка ввода. Введите корректный пункт меню')


def print_phone_book():
    phone_book = pb.get_phone_book()
    if phone_book:
        for id_cont, contact in enumerate(phone_book, 1):
            print(id_cont, *contact)
    else:
        if len(phone_book) < 1:
            print('Телефонная книга пуста или не загружена')
            print('Загрузите телефонную книгу. Пункт 3.')


# def check_phone_book():
#     phone_book = pb.get_phone_book()
#     print()
#     if not phone_book:
#         print('Телефонная книга пуста или не загружена')
#         print('Загрузите телефонную книгу. Пункт 3.')
#     else:
#         return True


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    new_contact = [name, phone, comment]
    return new_contact


def input_remove_contact() -> int:
    print()
    id_cont = int(input('Введите ID контакта to delete: '))
    # pb.remove_contact()
    return id_cont


# Изменение контакта

def input_change_id() -> int:
    print()
    id_cont = int(input('Введите ID контакта to change: '))
    pb.input_change_id(id_cont)
    return id_cont


def change_contact_menu():
    print()
    print('1. Имя')
    print('2. Телефон')
    print('3. Комментарий')
    print('0. Выход из меню "Изменить контакт"')
    return input_change_contact_menu()


def input_change_contact_menu():
    try:
        choice2 = int(input('Введите пункт меню to change: '))
        if choice2 not in range(0, 4):
            print('Такого пункта меню нет.')
        else:
            return choice2  # pb.choose_change(choice2)
    except ValueError:
        print('Ошибка ввода. Введите корректный пункт меню')


def input_change_name():
    changed_name = input('Внесите изменения в имя контакта: ')
    return changed_name


def input_change_phone():
    changed_phone = input('Внесите изменения в телефон контакта: ')
    return changed_phone


def input_change_comment():
    changed_comment = input('Внесите изменения в комментарий к контакту: ')
    return changed_comment


# Поиск контакта

def input_find():
    find_contact = input('Введите контакт to find: ')
    print()
    return find_contact.lower()


# Проверка подтверждения

def input_confirm():
    while True:
        try:
            confirm = input('Подтвердить? (y/n)')
            conf = ['y', 'n']
            if confirm.lower() not in conf:
                print('Для подтверждения выбранного действия введите y, для отмены - n')
            else:
                return confirm
        except ValueError:
            print('Ошибка ввода. Введите корректный пункт меню')
