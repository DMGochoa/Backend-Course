"""This module contains the functions to verify the response"""
import os
import jsonschema
from main.core.utils.logger import logging
from main.core.utils.json_reader import JsonReader


class VerifyResponse:
    """This class contains the functions to verify the response"""

    def verify_schema(response, schema):
        """This function verifies the response against a schema

        Args:
            response (object): response object of a request
            schema (str): schema path to validate the response

        Returns:
            bool: True if the response is valid, False otherwise
            str: Success if the response is valid, error message otherwise
        """
        logging.info(f"Validating the response against {schema} schema")
        resources_path = os.path.join(
            os.path.dirname(__file__), "..", "api", "resources", schema
        )
        template_schema = JsonReader(resources_path).open_json()
        try:
            jsonschema.validate(response, template_schema)
            return True, "Success"
        except jsonschema.exceptions.ValidationError as error:
            return False, str(error)
