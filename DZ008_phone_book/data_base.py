import phone_book as pb

path = r'phone_book.txt'


def load_contacts():
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    pb.set_phone_book(str_to_list(data))
    print('Телефонная книга загружена')


def save_contacts():
    global path
    ready_book = list_to_str(pb.get_phone_book())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)
    print('Телефонная книга сохранена')


def list_to_str(phonebook: list) -> str:
    str_phone_book = ''
    for contact in phonebook:
        new_contact = ';'.join(contact)
        str_phone_book += new_contact + '\n'
    return str_phone_book[:-1]


def str_to_list(phonebook: list) -> list:
    new_list = []
    for contact in phonebook:
        new_contact = contact.strip().split(';')
        new_list.append(new_contact)
    return new_list


def save_changed_contact():
    global path
    ready_book = pb.change_contact()
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)
    print('Изменения в контакте сохранены\n')