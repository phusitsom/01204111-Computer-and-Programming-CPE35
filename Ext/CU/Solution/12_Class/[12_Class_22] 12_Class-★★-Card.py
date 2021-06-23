class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def getScore(self):
        n = 1
        if self.value in ['J', 'Q', 'K']:
            n = 10
        elif self.value == 'A':
            n = 1
        else:
            n = int(self.value)
        return n

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self, rhs):
        card1 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        a = card1.index(self.value)
        b = card1.index(rhs.value)
        if a == b:
            card2 = ['club', 'diamond', 'heart', 'spade']
            c = card2.index(self.suit)
            d = card2.index(rhs.suit)
            return c < d
        return a < b


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n - 1):
    print(Card.sum(cards[i], cards[i + 1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])