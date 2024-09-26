#!/usr/bin/python3
"""Define a class named CountedIterator."""


class CountedIterator:
    """
    An iterator class that keeps track of how many items have been iterated.

    Attributes:
        iterator (iter): The original iterator object.
        counter (int): Tracks the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable (iterable): An iterable object that
                                    will be converted to an iterator.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the current value of the counter.

        Returns:
            int: Number of items iterated over.
        """
        return self.counter

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The current instance.
        """
        return self

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Raises:
            StopIteration: If there are no more items in the iterator.

        Returns:
            The next item from the iterator.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise


# Testing
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total"
                  f"{counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
