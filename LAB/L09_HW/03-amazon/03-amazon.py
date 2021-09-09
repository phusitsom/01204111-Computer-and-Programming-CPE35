import json
with open(input('file name: ')) as file:
    f = f"""[{file.read()}"""
    data = json.loads('\n'.join(map(lambda x: f'{x},',f.splitlines()))[:-1]+']')

_1 = len(data)

_2 = len(set(review['reviewerID'] for review in data))

_3 = len(set(review['productID'] for review in data))

_4 = len(set(review['category'].split('>')[0].strip() for review in data))

_5 = len(set(review['category'].split('>')[1] for review in data))

most_review = {}

for review in data:
    
    reviewerID = review['reviewerID']
    
    if reviewerID not in most_review:
        most_review.setdefault(reviewerID,0)
        
    most_review[reviewerID] += 1
    
_6 = max(most_review.items(), key= lambda x: x[1])[0]

prod_lentext, prod_rv = {}, {}

for review in data:
    
    productName = review['productName']
    len_reviewText = len(review['reviewText'].split())
    overall = review['overall']
    
    if productName not in prod_lentext:
        prod_lentext.setdefault(productName,[0,[]])
        
    if productName not in prod_rv:
        prod_rv.setdefault(productName,[0,[]])
        
    prod_rv[productName][1].append(overall)
    prod_rv[productName][0] += 1
    
    prod_lentext[productName][1].append(len_reviewText)
    prod_lentext[productName][0] += 1
    
prod_rv_avg = {k:(v[0], sum(v[1])/v[0])for k, v in prod_rv.items()}

max_score = max(prod_rv_avg.values(), key= lambda x: x[1])[1]

_7 = max([(product,v[0]) for product, v in prod_rv_avg.items() if v[1] == max_score], key= lambda x: x[1])[0]


prod_lentext_avg = {k:(v[0], sum(v[1])/v[0])for k, v in prod_lentext.items()}

max_score = max(prod_lentext_avg.values(), key= lambda x: x[1])[1]

_8 = max([(product,v[0]) for product, v in prod_lentext_avg.items() if v[1] == max_score], key= lambda x: x[1])[0]\
    
print([_1,_2,_3,_4,_5,_6,_7,_8][int(input('input: '))-1])