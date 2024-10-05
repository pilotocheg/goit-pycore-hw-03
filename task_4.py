from datetime import date, datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Generate list of upcoming birthdays with users names and congratulation dates.
    If congratulation date is weekend it's automatically shifted on next working Monday

    :param list[user] users: list of users in format `{ "name": str, "birthday": str }`
    """

    today_date = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birth_date = datetime.strptime(user["birthday"], DATE_FORMAT).date()
        congratulation_date = birth_date.replace(year=today_date.year)

        if congratulation_date < today_date:
            # if the user already had birthday this year we set congratulation_date on the next year
            congratulation_date = birth_date.replace(year=today_date.year + 1)

        days_before_birthday = (congratulation_date - today_date).days

        if days_before_birthday < 7:
            week_days_left = 7 - congratulation_date.weekday()

            if week_days_left <= 2:
                # if congratulations date is weekend - shift it on monday
                congratulation_date += timedelta(days=week_days_left)

            congratulation_date_str = date.strftime(congratulation_date, DATE_FORMAT)

            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": congratulation_date_str}
            )

    return upcoming_birthdays
