import pandas as pd

f = pd.read_csv('C:/Users/LENOVO\Documents/GitHub/KU_Exercises/Pretest/amazon-orders.csv', header = 3)
f.to_csv(r'amazon-orders.csv',index = None)

df = pd.read_csv('amazon-orders.csv')

def remove_dollar(series):
    series = series.replace({r'\$':''}, regex = True).astype('float')
    return series

df_chargedday = df[['Order Date', 'Total Charged']]
df_chargedday['Total Charged'] = remove_dollar(df_chargedday['Total Charged'])

df_gb_chargedday = df_chargedday.groupby('Order Date').sum()

df_promoday = df[['Order Date', 'Total Promotions']]
df_promoday['Total Promotions'] = remove_dollar(df_promoday['Total Promotions'])

df_gb_promoday = df_promoday.groupby('Order Date').sum()
max_promodate = df_gb_promoday.loc[(df_gb_promoday['Total Promotions'] == df_gb_promoday['Total Promotions'].max())].reset_index()

print('Payment per day\n', df_gb_chargedday.reset_index())
print('Most total promotion you got is on', max_promodate['Order Date'][0], '({})'.format(int(max_promodate['Total Promotions'][0])))