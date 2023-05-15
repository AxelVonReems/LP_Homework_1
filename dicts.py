from pprint import pprint

stock = [
    {'name': 'iPhone 12 Pro', 'stock': 24, 'price': 65432.1,
     'recommended': ['Samsung Galaxy S21', 'iPhone 12 Pro Max']},
    {'name': 'Samsung Galaxy S21', 'stock': 10, 'price': 56789.0,
     'discount': 5000},
    {'name': 'Xiaomi Mi 11', 'stock': 38, 'price': 44556.6},
]

stock[0]['recommended'].append('Xiaomi Mi 11')
stock[2]['price'] = stock[2]['price'] - 15000
pprint(stock)
print(type(stock))
print(type(stock[0]))
print(type(stock[0]['recommended']))
print(type(stock[0]['recommended'][0]))
