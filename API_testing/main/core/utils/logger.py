""" Logger module
"""
import logging
import os

LOGGER = "bootcampmt1.log"
absolute_path = os.path.dirname(__file__)
logger_path = os.path.join(absolute_path, "../../..", LOGGER)

logger_request = logging
logger_request.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    filename=logger_path,
)
