# MicroservicesA

This microservice provides an auto-generated password based on the parameters entered into it. Users enter in the specific amount of each character they want as a number in the order of length, uppercase, lowercase, number, special. The program returns back the generated password encoded in base64.

## How to Use

- Download the program and verify that the program is running on the same server as your main program
- Run the program

## Communication Contract

### Example Request Code (Python)

There is a given function located in the 'testReq.py' file. The req_message() function can be copied in order to implement it.
Once copied, requests for passwords can be made like so:

```python
req_message(length, uppercase, lowercase, numbers, special)
```

### Receiving Data

The provided function also receives the password, so data can be received by simply assigning it to a variable, or any other way.

```python
password = req_message(length, uppercase, lowercase, numbers, special)
```
