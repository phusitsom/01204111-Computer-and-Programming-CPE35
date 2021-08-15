class JongTao:
    
    def __init__(self):
        self.flightdata = {}
        self.bookingdata = {}
        
    def addFlightData(self) -> None:
        inpsplit = input("Add data :").split()
        self.flightdata.update({inpsplit[0]:dict(zip(['id','start','end','pas_remain','pas_max'], [inpsplit[i] for i in [0,1,3,4,6]]))})
        
    def showFlightData(self) -> None:
        
        flight = self.flightdata[input("Enter code : ")]
        print(f"{flight['id']} is from {flight['start']} to {flight['end']},\
                number of people booking is {flight['pas_remain']}/{flight['pas_max']}")
        
    def showAllFlightData(self) -> None:
        print("All flight data")
        for id in self.flightdata:
            flight = self.flightdata[id]
            print(f"{flight['id']} is from {flight['start']} to {flight['end']},\
                    number of people booking is {flight['pas_remain']}/{flight['pas_max']}")
            
    def addBookingData(self):
        name = input('Enter your name : ')
        flight_id = input('Enter flight code : ')
        flight = self.flightdata[flight_id]
        if flight['pas_remain'] == flight['pas_max']:
            print("The flight is full, Sorry")
        else:
            self.bookingdata.update({name:{'name':name,'flight_id':[flight[id]]}})
            self.flightdata[flight_id].update(flight['pas_remain']+1)
            print("Success")

    def showBookingData(self):
        name = input('Enter your name : ')
        pas_data = self.bookingdata['name']
        print(f"{name} is booking flight code = {' '.join(pas_data['flight_id'])}")
    