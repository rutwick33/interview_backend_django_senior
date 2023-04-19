import unittest
import requests

# Test 1: Return all values 
order_no = 2

r = requests.get('http://127.0.0.1:8000/orders/{order}/tags/'.format(order=order_no))
items = len(r.json()['tags'])
assert items == 3, "Expected 3 tags on Order"
print('Order Number: ', order_no, '\nExpected 3 Tags. Got: ', items)
print('TEST PASSED!\n')

order_no = 4

r = requests.get('http://127.0.0.1:8000/orders/{order}/tags/'.format(order=order_no))
items = len(r.json()['tags'])
assert items == 4, "Expected 4 tags on Order"
print('Order Number: ', order_no, '\nExpected 4 Tags. Got: ', items)
print('TEST PASSED!\n')

order_no = 1

r = requests.get('http://127.0.0.1:8000/orders/{order}/tags/'.format(order=order_no))
items = len(r.json()['tags'])
assert items == 3, "Expected 5 tags on Order"
print('Order Number: ', order_no, '\nExpected 3 Tags. Got: ', items)
print('TEST PASSED!\n')