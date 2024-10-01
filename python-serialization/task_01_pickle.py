#!/usr/bin/python3
"""Pickle Module"""
import pickle


class CustomObject:
    """A custom Python class to demonstrate object serialization/deserialization
    using the pickle module
    """

    def __init__(self, name, age, is_student):
        """Initialize a new instance of CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object and save it to the
        provided filename
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except FileNotFoundError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of the CustomObject from the provided
        filename
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
