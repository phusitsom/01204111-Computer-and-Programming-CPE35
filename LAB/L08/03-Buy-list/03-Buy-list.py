with open(input("File name: ")) as file:
    lines = file.read().splitlines()

list(map(print, lines))[0]
price_index = lines.index("Price")
list_index = lines.index("List")
slice1 = price_index if price_index < list_index else list_index
slice2 = list_index if price_index < list_index else price_index


price_data = (lambda x: {i: int(j) for i, j in x})(
    list(map(lambda x: x.split(), lines[slice1+1:slice2])))
list_data = (lambda x: {i: int(j) for i, j in x})(
    list(map(lambda x: x.split(), lines[slice2+1:])))

print("Total price:", sum([num*price_data.get(item, 0)
      for item, num in list_data.items()]))
