#!/usr/bin/python3
"""Define an abstract class"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Class"""
    @abstractmethod
    def sound(self):
        """Sound method"""
        pass


class Dog(Animal):
    """Dog class.

    Args:
        Animal (class): Abstract class.
    """

    def sound(self):
        """Sound Method for the dog

        Returns:
            str: Bark
        """
        return "Bark"


class Cat(Animal):
    """Cat class.

    Args:
        Animal (class): Abstract class.
    """

    def sound(self):
        """Sound Method for the cat.

        Returns:
            str: Meow
        """
        return "Meow"
