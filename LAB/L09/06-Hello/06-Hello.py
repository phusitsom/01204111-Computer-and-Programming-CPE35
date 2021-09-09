wrt = """def greeting(name):
    print(f"Hello, {name}")"""
try:
    with open('mymodule.py','x') as file:
        file.write(wrt)
except:
    pass
    
import mymodule

mymodule.greeting(input('Name : '))