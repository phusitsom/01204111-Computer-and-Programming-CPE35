def mean(lst):
    return sum(lst)/len(lst)

class City:
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    
with open(input('Enter file name: ')) as file:
  cities = [City(*row) for row in map(lambda x: x.split(','), file.read().splitlines()[1:])]
  countries = [city.country for city in cities]
  countries = sorted(set(countries), key=countries.index)
  
for c, t in [(country,mean([city.temperature for city in cities 
                            if city.country==country])) for country in countries]:
  print(c,f'{t:.2f}')