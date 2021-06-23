ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']


class roman:
    def __init__(self, r):
        self.ones = 0
        self.tens = 0
        self.hundreds = 0
        self.thousands = 0
        n = r
        while n[0] == 'M':
            self.thousands += 1
            n = n[1:]
            if n == '': break
        for i in range(9, -1, -1):
            x = n.find(hundreds[i])
            if x == 0:
                self.hundreds = i
                n = n[len(hundreds[i]):]
                break
        for i in range(9, -1, -1):
            x = n.find(tens[i])
            if x == 0:
                self.tens = i
                n = n[len(tens[i]):]
                break
        for i in range(9, -1, -1):
            x = n.find(ones[i])
            if x == 0:
                self.ones = i
                n = n[len(ones[i]):]
                break
        # print(self.thousands, self.hundreds, self.tens, self.ones)

    def __lt__(self, rhs):
        return (self.thousands * 1000 + self.hundreds * 100 + self.tens * 10 + self.ones * 1) < (
                    rhs.thousands * 1000 + rhs.hundreds * 100 + rhs.tens * 10 + rhs.ones * 1)

    def __str__(self):
        return self.thousands * 'M' + hundreds[self.hundreds] + tens[self.tens] + ones[self.ones]

    def __int__(self):
        return self.thousands * 1000 + self.hundreds * 100 + self.tens * 10 + self.ones * 1

    def __add__(self, rhs):
        ans = (self.thousands * 1000 + self.hundreds * 100 + self.tens * 10 + self.ones * 1) + (
                    rhs.thousands * 1000 + rhs.hundreds * 100 + rhs.tens * 10 + rhs.ones * 1)
        self.ones = ans % 10
        self.tens = (ans % 100) // 10
        self.hundreds = (ans % 1000) // 100
        self.thousands = ans // 1000
        return self


t, r1, r2 = input().split()
a = roman(r1);
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))