n, k = map(int, input('Grass : ').split())
fenceHeight = [int(x) for x in input().split()]
print(sum(map(lambda h: h > k, fenceHeight)))
