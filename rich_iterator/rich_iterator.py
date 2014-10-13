import functools

import rich_iterator.functions as _f


def return_rich_iterator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return RichIterator(func(*args, **kwargs))

    return wrapper


def _extractor(func, iterator_position=0):

    @functools.wraps(func)
    def wrapper(rich_iterator, *args, **kwargs):
        args = list(args)
        args.insert(iterator_position, rich_iterator.iterator)
        return func(*args, **kwargs)

    return wrapper


def _modifier(func, iterator_position=0):

    @functools.wraps(func)
    def wrapper(rich_iterator, *args, **kwargs):
        args = list(args)
        args.insert(iterator_position, rich_iterator.iterator)
        rich_iterator.iterator = func(*args, **kwargs)
        return rich_iterator

    return wrapper


class RichIterator:
    """
    Wraps an iterator and adds several convenience methods

    Some of these methods, modifiers, are designed for chaining (they return
    self), while others, extractors, return values from the wrapped iterator
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    # modifiers
    cycle = _modifier(_f.cycle)
    drop = _modifier(_f.drop)
    filter = _modifier(filter, iterator_position=1)
    map = _modifier(map, iterator_position=1)
    per = _modifier(_f.per)
    step = _modifier(_f.step)

    # extractors
    list = _extractor(list)
    next = _extractor(next)
    take = _extractor(_f.take)
    take_at_most = _extractor(_f.take_at_most)
