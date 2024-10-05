from datetime import datetime


def get_days_from_today(date_str: str) -> int:
    """
    Get difference in days between provided date and current date

    :param str date_str: date string in format "YYYY-MM-DD"
    """

    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    except:
        raise ValueError('The date argument should be in the format "YYYY-MM-DD"')

    current_date = datetime.today()

    delta = current_date - parsed_date

    return delta.days
