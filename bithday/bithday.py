from datetime import datetime, timedelta, date
import calendar

users = [
    {'name': 'Ivan', 'birthday': datetime(1978, 9, 27, 0, 0)},
    {'name': 'dik', 'birthday': datetime(1958, 10, 4, 0, 0)},
    {'name': 'Nik', 'birthday': datetime(1968, 10, 1, 0, 0)},
    {'name': 'Nata', 'birthday': datetime(1998, 9, 29, 0, 0)},
    {'name': 'ket', 'birthday': datetime(1938, 10, 2, 0, 0)},
    {'name': 'rt', 'birthday': datetime(1970, 9, 27, 0, 0)}]


def make_list_day_of_week():
    curn_date = date.today()
    weekday_today = curn_date.weekday()
    list_date_week = []

    if weekday_today != 0:
        for i in range(7):
            list_date_week.append(curn_date)
            curn_date += timedelta(days=1)
    else:
        curn_date = curn_date - timedelta(days=2)  # two_day_passed_date

        for i in range(7):
            list_date_week.append(curn_date)
            curn_date += timedelta(days=2)

    return (list_date_week)


bithday_list = {0: [], 1: [], 2: [], 3: [], 4: []}


def check_date_users_bithday(user, day_of_list):

    # check data user == data day

    day_birth_dt = user['birthday'].day  # number bithday
    month_birth_m = user['birthday'].month  # month bithday
    # day_of_list - date object from days next week for check
    return ((day_birth_dt == day_of_list.day) and (month_birth_m == day_of_list.month))


def check_data(users):

    list_date_week = make_list_day_of_week()

    for day in list_date_week:
        number_day_of_week = day.weekday()  # 0-monday...
        if number_day_of_week in (5, 6):
            number_day_of_week = 0

        for item in users:
            if check_date_users_bithday(item, day):
                bithday_list[number_day_of_week].append(item['name'])


def get_birthdays_per_week(users):

    check_data(users)

    for key in bithday_list:
        name_day = calendar.day_name[key]

        list_person_bithday = bithday_list[key]
        string_list_person = ', '.join(list_person_bithday)
        print(name_day, ': ', string_list_person)


def main():
    get_birthdays_per_week(users)


if __name__ == '__main__':
    main()
