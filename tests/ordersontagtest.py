import unittest
import requests

tag_no = 17

r = requests.get('http://127.0.0.1:8000/orders/tags/{tag}'.format(tag=tag_no))
orders = [item for item in r.json() if item['tags']]
items = len(orders)
assert items == 4, "Expected 4 Order with the Tag"
print('Tag Number: ', tag_no, '\nExpected 4 Orders. Got: ', items)
print('TEST PASSED!\n')


tag_no = 6

r = requests.get('http://127.0.0.1:8000/orders/tags/{tag}'.format(tag=tag_no))
orders = [item for item in r.json() if item['tags']]
items = len(orders)
assert items == 1, "Expected 1 Order with the Tag"
print('Tag Number: ', tag_no, '\nExpected 1 Orders. Got: ', items)
print('TEST PASSED!\n')


tag_no = 21

r = requests.get('http://127.0.0.1:8000/orders/tags/{tag}'.format(tag=tag_no))
orders = [item for item in r.json() if item['tags']]
items = len(orders)
assert items == 2, "Expected 2 Order with the Tag"
print('Tag Number: ', tag_no, '\nExpected 2 Orders. Got: ', items)
print('TEST PASSED!\n')