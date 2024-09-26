#!/usr/bin/python3
"""Define a class named CountedIterator."""


class CountedIterator:
    """CountedIterator"""

    def __init__(self, iterator):
        """Constructor.

        Args:
            iterator (iterable): Iterates the list to update the counter.
            counter (int): The counter tracks the number of items iterated.
        """
        self.iterator = iter(iterator)
        self.counter = 0

    def get_count(self):
        """Returns the current value of the counter"""
        return self.counter

    def __iter__(self):
        """Returns:
            The iterator
        """
        return self

    def __next__(self):
        """Modified the __next__ method to get the next item
            from the iterator and increments the counter.

        Raises:
            StopIteration: if there is no more items

        Returns:
            The next item from the list.
        """
        self.counter += 1
        try:
            return next(self.iterator)
        except StopIteration:
            raise StopIteration

# Testing


data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
