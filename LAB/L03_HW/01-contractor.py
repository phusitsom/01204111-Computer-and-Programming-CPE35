from math import pi

def inputShape():
    return int(input("Input Shape: "))

def calculateSphere():
    rad = int(input("Input radius(meter): "))
    volume = (4*pi*(rad**3))/3
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculateCone():
    rad = int(input("Input radius(meter): "))
    h = int(input("Input height(meter): "))
    volume = 1/3*pi*(rad**2)*h
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculateCylinder():
    rad = int(input("Input radius(meter): "))
    h = int(input("Input height(meter): "))
    volume = pi*(rad**2)*h
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume
    

def calculatePrism():
    w = int(input("Input width(meter): "))
    l = int(input("Input length(meter): "))
    h = int(input("Input height(meter): "))
    volume = w*l*h
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume
    
    
def calculatePyramid():
    w = int(input("Input width(meter): "))
    l = int(input("Input length(meter): "))
    h = int(input("Input height(meter): "))
    volume = ((w * l)*h)/3
    print(f"The volume is {volume:.2f} cubic meter.")
    return volume

def calculatePrice(v):
    priceWeight = int(input('Price(Bath) per 1 cubic meter: '))
    print(f"The price is {v*priceWeight:.2f} Baht.")

shape = inputShape()
if shape == 1:v = calculateSphere()
elif shape == 2:v = calculateCone()
elif shape == 3: v = calculateCylinder()
elif shape == 4: v = calculatePrism()
elif shape == 5: v = calculatePyramid()
calculatePrice(v)