from collections import UserDict
from datetime import datetime

from classes import AddressBook, Birthday,  Field, Phone, Record


CONTACTS = AddressBook()

# decorator


def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Wrong name"
        except TypeError:
            return "Wrong command"
        except IndexError:
            return "Enter name and phone"
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args

    return inner


@input_error
def hello_func():
    return 'How can I help you?'


@input_error
def quit_func():
    CONTACTS.write_adress_book_file()
    return 'Good bye!'


@input_error
def add_contact(user_data):
    """Create new contact"""
    list_contact = user_data.strip().split()
    len_listcontact = len(list_contact)
    if len_listcontact >= 3:
        name_contact = list_contact[0]
        phone_contact = list_contact[1]
        birthday = list_contact[2]
    else:
        name_contact = list_contact[0]
        phone_contact = list_contact[1]
        birthday = None

    if name_contact in CONTACTS:

        CONTACTS[name_contact].add_phone(phone_contact)
    else:
        new_record = Record(name_contact, phone_contact, birthday)
        CONTACTS.add_record(new_record)

    return (f'For {name_contact} add phone number: {phone_contact} and birthday {birthday}')


@input_error
def change_contact(user_data):
    """Change old number phone  for name which is in Contacts to new phone"""

    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact_old = list_contact[1]
    phone_contact_new = list_contact[2]
    old_data_contact = CONTACTS.data[name_contact]

#    if name_contact in CONTACTS.data: (спрацьовує декоратор і видає Wrong Name, якщо немає серед контактів на попередньому операторі)

    if old_data_contact.edit_phone(phone_contact_old, phone_contact_new):
        return f'For {name_contact} has changed phone number at: {phone_contact_new}'

    return f' {name_contact} has not phone number {phone_contact_old} in contact'

#    return f'Contact {name_contact} not in phone book'


@input_error
def find_contact(user_data):

    search_data = user_data.strip().split()[0]

    print(f'Result of search on key "{search_data}":\n')

    for name, data in CONTACTS.items():

        for phone in data.phones:

            if search_data in name or search_data in phone.value:
                print(f'\n{CONTACTS[name]}')


@input_error
def how_many_days_to_birthday(user_data):

    name_contact = user_data.strip().split()[0]
    if name_contact not in CONTACTS:
        return f'No record with this name {name_contact}'

    data_contact = CONTACTS.data[name_contact]

    return f' {data_contact.days_to_birthday()} days to birthday of {name_contact}'


@input_error
def phone_for_name(user_data):

    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact = CONTACTS[name_contact]

    return f'For {name_contact} phone number is {phone_contact}'


@input_error
def show_all_func(user_data):

    quantity_records_on_page = int(user_data.strip().split()[0])
    stock = CONTACTS.iterator()
    page = 1

    while True:
        try:
            for _ in range(quantity_records_on_page):
                print(next(stock))
            print(f"Page:   {page}")
            page += 1
        except StopIteration:
            print("it's end.No contacts in book")
            break

 #   all_contact = ''

 #   for key in CONTACTS:
 #       all_contact += f'\n{CONTACTS[key]}'

 #   return all_contact if all_contact else "No contacts in book"


def main():

    commands_dict = {
        'hello': hello_func,
        'exit': quit_func,
        'good bye': quit_func,
        'close': quit_func
    }
    commands_args_dict = {
        'show_all': show_all_func,
        'add': add_contact,
        'change': change_contact,
        'phone': phone_for_name,
        'birthday': how_many_days_to_birthday,
        'find': find_contact
    }
    records_from_file = CONTACTS.read_adress_book_from_file()
    if records_from_file:
        for key, value in records_from_file.items():
            CONTACTS.data[key] = value

    print("Hello! I am a bot. My Command list: ")
    for command in commands_dict:
        print(command)
    print("Input 'command name number' for next command")
    for command in commands_args_dict:
        print(command)

    while True:
        user_command = input('Input command: ').strip().lower()
        user_data = ''
        command = user_command.split()[0]

        if user_command in commands_dict:

            action = commands_dict[user_command]()

        elif command in commands_args_dict:

            user_data = user_command[len(command):]
            action = commands_args_dict[command](user_data)
        else:
            print("Wrong command ", {user_command}, " Try again")
            continue
        print(action)
        if action == "Good bye!":
            quit()


if __name__ == "__main__":
    main()
