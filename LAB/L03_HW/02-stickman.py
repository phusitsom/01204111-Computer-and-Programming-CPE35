n = int(input())
w = 'o'
def Head(n):
    print(" "+w*n)
    for i in range(int(n/2)-1):
        print(" "+w+(" " * len((w*n)[1:-1]))+w)
    print(" "+w*n)
def Body(n):
    for i in range(int(n/2)-1):
        print((' '*int(n/2))+'||')
    print(('-'*int(n/2))+'||'+('-'*int(n/2)))
    for i in range(int(n/2)-1):
        print((' '*int(n/2))+'||')
def Leg(n):
    for i in range(int(n/2), 0, -1):
            print((" "*i+"/")+(" "*((-(i-int(n/2))*2))+"\\"))
            
Head(n)
Body(n)
Leg(n)