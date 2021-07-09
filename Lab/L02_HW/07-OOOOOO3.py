ew = -(-int(input())//2)
for i in range(ew): print(' '*(ew-i-1) + 'O'*(2*i+1))
for i in range(ew-1,0,-1): print((ew-i) * (" ") + (i*"O") + ('O'*(i-1)))