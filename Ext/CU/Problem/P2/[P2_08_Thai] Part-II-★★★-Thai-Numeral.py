code = {0: 'soon', 1: 'neung', 2: 'song', 3: 'sam', 4: 'si',
        5: 'ha', 6: 'hok', 7: 'chet', 8: 'paet', 9: 'kao', 10: 'sip'}


def to_Thai(N):
    out = ""
    c = False
    if N == 0:
        out += 'soon'
    else:
        if N >= 1000:  # จัดกำรหลักพัน
            c = True
            out += code[N//1000] + ' pun '
            N %= 1000
        if N >= 100:  # จัดกำรหลักร้อย
            c = True
            out += code[N//100] + ' roi '
            N %= 100
        if N >= 10:  # จัดกำรหลักสสิบ
            c = True
            if N//10 == 2:
                out += 'yi sip '
            elif N//10 == 1:
                out += 'sip '
            else:
                out += code[N // 10] + ' sip '
            N %= 10
        if N >= 1:
            if c and N == 1:
                out += 'et'
            else:
                out += code[N]
    return out


exec(input().strip())
