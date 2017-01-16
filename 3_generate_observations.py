import pandas as pd
import numpy as np
import re
import datetime
import os

pth = os.path.join('~', 'Documents', 'ML_modules', 'Fin_LSTM_data')
c_path = os.path.join(pth, 'CompanyDataPanel.pickle')
t_path = os.path.join(pth, 'GoogleDomesticTrends.xlsx')
company_data = pd.read_pickle(c_path)
company_data = company_data.drop(['USDGBP', 'TETHF'], axis=2)
trends_data = pd.read_excel(t_path, index_col=0)

company_data.minor_axis
sectorkeys = ['transportation', 'health', 'energy', 'nondurables',
    'nondurables', 'technology', 'transportation', 'health', 'health',
    'technology', 'technology', 'transportation', 'nondurables', 'energy']
sector_dict = {idx : sec for idx, sec in zip(company_data.minor_axis, sectorkeys)}

observations = pd.DataFrame()
for IDX in company_data.minor_axis:
    o = company_data[:,:,IDX]
    o['r'] = o.Close.pct_change().apply(lambda l: np.log(abs(l) + 1))
    u = np.log(o.High / o.Open)
    d = np.log(o.Low / o.Open)
    c = np.log(o.Close / o.Open)
    o['sig^2'] = 0.511*np.square(u-d)-0.019*(c*(u+d)-2*u*d)-.383*np.square(c)
    o['lag_sig^2'] = o['sig^2'].shift(1)
    o['sector'] = sector_dict[IDX]
    o = trends_data.merge(o, how='inner', left_index=True, right_index=True)
    observations = observations.append(o)
observations.columns = [cn.replace('GOOGLEINDEX_US:', '') for cn in observations.columns]
len (observations)
observations['o_id'] = range(len(observations))
sector_onehot = pd.get_dummies(observations['sector'])
sector_onehot['o_id'] = range(len(observations))
observations = observations.merge(sector_onehot, how='inner', on='o_id').drop('sector', axis=1)

with pd.HDFStore(os.path.join(pth, 'observations.h5')) as store:
    store['o'] = observations

observations.to_excel(os.path.join(pth, 'observations.xlsx'))

# Count valid observations per IDX
for IDX in company_data.minor_axis:
    fl = len(company_data[:,:,IDX].Close)
    vl = len(company_data[:,:,IDX].Close.dropna())
    print(IDX, 'nans', fl-vl, 'valid', vl)
