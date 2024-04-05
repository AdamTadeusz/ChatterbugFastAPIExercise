# ChatterbugFastAPIExercise

# Requirements
- python 3.12.2
## Pip libraries
- fastapi
- uvicorn[standard]

# Installation
Install python 3.12.2

Open a new terminal and verify you are using the correct version of python with ```py --list```. The currently used version will be marked with an asterix.

Run the following commands
- ```py -m pip install 'fastapi==0.110.1'```
- ```py -m pip install uvicorn[standard]==0.29.0```

# Running the API
In a terminal, navigate to this folder, then run the following command
```uvicorn main:app --reload```