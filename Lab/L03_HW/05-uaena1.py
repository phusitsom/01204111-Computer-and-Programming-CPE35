isChecked = False
PRODUCT = None

def What(PRODUCT_CODE:str):
    
    global isChecked
    global PRODUCT
    
    isChecked = True
    
    if 64 <= ord(PRODUCT_CODE[0]) <= 90:
        PRODUCT = 'Photobook'
    else: 
        PRODUCT = 'Album'
    
    return PRODUCT
        

def SStatus():
    if not isChecked:
        return "Dont Check"
    else: 
        return PRODUCT


def RReal(PRODUCT_CODE:str):
    if PRODUCT_CODE[-1] == chr(ord(PRODUCT_CODE[0]) + 1):
        return True
    else: 
        return False


PRODUCT_CODE = input()

print(What(PRODUCT_CODE))
print(RReal(PRODUCT_CODE))
