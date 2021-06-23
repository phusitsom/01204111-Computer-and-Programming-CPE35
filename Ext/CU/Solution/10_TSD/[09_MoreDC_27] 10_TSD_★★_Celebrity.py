def knows(R,x,y):
# return True if x knows y
    return y in R[x]

def is_celeb(R,x): # return True if a is celeb, otherwise return False
# return False if x knows someone who is not him/herself
# return False if there exists someone in R who don't know x
# otherwise return True
    if R[x] != set() and R[x] != {x}:
        return False
    for i in R:
        if i != x and x not in R[i]:
            return False
    return True

def find_celeb(R):
# for each person x in the party
# if x is celeb --> return x
# if no celeb in the party --> return None
    for person in R:
        if is_celeb(R,person):
            return person

def read_relations() :
# build a dictionary R from inputs
# whose structure is shown in the example
    R = dict()
    a = set()
    while True:
        d = input().split()
        if len(d) == 1 : break
        a.add(d[0])
        a.add(d[1])
        if d[0] in R:
            R[d[0]].add(d[1])
        else:
            R[d[0]] = {d[1]}
    for i in a:
        if i not in R:
            R[i] = set()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip()) # do not remove this line