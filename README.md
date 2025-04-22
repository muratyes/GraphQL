# Python-Flask Application Using Two Different APIs (REST APIs and GRAPHQL)

This project contains two separate Flask applications that pull data from two different APIs and display this data on a web page.

## APPLICATION I: GraphQL Application Displaying Rick and Morty Characters
Description: The application displays a list of Rick and Morty characters on the home page ( `/` ). Each character's name, type, and image are displayed.

This application pulls character information using the "GraphQL" endpoint on the [Rick and Morty API](https://rickandmortyapi.com/) and displays it on a web page.

### Requirements (Rick and Morty)
* Python 3.x
* Flask
* requests
* gql

## IMPLEMENTATION II: REST API Application Displaying Fake Store Products

This application retrieves product information using the "REST API" on [Fake Store API](https://fakestoreapi.com/) and displays it on a web page.

### Features (Fake Store)

* Retrieves product data from the Fake Store API.
* Displays the retrieved product information in the web browser using an HTML template.
* Developed with the Flask framework.
* Uses the `requests` library for HTTP requests.

### Requirements (Fake Store)
* Python 3.x
* Flask
* requests

## Dependencies

* **Flask:** A Python framework used to develop web applications.
* **requests:** A Python library used to make HTTP requests.
* **gql:** A Python library for creating and running GraphQL queries (for the Rick and Morty app only).
