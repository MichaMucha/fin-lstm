import pandas as pd
from pandas_datareader import data, wb
import re
import datetime

tickers = ['USDGBP',
 'MSFT',
 'AAL',
 'APA',
 'CPB',
 'MMM',
 'SWN',
 'HTLD',
 'NUAN',
 'PF',
 'LUX',
 'TETHF',
 'FALC',
 'BDE',
 'AKAO',
 'PATI']

sectors = ['currency',
 'technology',
 'transportation',
 'energy',
 'nondurables',
 'health',
 'energy',
 'transportation',
 'technology',
 'nondurables',
 'health',
 'energy',
 'technology',
 'nondurables',
 'health',
 'transportation']

company_sector_data = pd.DataFrame({'tickers' : tickers,
                                    'sectors' : sectors})
start = datetime.datetime(2004, 1, 1)
cd = data.get_data_google(tickers, start)

path = '/Users/michalmucha/Documents/ML_modules/Fin_LSTM_data/CompanyDataPanel.pickle'
cd.to_pickle(path)

pd.read_pickle(path)['Close']
