def fixed_quantity_sizer(strategy, action, quantity=10):
    return quantity * action.value


def dollar_amount_sizer(strategy, action, amount=1000):
    """
    Return the quantity amount for the strategy that is valued closest
    to the amount value requested.

    :param strategy:
    :param action:
    :param amount:
    :return: quantity amount
    """

    return 1
