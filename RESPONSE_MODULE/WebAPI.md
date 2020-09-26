# WebAPI
What's an API? An API (Application Programming Interface), is a set of procedure that make possible the information exchange between two software components.  

API -> Interface -> Under-the-hood software logic 

A WebAPI could be seen as a set of protocols the let comunication between multiple WebApps, an efficient comunication between parts/section of the same WebApp or comunication between an external client (e.g. mobile app) to a WebApp. 

The most common WebAPI (synonym of _web service_) is REST. Standard format for the comunication is JSON (JavaScript Object Notation).

How we can access to those WebAPIs? With the **endpoints**, typically a URL pattern.

## REST API
REST (Representational State Transfer) is an architectural approach HTML-based for the creation of a WebAPI that follows the characteristics below:

- Resources accessible through an HTML endpoint;
- JSON or XML format for the comunication;
- Stateless, like HTML;
- Usage of the main HTML methods (GET, POST, UPDATE, DELETE).

### Request
A request is made of the following parts:

- Request type
- Header
- Blank line
- Body (optional)

Example of a request type:

* GET www.google.com HTTP/1.1

### Response
A response is made of the following parts:

- Request state (success or failure)
- Header
- Blank line
- Body (optional)

Example of a request state:

* HTTP/1.1 200 OK 

### HTTP status codes

- 200 0K
- 201 CREATED
- 400 BAD REQUEST
- 401 UNAUTHORIZED
- 403 FORBIDDEN
- 404 NOT FOUND
- 405 METHOD NOT ALLOWED
- ...

HTTP status codes can be subdivided in:


- 1xx Informational
- 2xx Success
- 3xx Redirect
- 4xx Client Error
- 5xx Server Error