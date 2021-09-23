class City:
  nbCity = 0
  def __init__(s,city,country,lat,long,temp):
    s.city = city; s.country = country; s.lat = lat
    s.long = long; s.temp = temp; City.nbCity += 1
class Country:
  nbCountry = 0
  def __init__(self,*args):
    self.country,self.population,self.EU,self.coastline = args
    Country.nbCountry+=1

def readCity():
  myCity = []
  with open('Cities.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity

def readCountry():
  myCountry = [Country(*row) for row in map(lambda x: x.split(','), open('Countries.csv').read().splitlines()[1:])]
  return myCountry

def q01(myCity, myCountry):
  _countries = [country.country for country in myCountry if all((country.EU=='yes',country.coastline=='no'))]
  _cities = [city for city in myCity if city.country in _countries]
  _country_temp = {}
  
  for city in _cities:
    _country_temp.setdefault(city.country, [])
    _country_temp[city.country].append(city.temp)
    
  for country, temps in _country_temp.items():
    print(f"{country}: {sum(temps)/len(temps):.2f}")

def q02(myCity, myCountry):
  _countries = [country.country for country in myCountry if country.EU=='no']
  _cities = [city for city in myCity if city.country in _countries]
  _country_temp = {}
  for city in _cities:
    _country_temp.setdefault(city.country, [])
    _country_temp[city.country].append(city.temp)
    
  for country, temps in _country_temp.items():
    _country_temp[country] = sum(temps)/len(temps)
   
  max_avg_temp = max(_country_temp.items(),key= lambda c: c[1])
  min_avg_temp = min(_country_temp.items(),key= lambda c: c[1])
  print(f"The highest average city temperature: {max_avg_temp[0]} ({max_avg_temp[1]:.2f})")
  print(f"The lowest average city temperature: {min_avg_temp[0]} ({min_avg_temp[1]:.2f})")

### main begins here
myCity = readCity()
myCountry = readCountry()