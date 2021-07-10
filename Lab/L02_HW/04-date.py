from datetime import date
print(int(date(*reversed([int(input('d: ')), int(input('m: ')), int(input('y: '))])).strftime('%j')))
