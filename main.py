from datetime import datetime, date, timedelta

def get_birthdays_day_week(users):
    result = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    today = date.today()
    yesterday = today - timedelta(days=1)
    before_yesterday = today - timedelta(days=2)
    week = timedelta(days=7)

    if not users:
        return {}
    else:
        for person in users:
            person["birthday"] = person["birthday"].replace(year=today.year)
            birthday = person["birthday"].strftime('%A')
            first_name = person["name"].split()[0]
            if today.strftime('%A') == "Monday":
                if person['birthday'] == yesterday\
                        or person["birthday"] == before_yesterday:
                    result["Monday"].append(first_name)
                    continue
            if today <= person["birthday"] <= today + week:
                if birthday == "Saturday" or birthday == "Sunday":
                    result["Monday"].append(first_name)
                else:
                    result[birthday].append(first_name)
            else:
                if (today + week).year == today.year + 1:
                    person["birthday"] = person["birthday"]\
                        .replace(year=today.year + 1)
                    new_year_birthday = person["birthday"].strftime('%A')
                    if today <= person["birthday"] <= today + week:
                        if new_year_birthday == "Saturday"\
                                or new_year_birthday == "Sunday":
                            result["Monday"].append(first_name)
                        else:
                            result[new_year_birthday].append(first_name)
                continue
    clear_result = {key: value for key, value in result.items() if value}
    return clear_result


if __name__ == "__main__":
    users = [
        {"name": "Mike O'Hearn", "birthday": datetime(1999, 4, 10).date()},
        {"name": "Kun Lao", "birthday": datetime(1977, 1, 5).date()},
        {"name": "Master Chief", "birthday": datetime(1988, 7, 7).date()},
        {"name": "BOSS", "birthday": datetime(1998, 12, 12).date()},
        {"name": "Tony Stark", "birthday": datetime(1978, 8, 9).date()},
        {"name": "Oleg Mongol", "birthday": datetime(1991, 5, 14).date()},
        {"name": "Elvies Presley", "birthday": datetime(1971, 11, 11).date()},
        {"name": "Albert Einstein", "birthday": datetime(1996, 5, 6).date()},
        {"name": "Harry Potter", "birthday": datetime(1972, 1, 2).date()},
        {"name": "Stanislav Synyavskyy", "birthday": datetime(1989, 7, 8).date()},
    ]

    result = get_birthdays_day_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
