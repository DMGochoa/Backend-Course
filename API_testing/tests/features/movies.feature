@movies @api
Feature: Movies
    As an aplication developer, I want
    to work with the movies API, so that
    I can woek with movies data.

    @functional @tc_01 @smoke
    Scenario: Search all the movies when there are no records
        When the user sends a "GET" request to "/projects" endpoint
        Then the response status code should be "200"
        And the response body should have "0" elements
        And the response should fit the following schema "get_projects_schema.json"