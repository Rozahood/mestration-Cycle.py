import datetime


def calculate_period_length(start_date, end_date):
    period_length = (end_date - start_date).days + 1
    return period_length


# def itermonthdates(start_date, end_date):
#     month_dates = (start_date, end_date) + 1
#     return month_dates


def string(name):
    string = (name)
    return string


def track_cycle():
    user_name = string(input("Enter user name: "))
    cycle_length = int(input("Enter the length of your menstrual cycle in days: "))
    last_period_date = input("Enter the start date of your last period (yyyy-mm-dd): ")
    year, month, day = map(int, last_period_date.split("-"))
    last_period_date = datetime.date(year, month, day)
    # itermonthdates()
    next_period_date = last_period_date + datetime.timedelta(days=cycle_length)
    today = datetime.date.today()

    while next_period_date <= today:
        print("Your next period is on {}.".format(next_period_date))
        last_period_date = next_period_date
        next_period_date = last_period_date + datetime.timedelta(days=cycle_length)

    print("You are not expecting your next period for at least {} days.".format((next_period_date - today).days))


if __name__ == '__main__':
    track_cycle()
