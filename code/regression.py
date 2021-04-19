import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '../data/'

df = pd.read_csv(path+'sp500_closefull.csv', index_col=0, parse_dates=True)

df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=1, how='any', inplace=True)
df.isna().sum().sum()

df_returns = pd.DataFrame()

for name in df.columns:
  df_returns[name] = np.log(df[name]).diff()

df_returns['SPY'] = df_returns['SPY'].shift(-1)
Ntest = 1000
train = df_returns.iloc[1:-Ntest]
test = df_returns.iloc[-Ntest:-1]
x_cols = ['AAPL', 'MSFT', 'AMZN', 'JNJ', 'V', 'PG', 'JPM']
Xtrain = train[x_cols]
Ytrain = train['SPY']
Xtest = test[x_cols]
Ytest = test['SPY']


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(Xtrain, Ytrain)
model.score(Xtrain, Ytrain), model.score(Xtest, Ytest)

Ptrain = model.predict(Xtrain)
Ptest = model.predict(Xtest)
np.mean(np.sign(Ptrain) == np.sign(Ytrain)), np.mean(np.sign(Ptest) == np.sign(Ytest))

set(np.sign(Ptrain)), set(np.sign(Ptest))

df_returns['Position'] = 0 # create new column
df_returns.loc[1:-Ntest,'Position'] = (Ptrain > 0)
df_returns.loc[-Ntest:-1,'Position'] = (Ptest > 0)

df_returns['AlgoReturn'] = df_returns['Position'] * df_returns['SPY']

df_returns.iloc[1:-Ntest]['AlgoReturn'].sum()

# Total algo log return test
df_returns.iloc[-Ntest:-1]['AlgoReturn'].sum()

# Total return buy-and-hold test
Ytest.sum()

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=10)
Ctrain = (Ytrain > 0)
Ctest = (Ytest > 0)
model.fit(Xtrain, Ctrain)
model.score(Xtrain, Ctrain), model.score(Xtest, Ctest)

Ptrain = model.predict(Xtrain)
Ptest = model.predict(Xtest)
set(Ptrain), set(Ptest)

df_returns.loc[1:-Ntest,'Position'] = Ptrain
df_returns.loc[-Ntest:-1,'Position'] = Ptest
df_returns['AlgoReturn'] = df_returns['Position'] * df_returns['SPY']

# Total algo log return train
df_returns.iloc[1:-Ntest]['AlgoReturn'].sum()

# Total algo log return test
df_returns.iloc[-Ntest:-1]['AlgoReturn'].sum()

# Total return buy-and-hold
Ytrain.sum(), Ytest.sum()

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=2)
model.fit(Xtrain, Ctrain)
model.score(Xtrain, Ctrain), model.score(Xtest, Ctest)

Ptrain = model.predict(Xtrain)
Ptest = model.predict(Xtest)

df_returns.loc[1:-Ntest,'Position'] = Ptrain
df_returns.loc[-Ntest:-1,'Position'] = Ptest

df_returns['AlgoReturn'] = df_returns['Position'] * df_returns['SPY']

df_returns.iloc[1:-Ntest]['AlgoReturn'].sum()

# Total algo log return test
df_returns.iloc[-Ntest:-1]['AlgoReturn'].sum()

# Total return buy-and-hold
Ytrain.sum(), Ytest.sum()