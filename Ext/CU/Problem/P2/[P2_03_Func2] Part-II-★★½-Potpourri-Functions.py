def convex_polygon_area(p):
    det = 0
    for i in range(len(p)):
        if i == len(p) - 1:
            det += p[i][0] * p[0][1]
            det -= p[0][0] * p[i][1]
        else:
            det += p[i][0] * p[i + 1][1]
            det -= p[i + 1][0] * p[i][1]
    return abs(det) * (0.5)


def is_heterogram(s):
    s = s.lower()
    s1 = ''
    for i in range(len(s)):
        if s[i] in [' ', ',', '"', "'", '(', ')']:
            s1 += ''
        else:
            s1 += s[i]
    for i in range(len(s1)):
        if s1[i] in s1[i + 1:]:
            return False
    return True


def replace_ignorecase(s, a, b):
    a = a.lower()
    s1 = ''
    while s.lower().find(a) != -1:
        c = s.lower().find(a)
        s = s[:c] + '_' + s[c + len(a):]
    for i in range(len(s)):
        if s[i] == '_':
            s1 += b
        else:
            s1 += s[i]
    return s1


def top3(votes):
    votelist = []
    for key in votes:
        votelist.append([-votes[key], key])
    votelist.sort()
    ans = []
    c = 0
    while c < len(votelist) and c < 3:
        ans.append(votelist[c][1])
        c += 1
    return ans


# ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
for k in range(2):
    exec(input().strip())
