class Product:
    def __init__(self, *args) -> None:
        self.ID, self.type, self.price = args


products = [Product(*tuple(map(lambda m: int(m) if m.isnumeric() else m, input().strip().split())))
            for _ in range(int(input('How many products are there? : ')))]

mapped_products = {product.ID: product for product in products}

while True:
    inp_id = int(input('Id : '))
    product = mapped_products.get(inp_id, False)
    
    q = 1
    
    if product:
        while True:

            q = int(input('Q : '))
            
            if q in (0, 3): break
            
            print((product.type, product.price)[q-1])

    else: 
        print("This id doesn't exist.")

    if not q: break
