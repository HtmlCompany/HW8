from datetime import date, timedelta
from collections import defaultdict


def get_date_change(start_day:date, days:int):
    result = {}
    for _ in range(days + 1):
        result[start_day.day, start_day.month] = start_day.year
        start_day += timedelta(1)
    return result

def get_birthdays_per_week(users:list)->dict:
    result_dict = defaultdict(list)
    start_day = date.today()
    period = get_date_change(start_day, 7)
    
    if not users:
        return {}

    for user in users:
        birth_day :date = user["birthday"]
        date_bd = birth_day.day, birth_day.month
        if date_bd in list(period):
            br_dat = birth_day.replace(year=period[date_bd])
            print(user["name"], br_dat, br_dat.weekday(), sep='->')
            bd_weekday = br_dat.weekday()
            if bd_weekday in (5, 6):
                result_dict["Monday"].append(user["name"])
            else:
                result_dict[br_dat.strftime("%A")].append(user["name"])
    return dict(result_dict)
                    
            # print(period[date_bd])

if __name__ == "__main__":

    test_dict = [
        {"name": "Bill Gates", "birthday": date(1955, 10, 4)},
        {"name": "Ramiz Yunus", "birthday": date(1959, 10, 3)},
        {"name": "Vovka Boltorez", "birthday": date(1990, 9, 29)},
        {"name": "Bill Gates", "birthday": date(1988, 10, 5)},
        {"name": "Zheka Vintorez", "birthday": date(1985, 9, 30)},
        {"name": "Oleh Zhdanov", "birthday": date(1975, 10, 2)},
        {"name": "Kolyan Svitan", "birthday": date(1995, 10, 1)}
    ]

    print(get_birthdays_per_week(test_dict))
    #print(get_date_change(date(2023, 12, 30), 7))