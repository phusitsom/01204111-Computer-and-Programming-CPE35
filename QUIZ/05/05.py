import json

with open(input('Filename : ')) as file:
    data = json.load(file)

for i, anime in enumerate(data):
    data[i]['index'] = i
    for k, v in anime.items():
        if v is None:
            data[i][k] = 0
_1 = lambda: print(len(data))


def _2():
    ind_st, ind_en, inp = [input(f'{_text} : ') for _text in ('From', 'To', 'Start with Char')]
    
    
    _print_list = [f"{anime['index']} : {anime['title']}" for anime in data[int(ind_st):int(ind_en)+1] if anime['title'].upper().startswith(inp)]
    for text in _print_list: 
        print(text)
        
def _3():
    ind_st, ind_en, inp = [input(f'{_text} : ') for _text in ('From', 'To', 'Type')]
    
    _anime_list = [anime for anime in data[int(ind_st):int(ind_en)+1] if anime['type'] == inp]
    
    _print_list = [f"{inp} : {len(_anime_list)}"]
    _print_list.append(f"Most scores : {max(_anime_list, key = lambda anime : anime['mal_score'])['title']}")
    _print_list.append(f"Most favorites : {max(_anime_list, key = lambda anime : anime['mal_favorites'])['title']}")
    
    for text in _print_list: 
        print(text)
        
def _4():
    ind_st, ind_en, inp_source, inp_status, inp_score = [input(f'{_text} : ') for _text in ('From', 'To', 'Source','Status','Mul score')]
    
    _print_list = [f"{anime['index']} : {anime['title']}" for anime in data[int(ind_st):int(ind_en)+1] if all((anime['source'] == inp_source, anime['status'] == inp_status, anime['mal_score'] >= float(inp_score)))]
    
    for text in _print_list: 
        print(text)
        
def _5():
   ind_st, ind_en, inp_season = [input(f'{_text} : ') for _text in ('From', 'To', 'Season')]

   _anime_list = [anime for anime in data[int(ind_st):int(ind_en)+1] if str(anime['premiered']).split()[0] == inp_season]

   print(f"{inp_season} : {len(_anime_list)}")
   
def _6():
   ind_st, ind_en, = [input(f'{_text} : ') for _text in ('From', 'To')]

   _anime_list = [anime for anime in data[int(ind_st):int(ind_en)+1] if str(anime['aired_start']).split('-')[0] == str(anime['aired_end']).split('-')[0]]

   print(f"Find : {len(_anime_list)}")
   
def _7():
    
    inp_title = input(f'Title : ')
    
    for anime in data:
        if anime['title'] == inp_title:
            print(anime['mal_rating'])
            break
        
def _8():
    ind_st, ind_en, = [input(f'{_text} : ') for _text in ('From', 'To')]
    
    max_syp_anime  = max(data[int(ind_st):int(ind_en)+1], key = lambda anime: len(anime['synopsis'].split()))
    print(f"{max_syp_anime['index']} : {max_syp_anime['title']}")
    
[None,_1,_2,_3,_4,_5,_6,_7,_8][int(input('Menu : '))]()