import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generate list of unique ticket numbers to win the lottery

    :param int min: the minimum value starting from 1
    :param int max: the maximum value not more than 1000
    :param int quantity: the amount of unique numbers. Must be between min and max values
    """

    # we add '1' because max value is included in range
    max_quantity = max - min + 1

    if (min < 1) or (max > 1000) or (max_quantity < 1) or (quantity > max_quantity):
        return []

    unique_numbers = random.sample(
        range(
            min,
            max + 1,  # do + 1 to include max in range
        ),
        quantity,
    )

    unique_numbers.sort()

    return unique_numbers
