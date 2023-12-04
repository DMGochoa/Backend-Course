""" request manager module
"""
import os
import requests

# pylint: disable=import-error
# pylint: disable=no-name-in-module
from main.core.utils.json_reader import JsonReader
from main.core.utils.logger import logging
from main.core.api.enums.http_methods_enum import HttpMethods

# pylint enable=import-error
# pylint enable=no-name-in-module
# pylint: disable=unused-private-member


class RequestManager:
    """Request Manager Class implementation"""

    __instance = None

    def __init__(self, config_file=""):
        """Constructor For Request Manager

        Args:
            config_file (str, optional): json file with
                        needed configuration. Defaults to ./configuration.json.
        """
        # Obtain the root path of the project
        root_path = os.path.join(os.path.dirname(__file__), "..", "..", "..")
        if config_file == "":
            self.__config = JsonReader(
                os.path.join(root_path, "configuration.json")
            ).open_json()
        else:
            self.__config = JsonReader(config_file).open_json()
        # Get the environment selected
        env_selected = self.__config.get("environment", "development")
        # Get the environment configuration by the environment selected
        __environment = (
            JsonReader(os.path.join(root_path, "environment.json"))
            .open_json()
            .get(env_selected)
        )
        # Set the environment configuration
        self.url = __environment.get("url")
        self.headers = __environment.get("headers")
        self.params = None
        self.response = {}

    @staticmethod
    def get_instance():
        """Singleton implementation to return instance

        Returns: instance -> RequestManager
        """
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestManager()
        return RequestManager.__instance

    def make_request(
        self, http_method, endpoint, payload=None
    ):  # pylint: disable=W0613
        """central method to make a request

        Args:
            http_method (str): HTTP method
            endpoint (str): Endpoint to make request
            payload (dict, optional): body of the request. Defaults to None.
        Returns:
            request response object
        """
        logging.debug(
            f"Request {http_method} to {self.url}{endpoint}"
        )  # pylint: enable=W0613
        self.response = requests.request(
            method=HttpMethods[http_method].value,
            url=f"{self.url}{endpoint}",
            headers=self.headers,
            params=payload,
            timeout=(15),
        )
        return self.response
