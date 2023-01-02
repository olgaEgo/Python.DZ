import data_base as db
import view
import phone_book as pb


def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            db.save_contacts()
        case 3:
            db.load_contacts()
        case 4:
            pb.add_contact()
        case 5:
            pb.change_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.find_contact()
        case 0:
            return True


while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break

#
# def change_contact_menu(choice2):
#     match choice2:
#         case 1:
#             pb.change_contact_name()
#         case 2:
#             pb.change_contact_phone()
#         case 3:
#             pb.change_contact_comment()
#         case 0:
#             return True
#
#
# while True:
#     choice2 = view.change_contact_menu()
#     if choice_menu(choice2):
#         break
#
# Stone;1111111111;GeekBrains
# Diana;2222222222;GeekBrains
# Olga;3333333333;I am
# Kate;4444444444;sister
# 55555;555;555
