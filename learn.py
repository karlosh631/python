import requests
x= requests.get("https://w3schools.com")
print(x.status_code)

def my_function():
    """This is a metadata docstring describing the function."""
    return "Hello, World!"
