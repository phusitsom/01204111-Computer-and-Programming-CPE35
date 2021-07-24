from collections import Counter
luxnum = input("Enter lucky number : ")
n = int(input("Enter amount of candidates : "))
cards = [input(f"Enter ID card number {(i)}: ") for i in range(1,n+1)]
m = []
for card in cards: m.append(Counter(card)[luxnum])
print("Winner:",max([cards[i] for i in [i for i, e in enumerate(m) if e == max(m)]]))