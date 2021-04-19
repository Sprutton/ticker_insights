
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '../data/'

df = pd.read_csv(path+'sp500_closefull.csv', index_col='Date', parse_dates=True)

# drop any columns with more 10 or more missing values
df.dropna(axis=1, thresh=len(df) - 10, inplace=True)

# forward fill and backfill
df.fillna(method='ffill', inplace=True)
df.fillna(method='bfill', inplace=True)

all_dates = df.index.unique().sort_values()

start = all_dates.get_loc('2014-01-02')
end = all_dates.get_loc('2017-06-30')
dates = all_dates[start:end+1]

# empty dataframe
returns = pd.DataFrame(index=all_dates[1:])


for name in df.columns:
  current_returns = np.log(df[name]).diff()
  returns[name] = current_returns.iloc[1:]

X = returns.to_numpy()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

from sklearn.decomposition import PCA
model = PCA()
Z = model.fit_transform(X)


plt.plot(model.explained_variance_ratio_);
plt.plot(model.explained_variance_ratio_[:10]);

cmulative_variance = np.cumsum(model.explained_variance_ratio_)
plt.plot(cumulative_variance);

# Plot first principal component vs S&P
plt.plot(Z[:,0]);

Z_df = pd.DataFrame(index=returns.index)
Z_df['PC1'] = Z[:,0]

spy = pd.read_csv(path+'SPY.csv', index_col='Date', parse_dates=True)

spy_returns = -np.log(spy['Close']).diff().dropna()
spy_returns.plot();

joined = Z_df.join(spy_returns)

joined.columns = ['PC1', 'SPY']

scaler2 = StandardScaler()
joined[['PC1', 'SPY']] = scaler2.fit_transform(joined)

joined.plot(figsize=(10, 5), alpha=0.7);
