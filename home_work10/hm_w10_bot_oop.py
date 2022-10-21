from collections import UserDict


class AddressBook(UserDict):
    # який додає Record у self.data.AddressBook
    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    def __init__(self, value):
        self.value = value

    def __str_(self):
        return f'{self.value}'


class Phone(Field):
    pass


class Name(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def edit_phone(self, old_phone, new_phone):
        for item in self.phones:
            if item.value == old_phone:
                item.value = new_phone

    def __str__(self):
        return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}'


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
    return 'Good bye!'
#    quit()


@input_error
def add_contact(user_data):
    """Create new contact"""
    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact = list_contact[1]

    if name_contact in CONTACTS:

        CONTACTS[name_contact].add_phone(phone_contact)
    else:
        new_record = Record(name_contact, phone_contact)
        CONTACTS.add_record(new_record)

    return (f'For {name_contact} add phone number: {phone_contact}')


@input_error
def change_contact(user_data):
    """Change old number phone  for name which is in Contacts to new phone"""

    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact_old = list_contact[1]
    phone_contact_new = list_contact[2]
    # print(name_contact)
    # print(name_contact.value)
    # print(CONTACTS.data)

    if name_contact in CONTACTS.data:

        CONTACTS.data[name_contact].edit_phone(
            phone_contact_old, phone_contact_new)
    else:
        return f'Contact {name_contact} not in phone book'

    return f'For {name_contact} has changed phone number at: {phone_contact_new}'


@input_error
def phone_for_name(user_data):

    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact = CONTACTS[name_contact]

    return f'For {name_contact} phone number is {phone_contact}'


@input_error
def show_all_func():
    all_contact = ''

    for key in CONTACTS:
        all_contact += f'\n{CONTACTS[key]}'

    return all_contact if all_contact else "No contacts in book"


def main():

    commands_dict = {
        'hello': hello_func,
        'show all': show_all_func,
        'exit': quit_func,
        'good bye': quit_func,
        'close': quit_func
    }
    commands_args_dict = {
        'add': add_contact,
        'change': change_contact,
        'phone': phone_for_name,
    }
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
