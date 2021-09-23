class Country:
  nbCountry = 0
  def __init__(self, country, population, EU, coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1
    
with open(input('Enter File name: ')) as file:
    countries = [Country(*row) for row in map(lambda x: x.split(','), file.read().splitlines()[1:])]
    
for country in countries:
    if country.EU == 'no' and country.coastline == 'yes':
        print(country.country, country.population)