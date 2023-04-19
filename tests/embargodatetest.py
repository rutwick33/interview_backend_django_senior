import unittest
import requests
from datetime import datetime

# Test 1: Return all values 
start_date = datetime.strptime('2023-03-04','%Y-%m-%d').date()
embargo_date = datetime.strptime('2023-06-04','%Y-%m-%d').date()

r = requests.get('http://127.0.0.1:8000/orders/date/{start}&{embargo}'.format(start=start_date, embargo=embargo_date))
items = len(r.json())
assert items == 5, "Expected 5 orders"
print('Start Date -', start_date, 'Embargo Date -',embargo_date,'\nExpected 5 order items. Got: ', items)
print('TEST PASSED!\n')

start_date = datetime.strptime('2023-04-15','%Y-%m-%d').date()
embargo_date = datetime.strptime('2023-06-04','%Y-%m-%d').date()

r = requests.get('http://127.0.0.1:8000/orders/date/{start}&{embargo}'.format(start=start_date, embargo=embargo_date))
items = len(r.json())
assert items == 3, "Expected 3 orders"
print('Start Date -', start_date,'Embargo Date -',embargo_date,'\nExpected 3 order items. Got: ', items)
print('TEST PASSED!\n')

start_date = datetime.strptime('2023-05-15','%Y-%m-%d').date()
embargo_date = datetime.strptime('2023-06-04','%Y-%m-%d').date()

r = requests.get('http://127.0.0.1:8000/orders/date/{start}&{embargo}'.format(start=start_date, embargo=embargo_date))
items = len(r.json())
assert items == 0, "Expected 0 orders"
print('Start Date -', start_date, 'Embargo Date -',embargo_date, '\nExpected 0 order items. Got: ', items)
print('TEST PASSED!\n')