import statistics


class StudentData:

    def __init__(self, data: list = None):
        if data == None:
            self.data = []
        else:
            self.data = data
            self.mean = statistics.mean(self.data)
            self.min = min(self.data)
            self.max = max(self.data)

    def update_describe(self):
        self.mean = statistics.mean(self.data)
        self.min = min(self.data)
        self.max = max(self.data)

    def add(self, item: int):
        self.data.append(item)
        self.update_describe()

    def print_score(self):
        for i, score in enumerate(self.data):
            print(f"Student #{i+1} score: {score}")

    def describe(self):
        print(
            f"Average score is {self.mean:.2f}\nMinimum score is {self.min}\nMaximum score is {self.max}")

    def print_ranking(self):
        for i, score in enumerate(sorted(self.data)[::-1]):
            print(f"Rank #{i+1}: {score}")


data = StudentData()
while True:
    inp = input("Input student score (or ENTER to end): ")
    if inp == '':
        break
    data.add(int(inp))
data.print_ranking()
