flight_data, booking_data, funclist = {}, {}, [lambda:(lambda x: flight_data.update({x[0]:dict(list(zip(['start', 'destination', 'seat_unav', 'seat_max'], x[1:])))}))((lambda y: ([y.split()[i] for i in [0, 1, 3, 4, 6]]))(input("Add data : "))), lambda:(lambda x: print(f"""{x} is from {flight_data[x]["start"]} to {flight_data[x]["destination"]}, number of people booking is {flight_data[x]["seat_unav"]}/{flight_data[x]["seat_max"]}"""))(input("Enter code : ")), lambda:([print("All flight data"), [(lambda x: print(f"""{x} is from {flight_data[x]["start"]} to {flight_data[x]["destination"]}, number of people booking is {flight_data[x]["seat_unav"]}/{flight_data[x]["seat_max"]}"""))(id) for id in flight_data][0]][0]), lambda:(
    (lambda fdata: [(lambda: None), (lambda: [flight_data[fdata[1]].update({"seat_unav": int(flight_data[fdata[1]]["seat_unav"])+1}), booking_data.update({fdata[0]:[fdata[1]]}) if fdata[0] not in booking_data else booking_data.update({fdata[0]:booking_data[fdata[0]]+[fdata[1]]})][0])][fdata[2]]())((lambda name, id: (name, id, print("Success") is None) if int(flight_data[id]['seat_unav']) != int(flight_data[id]['seat_max']) else (name, id, '1' == print("The flight is full, Sorry")))(input("Enter your name : "), input("Enter flight code : ")))), lambda:(lambda name: print(f"""{name} is booking flight code = {' '.join(sorted(list(set(booking_data[name])))[::-1])}"""))(input("Enter your name : "))]
print("Select menu :\n1. add flight data\n2. flight data by code\n3. show all flight data\n4. flight booking\n5. show people flight data\n6. exit")
while True:
    opt = int(input("menu : "))
    if opt == 6:
        print("EXIT!!!!!!!!!!!!!!!")
        break
    else:
        funclist[opt-1]()
