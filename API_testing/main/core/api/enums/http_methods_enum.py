""" Enum Module for HttpResponse
"""
from enum import Enum


class HttpMethods(Enum):
    """
    list of endpoints that pivotal uses
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
