CONTACTS = {}

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

    if name_contact in CONTACTS:
        raise ValueError("The name is in Contacts. Need other name")

    phone_contact = list_contact[1]
    CONTACTS[name_contact] = phone_contact

    return (f'For {name_contact} add phone number: {phone_contact}')


@input_error
def change_contact(user_data):
    """Change number phone for name which is in Contacts"""

    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact = list_contact[1]
    CONTACTS[name_contact] = phone_contact

    return f'For {name_contact} has changed phone number at: {phone_contact}'


@input_error
def phone_for_name(user_data):

    list_contact = user_data.strip().split()
    name_contact = list_contact[0]
    phone_contact = CONTACTS[name_contact]

    return f'For {name_contact} phone number is {phone_contact}'


@input_error
def show_all_func():
    return(CONTACTS)


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
