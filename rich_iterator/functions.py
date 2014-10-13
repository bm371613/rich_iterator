def next_(iterable, n=None):
    """
    Return next element (or list of elements) of an iterable
    Raise `StopIteration` if there are not enough elements
    """
    iterator = iter(iterable)
    if n is None:
        return next(iterator)
    else:
        return [next(iterator) for _ in range(n)]


def next_at_most(iterable, n):
    """
    Return a list of at most `n` elements of an iterable, or all the elements
    of the iterable if there are less than `n`
    """
    iterator = iter(iterable)
    result = []
    try:
        for _ in range(n):
            result.append(next(iterator))
    except StopIteration:
        pass
    return result


def per(iterable, n, with_remainder=True):
    """
    Yield lists of size `n` from iterable.
    If `with_remainder` is `True` and number of elements in iterable is not
    divisible by `n`, yield list of remaining elements in the end.
    """
    iterator = iter(iterable)
    while True:
        if with_remainder:
            batch = next_at_most(iterator, n)
        else:
            batch = next_(iterator, n)
        if batch:
            yield batch
        else:
            break


def step(iterable, step_):
    """
    Yield only every `n`-th element from `iterable`, begining with the first
    """
    for index, element in enumerate(iterable):
        if index % step_ == 0:
            yield element


def skip(iterable, n=1):
    """
    Skip `n` values from `iterable`
    """
    iterator = iter(iterable)
    try:
        for _ in range(n):
            next(iterator)
    except StopIteration:
        pass
    return iterator
