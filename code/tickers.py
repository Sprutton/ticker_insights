import pandas as pd
import quandl as q
import os
from glob import glob

#quandl api key
q_key = ''
q.ApiConfig.api_key = q_key

path = '../data/ticker_data'

#create ticker list
ticker_df = pd.read_csv('../data/test_data/ticker_list.csv')
ticker_df['Ticker'] = ticker_df['Ticker'].str.replace('.','_')
symbols = ticker_df['Ticker'].tolist()

#add paramaters
max_price = 10.00
low_price = 1.00
start_date = '2020-01-01'
end_date = '2021-01-01'

#create place to store data if not already there
if not os.path.exists(path):
  os.mkdir(path)

#pull & store data
for symbol in symbols:
  data = q.get('EOD/' + symbol, start_date=start_date, end_date=end_date)
  if data.size>0:
    if data['High'].max() <= max_price and data['High'].max() >= low_price:
      if os.path.exists(f"{path}/{symbol}.csv"):
        os.system(f"rm {path}/{symbol}.csv")
        data.to_csv(f"{path}/{symbol}.csv")
        print(f"Replacing file for {symbol}")
      else:
        if not os.path.exists(f"{path}/{symbol}.csv"):
          data.to_csv(f"{path}/{symbol}.csv")
          print(f"Creating file for {symbol}")
    print(f'Price for {symbol} not in range.')
  else:
    print(f"No results for {symbol}")
