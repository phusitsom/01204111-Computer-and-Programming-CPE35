id_card = input()
check_digit = (11 - (13 * int(id_card[0]) + 12 * int(id_card[1]) + 11 * int(id_card[2]) + 10 * int(id_card[3]) + 9 * int(id_card[4]) + 8 * int(id_card[5]) + 7 * int(id_card[6]) + 6 * int(id_card[7]) + 5 * int(id_card[8]) + 4 * int(id_card[9]) + 3 * int(id_card[10]) + 2 * int(id_card[11])) % 11) % 10
print(id_card[0], id_card[1:5], id_card[5:10], id_card[10:12], check_digit)