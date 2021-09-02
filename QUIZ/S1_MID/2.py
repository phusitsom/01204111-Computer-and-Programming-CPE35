perc_to_grade = {
    85: "A",
    79: "B+",
    73: "B",
    67: "C+",
    60: "C",
    50: "D+",
    40: "D",
    0: "F"
}

grade_std_count = {g: 0 for g in perc_to_grade.values()}

with open('MID/midterm.csv') as fp:
    data = (lambda x: [dict(zip(x[0].split(','), row.split(',')))
            for row in x[1:] if 'Midterm' in row])(fp.read().splitlines())

print(len(data))

(lambda scores: print(f"{max(scores)} {sum(scores)/len(scores):.2f} {(sum([(score -(sum(scores)/len(scores)))**2 for score in scores])/len(scores))**0.5:.2f} {min(scores)}"))(
    [int(row['Score']) for row in data])

percs = [float(row['Percentage']) for row in data]

for perc in percs:
    for perc_grade in perc_to_grade:
        if perc > perc_grade:
            grade = perc_to_grade[perc_grade]
            grade_std_count[grade] += 1
            break

print("\n".join([": ".join(map(str, grade))
      for grade in (grade_std_count.items())]))
