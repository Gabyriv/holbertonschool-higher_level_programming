#!/usr/bin/python3
"""Define a class named VerboseList that inherits from list
a built-in python class."""


from typing import Any, Iterable, SupportsIndex


class VerboseList(list):
    """Inherits from a built-in class.

    Args:
        list (class): Built-in python class.
    """

    def append(self, object: Any) -> None:
        """Modified the append method to
            print a message when an item is appended.

        Args:
            object (Any): Any object added to the list.

        Returns:
            str: message when an item is added.
        """
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable: Iterable) -> None:
        """Modified the extend method to
            print  message when the list is extended.

        Args:
            iterable (int): The number of items added.

        Returns:
            str: message when the list is extended.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value: Any) -> None:
        """Modified the remove method to print a
            message before removing an item from the list.

        Args:
            value (Any): The value removed from the list.
        """
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index: int = -1) -> Any:
        """Modified the pop method to print a
            message before popping an item from the list.

        Args:
            index (int, optional): The index in the list. Defaults to -1.

        Raises:
            IndexError: When the list is empty.

        Returns:
            Any: the popped item.
        """
        if len(self) == 0:
            raise IndexError("pop from empty list")
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
