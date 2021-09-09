import json
with open(input('Filename : ')) as file:
    data = json.loads(file.read())
prod_type = input()
print((lambda p, v: f'{p} : {v}')(*min(((product['Brand'], int(product['Cost'])) for product in data if product['Product type'] == prod_type), key= lambda x: x[1])))