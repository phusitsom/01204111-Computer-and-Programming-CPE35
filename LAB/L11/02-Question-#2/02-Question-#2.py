class City:
  nbCity = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1

with open(input('Enter file name: ')) as file:
    cities = [City(*row) for row in map(lambda x: x.split(','), file.read().splitlines()[1:])]
    
print(f'Minimum: {min(cities, key= lambda c: c.temperature).temperature:.2f}')    
print(f'Maximum: {max(cities, key= lambda c: c.temperature).temperature:.2f}')
print(f'Average temperature: {sum([city.temperature for city in cities])/len(cities):.4f}')
