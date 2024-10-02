#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    This function takes a CSV file and converts it into JSON format.

    Args:
        csv_file (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful,
        False if an error occurred.
    """
    try:
        with open(csv_file, 'r') as csvFile:
            csv_data = csv.DictReader(csvFile)

            data = list(csv_data)

        with open('data.json', 'w', encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile, indent=4)
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return False
