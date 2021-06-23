def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

name = input()
if (len(name) < 1) | (len(name) > 15):
    None
else:
    for i in range(len(name)):
        print(replace_str_index(name,i,name[i].upper()))

