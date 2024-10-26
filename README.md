# Remote-Procedure-Call

This project provides a simple Remote Procedure Call (RPC) system using UNIX sockets to facilitate communication between a Node.js client and a Python server. The client sends JSON-formatted requests, specifying a function and parameters, and the server dynamically executes the requested function, returning results to the client.
## Overview

    Server: A Python-based server that listens for incoming requests on a UNIX socket, parses the requested function, executes it, and sends the response.
    Client: A Node.js client that reads requests from a JSON file (request.json), connects to the server, sends each request, and logs the server’s response.

## Prerequisites
- Python 3.x (for the server)
- Node.js (version 12 or later for the client)

## Getting started
### Setup

    Clone this repository.
    Ensure Python and Node.js are installed on your system.
    Place your desired function definitions in server/functions.py.
    Create a request.json file in the root directory for client requests (see format below).

### Server Setup and Usage

    Define Functions
    Modify or add functions in server/functions.py as needed. Ensure each function corresponds to a name used in the function_hash dictionary in server.py.

    Start the Server
    Start the server with the following command:
    
```
    python server.py
```

    The server will listen for connections on the UNIX socket file ./tmp/socket_file.

    Server Code Explanation
        function_hash: Maps function names to their respective implementations in server/functions.py.
        Connection Handling: The server listens for incoming connections, decodes JSON requests, validates function names and parameters, executes the function, and sends the response back.

## JSON Request Format

Each client request sent to the server should be a JSON object with the following structure:

json

{
    "id": 1,
    "method": "nroot",
    "params": [16, 2],
    "params_types": ["int", "int"]
}

    id: A unique identifier for tracking responses.
    method: The name of the function to execute.
    params: Parameters to pass to the function.
    params_types: The types of each parameter (e.g., "int", "float").

Sample JSON Response from Server

The server responds with either a result or an error message, as shown:

json

{
    "id": 1,
    "type": "result",
    "value": 4.0
}

For invalid requests or errors, the response includes an error message:

json

{
    "id": 1,
    "type": "error",
    "value": "Invalid function"
}

Client Setup and Usage

    Prepare request.json
    Create a request.json file with the list of requests. Each request should adhere to the JSON request format above.

    Run the Client
    Execute the client script with:

    bash

    node client.js

    Client Code Explanation
        sendRequest(request): Connects to the server, sends a JSON request, receives and parses the JSON response, and logs it.
        main(): Reads request.json, parses each request, and processes it sequentially.

Example request.json Format

json

[
    {
        "id": 1,
        "method": "floor",
        "params": [15.7],
        "params_types": ["float"]
    },
    {
        "id": 2,
        "method": "nroot",
        "params": [16, 2],
        "params_types": ["int", "int"]
    }
]

Sample Output

When running client.js, you will see output similar to the following if the server processes requests successfully:

plaintext

Connected to server
Received data: { id: 1, type: 'result', value: 15 }
Disconnected from server
Connected to server
Received data: { id: 2, type: 'result', value: 4.0 }
Disconnected from server

Error Handling

    Server Errors: If the server encounters an error, such as an undefined function or parameter mismatch, it returns a JSON error message.
    Connection Errors: Both client and server handle connection errors, ensuring the client logs issues if the server is unavailable.

Notes

    Ensure the server is running before starting the client.
    Ensure request.json is properly formatted as per the JSON Request Format.
    Make sure server/functions.py contains all the functions specified in the client requests.

This RPC system provides a simple framework for UNIX socket-based remote function execution, suitable for controlled environments and educational purposes.
