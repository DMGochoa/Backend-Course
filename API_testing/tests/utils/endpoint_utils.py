"""Module to handle endpoint utils."""
# pylint: disable=import-error
# pylint: disable=no-member
# pylint: disable=no-self-argument
# pylint: disable=too-few-public-methods
# pylint: disable=self-cls-assignment
import re
from main.core.utils.logger import logging


class EndpointUtils:
    """Class to handle endpoint utils."""

    def endpoint_autofill_tags(endpoint, request_dict):
        """This function autofills the tags in the endpoint

        Args:
            endpoint (str): Endpoint to autofill.
            request_dict (dict): Dictionary with the tags to fill.

        Returns:
            str: Endpoint with the tags filled.
        """
        match_tags = re.findall(r"<[\w\.]*>", endpoint)
        logging.info(f"Match tags: {match_tags}, endpoint: {endpoint}")
        if match_tags:
            for tag in match_tags:
                logging.info(f"tag: {tag}")
                endpoint = endpoint.replace(tag,
                                            str(request_dict[tag]))
                logging.info(f"endpoint: {endpoint}")
        logging.info(f"Endpoint result: {endpoint}")
        return endpoint