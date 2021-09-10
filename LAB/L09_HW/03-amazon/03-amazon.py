import json
with open(input('file name: ')) as file:
    f = f"""[{file.read()}"""
    data = json.loads(
        '\n'.join(map(lambda x: f'{x},', f.splitlines()))[:-1]+']')

_1 = lambda: len(data)
_2 = lambda: len(set(review['reviewerID'] for review in data))
_3 = lambda: len(set(review['productID'] for review in data))
_4 = lambda: len(set(review['category'].split('>')[0].strip() for review in data))
_5 = lambda: len(set(review['category'].split('>')[1] for review in data))

def _6():
    
    most_review = {}

    for review in data:

        reviewerID = review['reviewerID']

        if reviewerID not in most_review:
            most_review.setdefault(reviewerID, 0)

        most_review[reviewerID] += 1

    return max(most_review.items(), key=lambda x: x[1])[0]

def _gb_max(__ch:int):

    _dc = {}
    for review in data:
        _prod_name = review['productName']
        
        if __ch == 7:
            _val = review['overall']
        elif __ch == 8:
            _val = len(review['reviewText'].split())
        

        if _prod_name not in _dc:
            _dc.setdefault(_prod_name, [])

        _dc[_prod_name].append(_val)
        
    _dc_avg = {_k:(len(_v), sum(_v)/len(_v)) for _k, _v in _dc.items()}
    _max_val = max((_v[1] for _v in _dc_avg.values()))

    return max([(_k,_v[0]) for _k,_v in _dc_avg.items() if _v[1] == _max_val], key= lambda _x: _x[1])[0]

_7 = lambda: _gb_max(7)
_8 = lambda: _gb_max(8)

print([_1, _2, _3, _4, _5, _6, _7, _8][int(input('input: '))-1]())