import json
with open(input('Enter json filename : ')) as file:
    data = json.loads(file.read())
    
product_prices = {x['product_name']:int(x['price']) for x in data['products']}

def change(_total_price, _pay):
    _change = _pay - _total_price
    if _change == 0:
        print('no change')
    else:
        for money in [1000, 500, 100, 50, 20, 10, 5, 2, 1]:
            bankamt, _change = divmod(_change, money)
            if bankamt != 0:
                print(f"{money} : {bankamt}")

for customer in sorted(data['customers'], key= lambda x: x['customer_name']):
    name = customer['customer_name']
    total_price = sum([product_prices[prod]*quan for prod, quan in customer['order'].items()])
        
    print(name)
    change(total_price, customer['money'])
    print()