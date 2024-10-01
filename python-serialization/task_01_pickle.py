#!/usr/bin/python3
"""Define a class CustomObject"""
import pickle


class CustomObject:
    """Define a class CustomObject"""

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize CustomObject instance

        Args:
            name (str): The name of the custom object
            age (int): The age of the custom object
            is_student (bool): Whether the custom object is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the properties of the CustomObject instance

        The display method prints out the name, age and whether the
        custom object is a student or not.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the CustomObject instance to a file using pickle

        Args:
            filename (str): The name of the file to serialize the object to
        """

        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file using pickle

        Args:
            filename (str): The name of the file to deserialize the object from

        Returns:
            CustomObject: The deserialized CustomObject instance
        """

        with open(filename, 'rb') as cls.file:
            return pickle.load(cls.file)
