def read_csv(fn: str):
    with open(fn) as file:
        _items = list(map(lambda x: x.split(','),file.read().splitlines()))
        _keys = [item.pop(0) for item in _items[1:]]
        _val_key = _items.pop(0)[1:]
        _data = {}
        for _key, _item in zip(_keys,_items):
            
            if _key not in _data:
                _data.setdefault(_key,dict(zip(_val_key,[0 for i in range(len(_val_key))])))
            
            for _k, _v in zip(_val_key,tuple(map(int,_item))):
                _data[_key][_k] += _v
            
        return _data
    
    
data = read_csv(input('filename: '))

_1 = lambda : sum([int(i['Total Cases']) for i in data.values()])
_2 = lambda : max(data.items(), key= lambda x: x[1]['Deaths'])[0]
_3 = lambda : max(data.items(), key= lambda x: x[1]['Deaths']/x[1]['Total Cases'])[0]
_4 = lambda : max(data.items(), key= lambda x: x[1]['Discharged']/x[1]['Total Cases'])[0]

def _5():
    a = t = 0

    for v in data.values():
        a, t = a+v['Active'], t+ v['Total Cases']
        
    return f'{a*100/t:.2f}%'

def _6():
    avg_7_days = {}

    for item in tuple(data.items()):
        
        state = item[0]
        day_1_7 = tuple(item[1].values())[4:]
        
        if state not in avg_7_days:
            avg_7_days.setdefault(state,0)
            
        avg_7_days[state] = sum(day_1_7)/7


    pri_str_6 = []
    for state, avg in sorted(avg_7_days.items(), key= lambda x: x[1], reverse= True)[:5]:
        pri_str_6.append(f"{state} {avg:.0f}")
        
    return '\n'.join(pri_str_6)

def _7():
    red_states = []

    for item in tuple(data.items()):
        
        state = item[0]
        day_1_7 = tuple(item[1].values())[4:]
        
        tf = tuple(map(lambda x: x>100,day_1_7))
        
        
        for i in range(len(tf)-4):
            if all(tf[i:i+5]):
                red_states.append(state)
                break
    
    return sorted(red_states)

ty = int(input('type: '))
if ty == 7:
    [print(i) for i in _7()][0]
else:
    print([_1,_2,_3,_4,_5,_6][ty-1]())