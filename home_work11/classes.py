from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self):
        for record in self.data.values():
            yield record


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str_(self):
        return self.value


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        date_format = '%d.%m.%Y'
# using try-except blocks for handling the exceptions
        try:
            date_birthday = datetime.strptime(value, date_format)
            self.__value = date_birthday
# If the date validation goes wrong
        except:
            print("Incorrect data format for birthday, should be DD.MM.YYYY")
            raise TypeError

    def __str__(self):
        return datetime.strftime(self.__value, '%d.%m.%Y')


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.isnumeric():
            self.__value = value
        else:
            print('Please for input phone use only number')
            raise TypeError


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = ''

    def __str__(self):

        if self.birthday:
            return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}, birthday: {str(self.birthday)}'
        else:
            return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}'

    #    if not self.birthday:
    #        return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}'
    #    else:
    #        return f'NameContact {self.name.value} - tel:  {"; ".join([phone.value for phone in self.phones])}, birthday: {str(self.birthday)}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def days_to_birthday(self):
        current_date = datetime.now()
        try:
            next_birthday = datetime(
                year=current_date.year, month=self.birthday.value.month, day=self.birthday.value.day)
        except:
            next_birthday = datetime(
                year=current_date.year, month=self.birthday.value.month, day=self.birthday.value.day-1)  # for date 29.02

        if next_birthday < current_date:
            try:
                next_birthday = datetime(
                    year=current_date.year+1, month=self.birthday.value.month, day=self.birthday.value.day)
            except:
                next_birthday = datetime(
                    year=current_date.year+1, month=self.birthday.value.month, day=self.birthday.value.day-1)

        return (next_birthday-current_date).days

    def delete_phone(self, del_phone):
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
#                edit_done=True
                return True
        print(f'Phone {old_phone} not found in data')
        return False
