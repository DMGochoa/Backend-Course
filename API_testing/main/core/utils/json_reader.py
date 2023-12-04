""" Json reader module
"""
import json


class JsonReader:
    """Json reader class"""

    def __init__(self, path):
        """In this implementation, the json_handler class takes a path
        parameter as an argument during initialization. This is the path
        where the json file is.

        Args:
            path (str): Is the path where the json file is
        """
        self.path = path
        self.json = None

    def open_json(self):
        """This function opens the json file and returns the content

        Returns:
            object: The content of the json file
        """
        with open(self.path, "r", encoding="utf-8") as json_file:
            self.json = json.load(json_file)
        return self.json

    def save_json(self, data):
        """This function saves the data in the json file

        Args:
            data (object): The data to save in the json file
        """
        with open(self.path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
