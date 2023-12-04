"""
This module contains the step definitions for the projects feature.
"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
import os
from pytest_bdd import scenarios
from main.core.utils.logger import logging # noqa: F403,F401,E501
from tests.step_defs.common_action_steps import *  # noqa: F403,F401,E501
from tests.step_defs.common_verification_steps import *  # noqa: F403,F401,E501

# pylint: enable=wildcard-import
# pylint: enable=import-error
# pylint: enable=no-name-in-module
# pylint: enable=unused-wildcard-import
logging.info("Executing the projects feature")
feature_path = os.path.join(os.path.dirname(__file__), "..", "features")


scenarios(feature_path)