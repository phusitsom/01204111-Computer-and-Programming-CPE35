def reverse(d):
    d_new = {}
    for key in d:
        d_new[d[key]] = key
    return d_new


def keys(d, v):
    x = []
    for key in d:
        if d[key] == v:
            x.append(key)
    return x


exec(input().strip())
