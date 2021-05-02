# imports necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from pylab import mpl, plt
import datetime
import hvplot.pandas

# creating variable for file path

path = '../data/'

# using pandas to import csv file

spy_df = pd.read_csv(path+'SPY.csv')

spy_df.tail(5)

# drops na values along both axis, sums total na values.

spy_df.dropna(axis=0, how='all', inplace=True)
spy_df.dropna(axis=1, how='any', inplace=True)
spy_df.isna().sum().sum()

# sets Date to index column 

spy_df.set_index('Date', inplace=True)

# creates a copy of the spy DataFrames close column 

eod_df = spy_df[['Close']].copy()

eod_df.index

# changes the column name from close to price indcating cost involved if position entered. 

eod_df.rename(columns={'Close' : 'price'}, inplace=True)

# creating the 'SMA_fast' column a 20 week simple moving average

eod_df['SMA_fast'] = eod_df['price'].rolling(20).mean()

# creating the 'SMA_slow' column a 200 week simple moving average

eod_df['SMA_slow'] = eod_df['price'].rolling(200).mean()

# visualization of the original time series data in combination wiht the SMAs

plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'
eod_df.plot(title='SPY | 20 & 200 days SMAs', figsize=(20,10))

# Implements trading rules in vectorized fashion 

eod_df['position'] = np.where(eod_df['SMA_fast'] > eod_df['SMA_slow'],                             
                              1, -1)

# deletes all rows that contain na values 
eod_df.dropna(inplace=True)

# plots positioning over time

eod_df['position'].plot(ylim=[-1.1, 1.1],
                       title="Market Positioning",
                       figsize=(15,7))

# calculates log returns over the price column


eod_df['returns'] = np.log(eod_df['price'] / eod_df['price'].shift(1))

# plots log returns as histogram 
eod_df['returns'].hvplot.hist(bins=25, width=925, height=510, color="orangered", title='Distribution of Log Returns', xlabel='Distribution of returns')

# procures the returns for the strategy given positioning and market retuns

eod_df['strategy'] = eod_df['position'].shift(1) * eod_df['returns']

# computes single log return values for both the ticker and the strategy

eod_df[['returns', 'strategy']].sum()

# applies the exponential funtion to sum of log returns to produce the 'gross performance'  

eod_df[['returns', 'strategy']].sum().apply(np.exp)

# plots 'gross performance' of SPY ticker to the SMA strategy

eod_df[['returns', 'strategy']].cumsum().apply(np.exp).plot(figsize=(15,7), title='Gross performance of SPY compared to the SMA-based strategy')

# calculates annualized mean return in both log and regular space


np.exp(eod_df[['returns', 'strategy']].mean() * 252) -1

# calculate annualized std in both log and regular space


(eod_df[['returns', 'strategy']].apply(np.exp) - 1).std() * 252 ** 0.5

# initiates new column for the gorss performance over time

eod_df['cumret'] = eod_df['strategy'].cumsum().apply(np.exp) 

# initiates new column for the running maximum value of the gorss performance 

eod_df['cummax'] = eod_df['cumret'].cummax()

'''
plots newly created columns 

Gross performance and cumulative maximum performance of SMA strategy

'''

eod_df[['cumret', 'cummax']].dropna().plot(figsize=(15,7), title='Gross performance and cumulative maximum performance of SMA strategy')

# calculates the element-wise difference between the two columns and picks out maximum value 

drawdown = eod_df['cummax'] - eod_df['cumret']

drawdown.max()




