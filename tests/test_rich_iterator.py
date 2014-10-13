import unittest

from rich_iterator import RichIterator


class RichIteratorTestCase(unittest.TestCase):

    def test_drop(self):
        ri = RichIterator(range(5))
        ri.drop(2)
        self.assertListEqual(
            list(ri),
            [2, 3, 4]
        )

    def test_drop_stop_iteration(self):
        ri = RichIterator(range(5))
        ri.drop(7)
        self.assertListEqual(
            list(ri),
            []
        )

    def test_filter(self):
        ri = RichIterator(range(10))
        ri.filter(lambda x: x % 2)
        self.assertListEqual(
            list(ri),
            [1, 3, 5, 7, 9]
        )

    def test_list(self):
        ri = RichIterator(range(5))
        self.assertListEqual(
            ri.list(),
            [0, 1, 2, 3, 4]
        )

    def test_map(self):
        ri = RichIterator(range(3))
        ri.map(lambda x: x * 2)
        self.assertListEqual(
            list(ri),
            [0, 2, 4]
        )

    def test_next(self):
        ri = RichIterator(range(3))
        self.assertEqual(ri.next(), 0)
        self.assertEqual(ri.next(), 1)
        self.assertEqual(ri.next(), 2)
        self.assertRaises(StopIteration, lambda: ri.next())

    def test_per(self):
        ri = RichIterator(range(6))
        ri.per(2)
        self.assertListEqual(
            list(ri),
            [[0, 1], [2, 3], [4, 5]]
        )

    def test_per_with_remainder(self):
        ri = RichIterator(range(7))
        ri.per(2)
        self.assertListEqual(
            list(ri),
            [[0, 1], [2, 3], [4, 5], [6]]
        )

    def test_per_with_remainder_skipped(self):
        ri = RichIterator(range(7))
        ri.per(2, with_remainder=False)
        self.assertListEqual(
            list(ri),
            [[0, 1], [2, 3], [4, 5]]
        )

    def test_step(self):
        ri = RichIterator(range(7))
        ri.step(2)
        self.assertListEqual(
            list(ri),
            [0, 2, 4, 6]
        )

    def test_take(self):
        ri = RichIterator(range(5))
        self.assertListEqual(
            list(ri.take(3)),
            [0, 1, 2]
        )
        self.assertRaises(StopIteration, lambda: ri.take(3))

    def test_take_at_most(self):
        ri = RichIterator(range(5))
        self.assertListEqual(
            list(ri.take_at_most(3)),
            [0, 1, 2]
        )
        self.assertListEqual(
            list(ri.take_at_most(3)),
            [3, 4]
        )
