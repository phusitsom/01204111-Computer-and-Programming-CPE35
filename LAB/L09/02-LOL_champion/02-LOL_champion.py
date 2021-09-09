import json

with open (input('Filename : ')) as file:
    data=json.loads(file.read())

case, character= int(input('Case : ')), input('Character : ').split(',')

if case == 1:
    for i in data.values():
        if str(i["name"][0]) in character:print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')
elif case == 2:
    for i in data.values():
        if str(i["title"].strip('the').strip('The').strip()[0]) in character:print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')
else:
    for i in data.values():
        if str(i["id"]) in character:print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')