import pandas as pd
from glob import glob
#add all tickers to dataframe
files = glob(f'{path}/*.csv')
full_df = None

for f in files:
  print(f)
  df = pd.read_csv(f)
  symbol = f.split('../data/ticker_data/')[1].split('.')[0]
  df['Name'] = symbol
  if full_df is None:
    full_df = df
  else:
    full_df = full_df.append(df, ignore_index = True)

if not os.path.exists('../data/ticker_df.csv'):
  full_df.to_csv('../data/ticker_df.csv', index=False)
else:
  os.system(f'rm ../data/ticker_df.csv')
  full_df.to_csv('../data/ticker_df.csv', index=False)

#extract and join closing columns
tickers = pd.read_csv('../data/ticker_df.csv')
dates = pd.date_range(tickers['Date'].min(), tickers['Date'].max())
close_prices = pd.DataFrame(index=dates)
symbols2 = tickers['Name'].unique()

for symbol in symbols2:
  df_sym = tickers[tickers['Name'] == symbol]
  df_tmp = pd.DataFrame(data=df_sym['Close'].to_numpy(), \
                        index=df_sym['Date'], columns=[symbol])
  close_prices = close_prices.join(df_tmp, how='outer')

#clear na rows and columns
close_prices.dropna(axis=0, how='all', inplace = True)
close_prices.dropna(axis=1, how='all', inplace = True)

#save closing data
if not os.path.exists('../data/close_prices.csv'):
  close_prices.to_csv('../data/close_prices.csv')
else:
  os.system(f'rm ../data/ticker_df.csv')
  close_prices.to_csv('../data/close_prices.csv')
