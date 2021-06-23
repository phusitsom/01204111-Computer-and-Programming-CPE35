class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def next1(self):
        card1 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3']
        card2 = ['club', 'diamond', 'heart', 'spade']
        if self.suit == 'spade':
            newsuit = 'club'
            newvalue = card1[card1.index(self.value) + 1]
        else:
            k = card2.index(self.suit)
            newsuit = card2[k + 1]
            newvalue = self.value
        return Card(newvalue, newsuit)

    def next2(self):
        nextcard = self.next1()
        self.value = nextcard.value
        self.suit = nextcard.suit


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])