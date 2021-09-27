import statistics


class StudentData:

    def __init__(self, data: list = None):
        if data == None:
            self.data = []
        else:
            self.data = data

    def __repr__(self) -> str:
        return repr(self.data)

    def update_param(self) -> None:
        self.mean = statistics.mean(self.data)
        self.min = min(self.data)
        self.max = max(self.data)
        try:
            self.stdev = statistics.stdev(self.data)
        except:
            self.stdev = 0

        if not all(map(lambda x: x == self.max, self.data)):
            self.grades = {
                self.mean+self.stdev*1.5: "A",
                self.mean+self.stdev: "B+",
                self.mean+self.stdev/2: "B",
                self.mean: "C+",
                self.mean-self.stdev/2: "C",
                self.mean-self.stdev: "D+",
                self.mean-self.stdev*1.5: "D",
                0: "F"
            }
        else:
            self.grades = {
                0: "A"
            }

    def add(self, item: int) -> None:
        self.data.append(item)
        self.update_param()

    def input_scores(self):
        while True:
            inp = input("Input student score (or ENTER to end): ")
            if inp == '':
                break
            self.add(int(inp))

    def print_score(self) -> None:
        for i, score in enumerate(self.data):
            print(f"Student #{i+1} score: {score}")

    def print_params(self, *params: str) -> None:
        for param in params:
            if param.lower() in ['mean', 'avg', 'average']:
                print(f"Average score is {self.mean:.2f}")
            if param.lower() in ['std', 'stdev', 'standard deviation']:
                print(f"Standard deviation is {self.stdev:.2f}")
            if param.lower() in ['min', 'minimum']:
                print(f"Minimum score is {self.min}")
            if param.lower() in ['max', 'maximum']:
                print(f"maximum score is {self.max}")

    def print_grading(self) -> None:
        for i, score in enumerate(self.data):
            for score_grade in self.grades:
                if score > score_grade:
                    grade = self.grades[score_grade]
                    break
            print(f"Student #{i+1} score: {score} grade: {grade}")

    def print_ranking(self) -> None:
        for i, score in enumerate(sorted(self.data)[::-1]):
            print(f"Rank #{i+1}: {score}")


stddata = StudentData()
stddata.input_scores()
stddata.print_params('mean', 'stdev')
stddata.print_grading()
