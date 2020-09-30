import pandas as pd


def merge(new, old=None):
    # very smart merging here, new and old merge
    if new is not None:
        if old is not None:
            x = pd.concat((new, old), sort=True)
            return x.groupby(x.index).first().sort_index()
        else:
            return new

    else:
        return old


# also works for frames, etc.
def last_index(ts, default=None):
    try:
        # if the object is empty
        return ts.last_valid_index() or default
    except AttributeError:
        return default


def first_index(ts, default=None):
    """
    Return the first valid index of a Series or DataFrame
    :param ts:
    :param default: Use if the series has no valid entries or if the argument is None
    :return:
    """
    try:
        return ts.first_valid_index() or default
    except AttributeError:
        return default


def to_datetime(ts=None):
    try:
        ts.index = pd.to_datetime(ts.index)
        return ts
    except AttributeError:
        return None


def to_date(ts=None, format=None):
    try:
        if format:
            ts.index = [t.strftime(format) for t in to_datetime(ts).index]
        else:
            ts.index = [t.date() for t in to_datetime(ts).index]
        return ts
    except AttributeError:
        return None
