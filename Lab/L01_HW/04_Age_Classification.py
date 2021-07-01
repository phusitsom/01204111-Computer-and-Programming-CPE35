age = float(input('Enter your age : '))
def age_classification(age):
    if (age <= 12): return 'Child'
    elif (age > 12) & (age <= 18): return 'Adolescence'
    elif (age > 18) & (age <= 59): return 'Adult'
    else: return 'Senior Adult'

print('You are {}.'.format(age_classification(age)))
