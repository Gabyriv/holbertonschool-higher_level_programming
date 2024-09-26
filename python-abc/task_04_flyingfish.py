#!/usr/bin/python3
"""Construct 3 class(Fish, Bird, FlyingFish)"""


class Fish():
    """Fish class"""

    def swim(self):
        """Tells if the fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Tells where the fish lives"""
        print("The fish lives in water")


class Bird():
    """Bird class."""

    def fly(self):
        """Tells if the bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """Tells where the bird lives"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from the bird class and
    the fish class.

    Args:
        Fish (class): the fish class
        Bird (class): the bird class
    """

    def fly(self):
        """Override the fly method to print
            what the flying fish is doing.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swim method to print
        what the flying fish is doing.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method to print
            where the flying fish lives.
        """
        print("The flying fish lives both in water and the sky!")


ff = FlyingFish()

ff.fly()
ff.swim()
ff.habitat()
print(FlyingFish.mro())
