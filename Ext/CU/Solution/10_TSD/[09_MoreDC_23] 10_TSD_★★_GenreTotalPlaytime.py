n = int(input())
song = {}
for i in range(n):
    s = input().strip().split(', ')
    m = s[3].split(':')
    min = int(m[0]) * 60 + int(m[1])
    if s[2] in song:
        song[s[2]] += min
    else: song[s[2]] = min
songg = [[song[n], n] for n in song]
songg.sort(reverse = -1)
c = 0
while c < 3 and c < len(songg):
    min = songg[c][0] // 60
    sec = str(songg[c][0] - min * 60)
    sec = '0'*(2-len(sec)) + sec
    print(songg[c][1] + ' --> ' + str(min) + ':' + str(sec))
    c += 1