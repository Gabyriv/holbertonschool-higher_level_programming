#!/usr/bin/python3
"""Define 3 classes(SwimMixin, FlyMixin, Dragon)"""


class SwimMixin():
    """SwimMixin class."""

    def swim(self):
        """Swimming method"""
        print("The creature swims!")


class FlyMixin():
    """FlyMixin class."""

    def fly(self):
        """Flying Method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class.

    Args:
        SwimMixin (class): To inherit from.
        FlyMixin (class): To inherit from.
    """

    def swim(self):
        """No change

        Returns:
            str: The creature swim.
        """
        return super().swim()

    def fly(self):
        """No change

        Returns:
            str: The creature flies.
        """
        return super().fly()

    def roar(self):
        """The dragon roars.
        """
        print("The dragon roars!")


dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!
