y, x = map(int, input("City Size: ").split())
city = [tuple(map(int, input().split())) for _ in range(y)]

N = list(zip(*city.copy()))  # Rotate City -90 Degrees
S = list(zip(*city.copy()[::-1]))  # Rotate City 90 Degrees
E = list(map(lambda x: x[::-1], city.copy()))  # Rotate City 90 Degrees
W = city.copy()


"""
City
[
    (2, 3, 5, 6, 2), 
    (1, 3, 4, 7, 1), 
    (6, 5, 4, 1, 3), 
    (2, 3, 7, 9, 6)
]
North   # Rotate City -90 Degrees
[
    > (2, 1, 6, 2), 
    > (3, 3, 5, 3), 
    > (5, 4, 4, 7), 
    > (6, 7, 1, 9), 
    > (2, 1, 3, 6)
]

South   # Rotate City 90 Degrees
[
    > (2, 6, 1, 2),
    > (3, 5, 3, 3),
    > (7, 4, 4, 5),
    > (9, 1, 7, 6),
    > (6, 3, 1, 2)
]

East    # Rotate City 180 Degrees
[
    > (2, 6, 5, 3, 2), 
    > (1, 7, 4, 3, 1), 
    > (3, 1, 4, 5, 6), 
    > (6, 9, 7, 3, 2)
]

West    # No More Rotate
[
    > (2, 3, 5, 6, 2), 
    > (1, 3, 4, 7, 1), 
    > (6, 5, 4, 1, 3), 
    > (2, 3, 7, 9, 6)
]
"""


visibleT_directions = {"N": 0,
                       "S": 0,
                       "E": 0,
                       "W": 0}

for direction, city_view in zip(visibleT_directions, [N, S, E, W]):

    """
    1st iter
    direction -> 'N'
    ciry_view -> [(2, 1, 6, 2), (3, 3, 5, 3), (5, 4, 4, 7), (6, 7, 1, 9), (2, 1, 3, 6)]
    """

    for line in city_view:

        """
        1st iter
        line -> (2, 1, 6, 2)
        """

        first_T = line[0]  # = 2
        visibleT = [first_T]  # = [2]

        tallest_T = line.index(max(line))  # = 6 (Index of max(line))
        first_to_tallest = line[:tallest_T+1]  # = (2,1,6)

        for T in first_to_tallest:
            if T > first_T:  # 6 > 2 -> True
                visibleT.append(T)  # visibleT.append(6)

        # visibleT_directions["N"] += len([2,6])
        visibleT_directions[direction] += len(visibleT)

for direction, val in visibleT_directions.items():
    """
    1st iter
    direction -> "N"
    val -> 12
    """
    print_lst = []
    if val == max(visibleT_directions.values()):  # Find the key with maximum value
        print_lst.append(direction)  # Add key to print_lst

    print_str = " ".join(print_lst)

print(print_str)
