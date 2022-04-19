import json

car = """{"model": "Civic",
"make": "Honda",
"variants": ["Sedan", "Coupe"]}"""

print(car)
print(type(car))

car_dict = json.loads(car)

print(type(car))
print(type(car_dict))
print(car_dict)
print(car_dict['variants'])

with open('../data_file/currency.json') as json_file:
    data = json.load(json_file)
    print(data)

currency = {'Country': 'India', 'Currency': 'Rupee'}
print(type(currency))
json_var = json.dumps(currency)

print(json_var)
print(type(json_var))

with open('../data_file/currency.json', 'w') as json_file:
    json_file.write(json_var)

with open('../data_file/currency.json') as json_file:
    data = json.load(json_file)
    print(data)

written_data = json.load(open('../data_file/currency.json'))

print(written_data)

print('####################################################')

dessert = {'Name': 'Ice cream',
           'Flavours': ['Chocolate', 'Pineapple'],
           'Toppings': True,
           'WaffleCone': 'Yes'}

dessert_str = json.dumps(dessert)

print(dessert)
print(dessert_str)

with open('../data_file/eat.txt', 'w') as json_file:
    json.dump(dessert, json_file)

print('######################################################')

print(dessert)
print(json.dumps(dessert, indent=2))
print(json.dumps(dessert, separators=(':', '=')))
print(json.dumps(dessert, separators=('|', '-')))
print(json.dumps(dessert, sort_keys=True))
print(json.dumps(dessert, sort_keys=False))
