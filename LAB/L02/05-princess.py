sInput = int(input('s: '))
m, s = divmod(sInput, 60)
h, m = divmod(m, 60)
print(f'{sInput} seconds equals {h} hour(s) {m} minute(s) and {s} second(s)')
# print(f'{sInput} seconds equals {int((sInput/60)/60)} hour(s) {int(sInput/(60))%60} minute(s) and {sInput%60} second(s)')
