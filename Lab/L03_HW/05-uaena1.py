isChecked = False
PRODUCT = None

def What(PRODUCT_CODE:str):
    
    global isChecked
    global PRODUCT
    
    isChecked = True
    
    if PRODUCT_CODE.isupper:
        PRODUCT = 'Photobook'
    else: 
        PRODUCT = 'Album'
    
    print(PRODUCT)
        

def SStatus():
    if not isChecked:
        print("Dont Check")
    else: print(PRODUCT)

def RReal(PRODUCT_CODE:str):
    
    if PRODUCT_CODE[-1] == chr(ord(PRODUCT_CODE[1]) + 1):
        print(True)
    else: 
        print(False)

def main():
    What(PRODUCT_CODE)
    RReal(PRODUCT_CODE)

PRODUCT_CODE = input()

if __name__ == "__main__":
    main()

