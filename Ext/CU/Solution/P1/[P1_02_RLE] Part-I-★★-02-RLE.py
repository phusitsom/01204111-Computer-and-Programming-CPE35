c = input()
if c == 'str2RLE':
    #stringเป็นRLE
    st = input()
    p = ''
    n = st[0]
    count = 0
    for i in range(len(st)):
        if n == st[i]:
            count += 1
        else:
            p = p[0:] + n + ' ' + str(count) + ' '
            n = st[i]
            count = 1
    p = p[0:] + n + ' ' + str(count) + ' '
    print(p)
elif c == 'RLE2str':
    #RLEเป็นstring
    st = input()
    st = st.split()
    for i in range(len(st)//2):
        n = int(st[2*i+1])
        print(st[i*2] * n, end='')
else:
    print('Error')