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

    def serialize(self, filename: str):
        """
        Serialize the CustomObject instance to a file using pickle

        Args:
            filename (str): The name of the file to serialize the object to
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as error:
            print(error)

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize a CustomObject instance from a file using pickle

        Args:
            filename (str): The name of the file to deserialize the object from

        Returns:
            CustomObject: The deserialized CustomObject instance
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except (OSError, pickle.PickleError) as error:
            print(error)
            return None
