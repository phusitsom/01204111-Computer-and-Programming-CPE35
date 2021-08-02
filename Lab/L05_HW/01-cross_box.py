n, char= int(input()), "."
print(char * n)
for i in range((n//2)-1):print(char + ' ' * i + char + ' ' * (n-2*(2+i))+ char + ' ' * i + char)
print(char + ' ' * ((n//2)-1) + char + ' ' * ((n//2)-1) + char)
for i in range((n//2)-1):print(char + ' ' * ((n//2)-(2+i)) + char + ' ' * (1+(i*2)) + char+ ' ' * ((n//2)-(2+i)) + char)
print(char * n)
