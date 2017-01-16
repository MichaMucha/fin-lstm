import pandas as pd
from pandas_datareader import data, wb
import re
import datetime

GoogleDomesticTrends = '''
    - GOOGLEINDEX_US:ADVERT
    This Google Advertising & Marketing Index tracks searches related to (marketing, advertising, commercials...)
    - GOOGLEINDEX_US:AIRTVL
    This Google Air Travel Index tracks searches related to (airlines, airline, flights...)
    - GOOGLEINDEX_US:AUTOBY
    This Google Auto Buyers Index tracks searches related to (car, blue book...)
    - GOOGLEINDEX_US:AUTOFI
    This Google Auto Financing Index tracks searches related to (loan, car lean...)
    - GOOGLEINDEX_US:AUTO
    This Google Automotive Index tracks searches related to (car, honda, toyota...)
    - GOOGLEINDEX_US:BIZIND
    The Google Business and Industrial Index tracks queries related to "ups, new, water, usps, paypal, staples, dow, mypay" and so forth.
    - GOOGLEINDEX_US:BNKRPT
    The Google Bankruptcy Index tracks queries related to "bankruptcy, chapter 7, chapter 11, garnish wages" and so forth.
    - GOOGLEINDEX_US:COMLND
    The Google Commercial Lending Index tracks queries related to "business credit, business loans, business credit cards, ge capital"
    - GOOGLEINDEX_US:COMPUT
    This Google Computers & Electronics Index tracks searches related to (windows, download, microsoft...)
    - GOOGLEINDEX_US:CONSTR
    This Google Construction Index tracks searches related to (doors, construction...)
    - GOOGLEINDEX_US:CRCARD
    The Google Credit Cards Index tracks queries related to "chase, card, credit card, capital one, american express" and so forth.
    - GOOGLEINDEX_US:DURBLE
    This Google Durable Goods Index tracks searches related to (vacuum, appliances, refrigerator...)
    - GOOGLEINDEX_US:EDUCAT
    The Google Education Index tracks queries related to "college, education, test, academy, barnes and noble, harvard" and so forth
    - GOOGLEINDEX_US:FURNTR
    This Google Furniture Index tracks searches related to (ikea, furniture, table...)
    - GOOGLEINDEX_US:INVEST
    The Google Investing Index tracks queries related to "stock, gold, fidelity, oil, stock market, scottrade" and so forth.
    - GOOGLEINDEX_US:FINPLN
    The Google Financial Planning Index tracks queries related to "schwab, 401k, ira, smith barney, fidelity, roth 401k"
    - GOOGLEINDEX_US:INSUR
    The Google Insurance Index tracks queries related to "insurance, health insurance, life insurance, blue cross, state farm, geico"
    - GOOGLEINDEX_US:JOBS
    This Google Jobs Index tracks searches related to (city, jobs, resume, monster...)
    - GOOGLEINDEX_US:LUXURY
    This Google Luxuries Index tracks searches related to (diamond, jewelers, rings, tiffany...)
    - GOOGLEINDEX_US:MOBILE
    The Google Mobile & Wireless Index tracks queries related to "iphone, verizon, blackberry, phone, samsung, apps" and so forth
    - GOOGLEINDEX_US:MTGE
    This Google Mortgage Index tracks searches related to (mortgage calculator, mortage rates, mortgage...)
    - GOOGLEINDEX_US:RLEST
    This Google Real Estate Index tracks searches related to (mortgage,apartmenents, real estate, rent...)
    - GOOGLEINDEX_US:RENTAL
    This Google Rental Index tracks searches related to (for rent, rent, rentals...)
    - GOOGLEINDEX_US:SHOP
    The Google Shopping Index tracks queries related to "ebay, walmart, shoes, amazon, coupons, ipod" and so forth
    - GOOGLEINDEX_US:SMALLBIZ
    The Google Small Business Index tracks queries related to "small business, make money, franchise, work from home, chamber or commerce" and so forth.
    - GOOGLEINDEX_US:TRAVEL
    This Google Travel Index tracks searches related to (hotel, vegas, airlines...)
    - GOOGLEINDEX_US:UNEMPL
    This Google Unemployment Index tracks searches related to (social security, unemployment...)
    '''

trend_ticknames = re.findall(r'[A-Z_:]{14,}', GoogleDomesticTrends)

start = datetime.datetime(2004, 1, 1)
half = datetime.datetime(2010, 12, 31)
half_ = datetime.datetime(2011, 1, 1)

gt1 = data.get_data_google(trend_ticknames, start, half)
gt2 = data.get_data_google(trend_ticknames, half_)

googletrends_df = gt1['Close'].append(gt2['Close'])
googletrends_df.to_excel('GoogleDomesticTrends.xlsx')
