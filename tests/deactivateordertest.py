import requests
import unittest

r = requests.get('http://127.0.0.1:8000/orders/deactivate/1')

valid_response = "[\"Success:Deactivate Order\"]"
assert r.text == valid_response, "Could not Deactivate Order"
print('\nTEST PASSED!\n', r.text)