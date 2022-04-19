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