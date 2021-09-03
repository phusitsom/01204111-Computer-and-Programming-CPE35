print((lambda file_string: f"There are {len(file_string.split('.'))-1} sentences and {len(file_string.split())} words.")(open(input("File name: ")).read()))
