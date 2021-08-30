y, x = map(int, input("City Size: ").split())
city = [list(map(int, input().split())) for _ in range(y)]

N = list(zip(*city.copy()))
S = list(zip(*city.copy()[::-1]))
E = list(map(lambda x: x[::-1], city.copy()))
W = city.copy()

visibleT_views = {"N":0,
                  "S":0,
                  "E":0,
                  "W":0}

for direction, view in zip(visibleT_views,[N,S,E,W]):
    visibleT_views[direction] = sum([(1 + len([t for t in line[:line.index(max(line))+1] if t > line[0]])) for line in view])
    
print(" ".join([direction for direction in map(lambda d: d[0] if d[1]==max(visibleT_views.values()) else None, visibleT_views.items()) if direction != None]))