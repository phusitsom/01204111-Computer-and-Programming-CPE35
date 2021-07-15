number = input()
if(len(number) == 10):
    x = ['06', '08', '09']
    if number[0:2] in x:
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")
