""" Module that contains the step definitions for the
workspace verification
"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module
from sttable import parse_str_table
from pytest_bdd import then, parsers
from tests.step_defs.common_action_steps import send_request
from main.core.utils.logger import logging
from main.core.api.enums.http_methods_enum import HttpMethods
from main.movies.api.enums.project_constants import EndpointTags
from main.movies.utils.verify_response import VerifyResponse
# pylint: enable=no-name-in-module
# pylint: enable=import-error


@then(
    parsers.parse(
        "the response body should contain a list of {story_number}"
        + "stories associated with the project"
    )
)
def get_stories_list(request):
    """get stories list for the project

    Args:
        request (obj): the context object
    """
    logging.info(
        "validation request " +
        f"{isinstance(request.response.json(), list)}")
    assert isinstance(request.response.json(), list)
    for story in request.response.json():
        project_id_tag = EndpointTags.PROJECT_ID.value
        before_id = request.before_scenario[project_id_tag]
        logging.info(
            f"validate story project#{story.get('project_id')}")
        logging.info(
            "validate request " +
            f"project#{before_id}"
        )
        assert story.get("project_id") == before_id


@then(parsers.parse('the response status code should be "{statuscode}"'))
def validate_status_code(request, statuscode):
    """This function validates the status code
        recive the reques fixture
        recieve the statuscode
    """
    logging.info(
        "Validating the status code the response " +
        "status should be {statuscode} and " +
        f"is {request.response.status_code}")
    if request.response.status_code != 204:
        logging.info(f"response verification {request.response.json()}")
    assert request.response.status_code == int(statuscode)


@then(
    parsers.parse(
        "the response body should contain" +
        " the following data\n{body_parameters}"
    )
)
def body_params(request, body_parameters):
    """This function validates the response body
        recives the request fixture
        recives the body parameters which is a dict
    """
    logging.info("Validating the response body")
    body_parameters = parse_str_table(body_parameters)
    body_parameters = body_parameters.rows[0]
    logging.info(f"Validating the response body: {body_parameters}")
    for key, value in body_parameters.items():
        assert request.response.json().get(key) == value


@then(parsers.parse('the response should fit the following schema "{schema}"'))
def validate_schema(request, schema):
    """This function validates the response body
        recives a request fixture
        recives a schema to validate the response
    """
    logging.info(f"Validating the response against {schema} schema")
    schema_resp = request.response.json()
    veredict, emsg = VerifyResponse.verify_schema(
        response=schema_resp,
        schema=schema)
    logging.info(f"Veredict: {veredict} with message: {emsg}")
    assert veredict


@then(parsers.parse('the response body should have "{number}" elements'))
def validate_number_elements(request, number):
    """This function validates the response body

    Args:
        request (object): request fixture
        number (str): number of elements to validate
    """
    logging.info(f"Validating the response has {number} elements")
    assert len(request.response.json()) == int(number)


@then(
    parsers.parse(
        'the items from "{endpoint}" should have "{number}" elements')
)
def validating_number_from_endpoint(request, endpoint, number):
    """This function validates the number of elements
    from an endpoint

    Args:
        endpoint (str): Get endpoint to validate
        number (str): Number of elements to validate
    """
    response = send_request(request, HttpMethods.GET.value, endpoint)
    logging.info(f"Validating endpoint {endpoint} elements")
    logging.info(f"Validating the response has {number} elements")
    logging.info(f"real response has {len(response.json())} elements")
    logging.info(f"real response is {response.json()} elements")
    assert len(response.json()) == int(number)
