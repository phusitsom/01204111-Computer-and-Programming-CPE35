for __pbk, __pvk in zip(open(input("Enter publickey filename : ")).read().splitlines(), open(input("Enter privatekey filename : ")).read().splitlines()):
    print(''.join([chr(97 + ((ord(i) + ord(j)) % 26)) for i, j in zip(__pbk, __pvk)])) if __pvk[0].isnumeric(
    ) else print(''.join([chr(65 + ((ord(i) + ord(j)) % 26)) for i, j in zip(__pbk, __pvk)]))
