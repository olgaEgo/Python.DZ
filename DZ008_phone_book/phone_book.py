import view

phone_book = []


def get_phone_book() -> list:
    global phone_book
    return phone_book


def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book


def add_contact():
    global phone_book
    if len(phone_book) > 1:
        print('Вы хотите добавить контакт.')
        while True:
            if view.input_confirm() == 'y':
                contact = view.input_new_contact()
                phone_book.append(contact)
                print('Новый контакт добавлен.')
                print('Добавить еще один контакт?')
            else:
                print('!!! Обязательно сохраните телефонную книгу. Пункт 2.')
                break
    else:
        print('Телефонная книга пуста или не загружена.')
        print('!!! Загрузите телефонную книгу. Пункт 3.')


def input_change_id(id_cont_int) -> int:
    global phone_book
    try:
        id_cont = int(id_cont_int)
        if id_cont > len(phone_book) + 1:
            print('Контакта с таким ID нет')
        else:
            return id_cont
    except ValueError:
        print('Ошибка ввода. Введите корректный пункт меню')


def remove_contact():
    global phone_book
    if len(phone_book) > 1:
        print('Вы хотите удалить контакт.')
        while True:
            if view.input_confirm() == 'y':
                print()
                view.print_phone_book()
                id_cont = view.input_remove_contact()
                if id_cont < len(phone_book) + 1:
                    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id_cont - 1][0]}? (y/n)')
                    if confirm.lower() == 'y':
                        print(f'Контакт {phone_book[id_cont - 1][0]} удалён.')
                        phone_book.pop(id_cont - 1)
                        print('Обязательно сохраните телефонную книгу, если удалили контакт (пункт 2)')
                        break
                else:
                    print('Контакта с таким ID нет')
            else:
                break
    else:
        print('Телефонная книга пуста или не загружена.')
        print('Загрузите телефонную книгу. Пункт 3.')


def find_contact():
    global phone_book
    qwery = view.input_find()
    id_cont = 1
    count = 0
    if len(phone_book) > 1:
        for contact in phone_book:
            c_lower = list(map(str.lower, contact))
            id_cont += 1
            for item in c_lower:
                if qwery in item:
                    count += 1
                    print(f'Найден подходящий контакт с id {id_cont}: ')
                    print(*contact)
        if count < 1:
            print('Контакт не найден')
    else:
        print('Телефонная книга пуста или не загружена.')
        print('Загрузите телефонную книгу. Пункт 3.')


def change_contact():
    global phone_book
    view.print_phone_book()
    if len(phone_book) < 1:
        print('!! Загрузите телефонную книгу (пункт 3)')
    else:
        id_cont = view.input_change_id()
        if id_cont > len(phone_book) + 1:
            print('Контакта с таким ID нет')
        else:
            print(f'Вы хотите изменить контакт {phone_book[id_cont - 1][0]} ')
            if view.input_confirm() == 'y':
                while True:
                    change_choice = view.change_contact_menu()

                    if change_choice == 1:
                        changed_contact_name = view.input_change_name()
                        print(f'Вы меняете имя контакта "{phone_book[id_cont - 1][0]}" \
на "{changed_contact_name}" ')
                        if view.input_confirm() == 'y':
                            phone_book[id_cont - 1][0] = changed_contact_name
                            print('Имя контакта изменено')

                    elif change_choice == 2:
                        changed_contact_phone = view.input_change_phone()
                        print(f'Вы меняете номер телефона {phone_book[id_cont - 1][1]} \
в контакте {phone_book[id_cont - 1][0]} на {changed_contact_phone} ')
                        if view.input_confirm() == 'y':
                            phone_book[id_cont - 1][1] = changed_contact_phone
                            print('Номер телефона контакта изменен')

                    elif change_choice == 3:
                        change_contact_comment = view.input_change_comment()
                        print(f'Вы меняете комментарий "{phone_book[id_cont - 1][2]}" \
в контакте "{phone_book[id_cont - 1][0]}" на "{change_contact_comment}" ')
                        if view.input_confirm() == 'y':
                            phone_book[id_cont - 1][2] = change_contact_comment
                            print('Комментарий контакта изменен')
                    else:
                        print('!!! Обязательно сохраните телефонную книгу, если вносили изменения (пункт 2)')
                        break


# def change_contact():
#     global phone_book
#     if len(phone_book) > 1:
#         view.print_phone_book()
#         id_cont = view.input_change_id()
#         if id_cont < len(phone_book) + 1:
#             print(f'Вы хотите изменить контакт {phone_book[id_cont - 1][0]}')
#             if view.input_confirm() == 'y':
#                 view.change_contact_menu()
#     else:
#         print('Телефонная книга пуста или не загружена.')
#         print('Загрузите телефонную книгу. Пункт 3.')
#
# #
# def change_contact():
#     global phone_book
#     if len(phone_book) < 1:
#         print('Телефонная книга пуста или не загружена.')
#         print('Загрузите телефонную книгу. Пункт 3.')
#     else:
#         view.print_phone_book()
#         id_cont = view.input_change_id()
#         if id_cont < len(phone_book) + 1:
#             print(f'Вы хотите изменить контакт "{phone_book[id_cont - 1][0]}"')
#             if view.input_confirm() == 'y':
#                 view.change_contact_menu()
#
#
# def choose_change(choice2):
#     match choice2:
#         case 1:
#             change_contact_name()
#         case 2:
#             change_contact_phone()
#         case 3:
#             change_contact_comment()
#         case 0:
#             return True
#
#
# def choose_choice():
#     while True:
#         choice2 = view.change_contact_menu()
#         if choose_change(choice2):
#             break
#
#
# def change_contact_name():
#     global phone_book
#     id_cont = view.input_change_id()
#     if len(phone_book) > 1:
#         changed_contact_name = view.input_change_name()
#         print(f'Вы меняете имя контакта "{phone_book[id_cont - 1][0]}" \
# на "{changed_contact_name}"?')
#         if view.input_confirm() == 'y':
#             phone_book[id_cont - 1][0] = changed_contact_name
#             print('Имя контакта изменено.')
#     else:
#         print('Телефонная книга пуста или не загружена.')
#         print('Загрузите телефонную книгу. Пункт 3.')
#
#
# def change_contact_phone():
#     global phone_book
#     id_cont = view.input_change_id()
#     if len(phone_book) > 1:
#         changed_contact_phone = view.input_change_phone()
#         confirm = input(f'Вы точно хотите изменить номер телефона \
# {phone_book[id_cont - 1][1]} в контакте {phone_book[id_cont - 1][0]} \
# на {changed_contact_phone}? (y/n) ')
#         if confirm.lower() == 'y':
#             phone_book[id_cont - 1][1] = changed_contact_phone
#     else:
#         print('Телефонная книга пуста или не загружена.')
#         print('Загрузите телефонную книгу. Пункт 3.')
#
#
# def change_contact_comment():
#     global phone_book
#     id_cont = view.input_change_id()
#     if len(phone_book) > 1:
#         changed_contact_comment = view.input_change_comment()
#         confirm = input(f'Вы точно хотите изменить комментарий \
# "{phone_book[id_cont - 1][2]}" в контакте{phone_book[id_cont - 1][0]} \
# на "{changed_contact_comment}"? (y/n) ')
#         if confirm.lower() == 'y':
#             phone_book[id_cont - 1][2] = changed_contact_comment
#     else:
#         print('Телефонная книга пуста или не загружена.')
#         print('Загрузите телефонную книгу. Пункт 3.')
