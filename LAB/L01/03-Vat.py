priceWvat = float(input('summary price : '))

priceWOvat = (priceWvat/107)*100
print('food :', priceWOvat)
vat = priceWvat - priceWOvat

print('vat :', vat)
