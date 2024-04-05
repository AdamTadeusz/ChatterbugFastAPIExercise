# ChatterbugFastAPIExercise

# Requirements
- python 3.12.2
## Pip libraries
- fastapi 0.110.1
- uvicorn[standard] 0.29.0

(Python and library versions are versions used during development and testing)

# Installation
Install python 3.12.2

Open a new terminal and verify you are using the correct version of python with ```py --list```. The currently used version will be marked with an asterix

Run the following commands:

```py -m pip install 'fastapi==0.110.1'```
```py -m pip install uvicorn[standard]==0.29.0```

# Running the API
In a terminal, navigate to this folder, then run ```uvicorn main:app --reload```

# Testing the API
You can test the API using POSTMAN. To make calls to a locally running server first install the POSTMAN client

![Example of a correct query made to the API. There are no parameters in the url and instead a json object is defined in the body of the request, containing arguments for the password to be generated](./media/readmeMedia/exampleQuery.png)

See the documentation for list of all endpoints

# Documentation

FastAPI provides an automatically generated document you can view in the browser by visiting the "/docs" and "/redoc" endpoints while the server is running

## Endpoints

```/generate_password``` takes a json object sent in the body of the request. Example object is

```
{
    "length": 20,
    "capitals": true,
    "digits": true,
    "symbols": true
}
```

length: int or numeric string with a value >=8 and <=60. Defines length of generated password
capitals: bool. Toggles presence of capitals in generated password
digits: bool. Toggles presence of digits in generated password
symbols: bool. toggles presence of symbols in generated password