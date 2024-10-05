import re


def normalize_phone(phone_number: str) -> str:
    """
    Clean all chars except numbers from the phone and add Ukrainian code prefix (if needed).
    For example: "(095) 234-5678\\n" will become "+380952345678"

    :param str phone_number: the valid phone number string
    """

    clean_number = re.sub(r"(\+?38)|\D", "", phone_number)

    valid_number = "+38" + clean_number

    return valid_number
