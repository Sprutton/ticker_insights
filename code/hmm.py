!pip install hmmlearn
from hmmlearn import hmm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

path = '../data/'

df = pd.read_csv(path+'SPY.csv', index_col='Date', parse_dates=True)

returns = np.log(df['Close']).diff()

returns.dropna(inplace=True)
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")
X = returns.to_numpy().reshape(-1, 1)
model.fit(X)

Z = model.predict(X)

fig, ax = plt.subplots(figsize=(10, 5))
plt.subplot(211)
plt.plot(Z)
plt.subplot(212)
plt.plot(returns);

# we want to draw different segments in different colors according to state
fig, ax = plt.subplots(figsize=(10, 5))

# first create arrays with nan
returns0 = np.empty(len(Z))
returns1 = np.empty(len(Z))
returns0[:] = np.nan
returns1[:] = np.nan

# fill in the values only if the state is the one corresponding to the array
returns0[Z == 0] = returns[Z == 0]
returns1[Z == 1] = returns[Z == 1]
plt.plot(returns0, label='state 0')
plt.plot(returns1, label='state 1')
plt.legend();

model.transmat_

model.transmat_ = np.array([
  [0.999, 0.001],
  [0.001, 0.999],                           
])

Z = model.predict(X)

fig, ax = plt.subplots(figsize=(10, 5))
plt.subplot(211)
plt.plot(Z)
plt.subplot(212)
plt.plot(returns);

# we want to draw different segments in different colors according to state
fig, ax = plt.subplots(figsize=(10, 5))

# first create arrays with nan
returns0 = np.empty(len(Z))
returns1 = np.empty(len(Z))
returns0[:] = np.nan
returns1[:] = np.nan

# fill in the values only if the state is the one corresponding to the array
returns0[Z == 0] = returns[Z == 0]
returns1[Z == 1] = returns[Z == 1]
plt.plot(returns0, label='state 0')
plt.plot(returns1, label='state 1')
plt.legend();
