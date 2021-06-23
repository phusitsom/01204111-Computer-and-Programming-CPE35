n = int(input())
if(n%2==0):
    x = "even"
else: x = "odd"
if(n>0):
    y = "positive"
elif(n==0):
    y = "zero"
else: y = "negative"
print(y)
print(x)