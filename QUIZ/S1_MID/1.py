
menu = {
    1: {'name': 'Latte', 'price': 40},
    2: {'name': 'Espresso', 'price': 45},
    3: {'name': 'Americano', 'price': 50},
    4: {'name': 'Mocca', 'price': 55},
    5: {'name': 'Cappuccino', 'price': 60}
}


def print_menu():
    print("""Coffee Menu
0. Finish
1. Latte = 40
2. Espresso = 45
3. Americano = 50
4. Mocca = 55
5. Cappuccino = 60""")


def order_coffee():

    tol_price = 0
    while True:
        cof_type = int(input("Coffee type: "))
        if cof_type == 0:
            print(f"Total price: {tol_price}")
            break
        else:
            amt = int(input(f"Amount of {menu[cof_type]['name']}: "))
            tol_price += menu[cof_type]['price'] * amt
            orders_dict = {menu[cof_type]['name']: amt}
    return orders_dict, tol_price


def change(total_price, pay):
    moneys = [1000, 500, 100, 50, 20, 10, 5, 1]
    rest = pay - total_price
    print(f"Customer's change: {rest}")
    for money in moneys:
        bankamt, rest = divmod(rest, money)
        if bankamt != 0:
            print(f"Change {money}: {bankamt}")


def print_receipt(orders_dict, customer_name, total_price):
    print(f"""--------- receipt ---------
CPE35 COFFEE SHOP
Customer name: {customer_name}
{' '.join(map(str, list(orders_dict.items())[0]))}, {total_price} baht
Thank you
---------------------------""")


def print_report(sales_dict):
    print(f"---- Daily Sale Report ----")
    if sales_dict == {}:
        print("Total sale: 0 baht")
    else:
        for i, j in sales_dict.items():
            print(i, j, 'bath')
        print(f"Total sale: {sum(sales_dict.values())} baht")
    print("---------------------------")


sales_dict = {}
while True:
    print_menu()
    customer_name = input("Customer name: ")
    if customer_name == "end day":
        break
    orders_dict, total_price = order_coffee()
    if customer_name not in sales_dict:
        sales_dict[customer_name] = total_price
    else:
        sales_dict[customer_name] += total_price

    pay = int(input("Customer pay: "))
    change(total_price, pay)
    print_receipt(orders_dict, customer_name, total_price)

print_report(sales_dict)
