from rich_iterator.rich_iterator import return_rich_iterator


@return_rich_iterator
def integers(start=0):
    current = start
    while True:
        yield current
        current += 1


@return_rich_iterator
def constant(value, times=None):
    if times is None:
        while True:
            yield value
    else:
        for _ in range(times):
            yield value
