wife = int(input())
price = list(map(int, input().split()))
if len(price) == wife:
    total_price = sum(price)

    print(total_price)
else:
    print("1 DISH PER WIFE")
