import requests
import unittest

r = requests.get('http://127.0.0.1:8000/inventory/date/2023-03-04')
t = requests.get('http://127.0.0.1:8000/inventory/date/2024-03-04')

items = len(r.json())
assert items == 17, "Expected 17 inventory items"
print('\n2023-03-04 Date - Expected 17 inventory items. Got: ', items)
print('TEST PASSED!\n')

items = len(t.json())
assert items == 0, "Expected 0 inventory items"
print('2024-03-04 Date - Expected 0 inventory items. Got: ', items)
print('TEST PASSED!\n')