print(
    (lambda file_name: f"There are {len(open(file_name).read().split('.'))-1} sentences and {len(open(file_name).read().split())} words.")(input("File name: ")))