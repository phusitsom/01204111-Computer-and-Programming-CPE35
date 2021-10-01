def mean(lst):
  try:
    return sum(lst)/len(lst)
  except:
    return 0

class City:
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    
class Country:
  def __init__(self, country, population, EU, coastline):
      self.country = country
      self.population = float(population)
      self.eu = EU
      self.coastline = coastline

with open(input('Enter city file: ')) as file:
  cities = [City(*row) for row in map(lambda x: x.split(','), file.read().splitlines()[1:])]
  
with open(input('Enter country file: ')) as file:
  countries = [Country(*row) for row in map(lambda x: x.split(','), file.read().splitlines()[1:])]
  filtered_countries = [c.country for c in countries if all((c.coastline=='yes',c.eu=='no'))]

print('Average temperature of countries having coastline, but not in EU:')
for c, t in [(country,mean([city.temperature for city in cities if city.country==country])) for country in filtered_countries]:
  if t: print(c,f'{t:.2f}')