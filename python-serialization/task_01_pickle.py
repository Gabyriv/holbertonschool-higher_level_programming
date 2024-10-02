#!/usr/bin/python3
"""Define a class CustomObject."""
import pickle


class CustomObject:
    """Custom Python class."""

    def __init__(self, name, age, is_student):
        """
        Constructor for CustomObject.

        Args:
            name (str): The name of the person being represented.
            age (int): The age of the person being represented.
            is_student (bool): Whether or not the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object in a human-readable format.

        This method can be used to inspect the contents of the object in a
        user-friendly way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file.

        This method will serialize the object instance to the given
        filename. It will return None if an error occurs, otherwise
        it will return the serialized object.

        Args:
            filename (str): The name of the file to serialize the object
                            to.

        Returns:
            object or None: The serialized object if successful, otherwise
                            None.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize the object from a file.

        This method will deserialize an object from the given filename.

        Args:
            filename (str): The name of the file to deserialize the object
                            from.

        Returns:
            object or None: The deserialized object if successful, otherwise
                            None.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return None
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
