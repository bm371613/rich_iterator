rich_iterator
=============

The `rich_iterator` module key feature is the `RichIterator` class, which
wraps an iterator and adds several convenience methods.

The motivation for `RichIterator` is readability. This little library is
targeted for people who think that `x.filter(f).map(g)` looks better than
`x = map(g, filter(f, x))`.
   
Examples:

    >>> from rich_iterator import RichIterator
    >>> ri = RichIterator([2, 7, 4, 1, 9, 3, 8, 5, 2, 8])
    >>> ri.filter(lambda x: x % 2).map(lambda x: x * 10).next(3)
    [70, 10, 90]

    >>> from rich_iterator import integers
    >>> integers().per(5).skip(10).step(2).next(2)
    [[50, 51, 52, 53, 54], [60, 61, 62, 63, 64]]

