name = input().strip()
fn = open(name,'r')
comm = fn.readline().strip()
pattern = fn.readline().strip()
if comm == 'T2M':
    morse_ans = []
    for text in fn:
        text = text.strip()
        morse = ''
        check = True
        for e in text:
            j = pattern.find('[' + e + ']')
            if j == -1:
                check = False
            j += 3
            k = pattern.find('[', j)
            morse += pattern[j:k] + ' '
        if check:
            morse_ans.append(morse)
        else:
            morse_ans.append('Invalid : '+text)
    for i in morse_ans:
        print(i)

elif comm == 'M2T':
    text_ans = []
    for morse1 in fn:
        morse = morse1.strip().split()
        text = ''
        check = True
        for e in morse:
            j = pattern.find(']' + e + '[')
            if j == -1:
                check = False
            text += pattern[j-1]
        if check:
            text_ans.append(text)
        else:
            text_ans.append('Invalid : '+morse1.strip())
    for i in text_ans:
        print(i)

else:
    print('Invalid code')

fn.close()