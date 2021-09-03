with open(input("File name: ")) as file:
    lines = file.read().splitlines()
    
#   Print all lines
for line in lines:
    print(line)
    
#   Get the index of "Price" & "List"
price_index = lines.index("Price")
list_index = lines.index("List")

#   Check if price_index comes first
if price_index < list_index:
    slice1 = price_index
    slice2 = list_index
else:
    slice1 = list_index
    slice2 = price_index


data1 = {}
data2 = {}

"""
data1 is for the table that comes first (lines[slice1+1:slice2])
data2 is for the table that comes last (lines[slice2+1:])
"""

for line in lines[slice1+1:slice2]:
    item, price = line.split()

    data1.update({item: int(price)})

for line in lines[slice2+1:]:
    item, quantity = line.split()

    data2.update({item: int(quantity)})

"""
Calculate the total price by multiplying price and quantity 
and sum those multiplied numbers.
"""
total = 0
for item, num in data2.items():
    total += num*data1.get(item, 0)

print("Total price:", total)
