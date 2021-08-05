dictionary = {"arm":["n", "แขน"], "hello": ["v","สวัสดี"], "beautiful":["adj","สวย"], "toilet" :["n", "ห้องน้ำ"], "kick":["v", "เตะ"], "handsome":["adj", "หล่อ"]}
def opt():
    optnum = int(input())
    if optnum == 1:print(dictionary[word][0])
    elif optnum == 2:print(dictionary[word][1])
    else: 
        print("Invalid option.")
        opt()
while True:
    word = input()
    if word == "0": break
    if word not in dictionary: 
        print("Word not in dictionary.")
        pass
    else: opt()