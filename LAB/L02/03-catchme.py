policeDistance = 0
criminalDistance = 100
count = 1
while policeDistance < criminalDistance:
    policeDistance += int(input('Input distance: '))
    criminalDistance += 2**count
    count += 1
    print(
        f'Police distance: {policeDistance}\nCriminal distance: {criminalDistance}')
print('Caught him!')
