import unittest
import requests

r = requests.get('http://127.0.0.1:8000/inventory?limit=4&offset=5')
print(r.json())
# items = len(r.json()['tags'])
# assert items == 3, "Expected 3 tags on Order"
# print('Order Number: ', order_no, '\nExpected 3 Tags. Got: ', items)
# print('TEST PASSED!\n')