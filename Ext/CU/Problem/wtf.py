import numpy as np

def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:,1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
    return {'new_cases': new_cases, 
    'norm_data': norm,
    'province_names': d[1:,0],
    'dates': d[0,1:]}

data = read_data('ass.csv')

def max_new_cases_date(DATA):
    ind = np.argmax(np.sum(DATA['new_cases'], axis = 0))
    return DATA['dates'][ind], np.sum(DATA['new_cases'],axis = 0)[ind]

def max_new_cases_province(DATA, beg_date, end_date):
    ind_beg_date = np.where(DATA['dates'] == beg_date)[0][0]
    ind_end_date = np.where(DATA['dates'] == end_date)[0][0]

    caseByDate = DATA['new_cases'].take(indices = range(ind_beg_date, ind_end_date+1), axis = 1)

    ind = np.argmax(np.sum(caseByDate, axis = 1))
    return DATA['province_names'][ind], np.sum(caseByDate,axis = 1)[ind]

def max_new_cases_province_by_dates(DATA):
    arr = np.ndarray( (3,16), dtype=object)
    arr[0] = np.transpose(DATA['dates'])
    arr[1] = DATA['province_names'][np.argmax(DATA['new_cases'], axis = 0)]
    arr[2] = np.max(DATA['new_cases'], axis=0)
    return arr.transpose()

def most_similar(DATA, province):
    province_ind = np.where(DATA['province_names'] == province)[0][0]
    sim = list(np.sum((DATA['norm_data'][province_ind] - DATA['norm_data'])**2, axis = 1))
    return DATA['province_names'][np.argmin(sim[:province_ind] + sim[province_ind+1:])+1]

def most_similar_province_pair(DATA):
    prov = (np.add(DATA['province_names'].astype(object).reshape(-1,1), ' ') + DATA['province_names'].astype(object)).reshape(-1,1)

    a = np.sum(np.power(np.repeat(DATA['norm_data'], 77,axis = 0) - np.tile(DATA['norm_data'], (77,1)),2), axis=1)
    b = np.where(a==0,np.nan,a)

    np.where(b == np.nanmin(b))
    same_norm_diff_prov = np.mod(np.where(a==0),78)
    if np.sum(same_norm_diff_prov) != 0:

        ind = (np.take(np.where(a==0)[0],[np.where((np.mod(np.where(a==0),78) != 0))[1:]]))[0][0]
        np.put(b,[ind],np.take(a,[ind]))

    ans = str(np.random.choice(np.take(prov, np.where(b == np.nanmin(b)))[0])).split()

    return ans[0], ans[1]


def main():
    print(max_new_cases_date(data))
    print(max_new_cases_province(data, '2021-04-10', '2021-04-13'))
    print(max_new_cases_province_by_dates(data))
    print(most_similar(data,'กรุงเทพมหานคร'))
    print(most_similar_province_pair(data))
    return

main()