signal = input()
nath = abs(ord(signal[0]) - ord(signal[-1]))
if  nath == 32 or nath == 0:
    print(f"YES\n{signal[0].upper()}")
else:
    print(f"NO")