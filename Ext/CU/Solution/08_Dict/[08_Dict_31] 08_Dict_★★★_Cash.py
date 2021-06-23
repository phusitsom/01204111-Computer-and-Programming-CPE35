def total(pocket):
    total = 0
    for key in pocket:
        total += key * pocket[key]
    return total


def take(pocket, money_in):
    for key in money_in:
        if key in pocket:
            pocket[key] += money_in[key]
        else:
            pocket[key] = money_in[key]
    return pocket


def pay(pocket, amt):
    new_poc = []
    for key in pocket:
        new_poc.append([key, pocket[key]])
    new_poc.sort(reverse=1)
    paid_poc = []
    if total(pocket) < amt:
        return {}
    else:
        k = 0
        for i in new_poc:
            if int(i[1]) <= amt // i[0]:
                amt -= new_poc[k][0] * i[1]
                paid_poc.append([i[0], i[1]])
                new_poc[k][1] = 0
            else:
                if amt // i[0] != 0:
                    paid_poc.append([i[0], amt // i[0]])
                new_poc[k][1] -= (amt // i[0])
                amt -= (amt // i[0]) * i[0]
            k += 1
        # print(i,amt,new_poc,pocket,paid_poc)
        if amt == 0:
            for key in new_poc:
                pocket[key[0]] = key[1]
            paid = {}
            for i in paid_poc:
                paid[i[0]] = i[1]
            return paid
        else:
            return {}


exec(input().strip())