def sum_price():
    print("""Menu\n0. Finish\n1. Latte = 40\n2. Espresso = 45\n3. Americano = 50\n4. Mocca = 55\n5. Cappuccino = 60""")
    menu = [None, 40, 45, 50, 55, 60]
    total = 0
    while(True):
        n = int(input("coffee : "))
        if n == 0:
            break
        amt = int(input("amount : "))
        total += amt * menu[n]
    print(f"total price : {total}")
    return total


def change(total_price, pay):
    rest = pay - total_price
    print(f"customer's change : {rest}")
    moneys = [1000, 500, 100, 50, 20, 10, 5]

    for money in moneys:
        bankamt, rest = divmod(rest, money)
        if bankamt != 0:
            print(f"change {money} : {bankamt}")


total = sum_price()
pay = int(input("customer pay : "))
change(total, pay)
