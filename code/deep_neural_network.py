import pandas as pd
import numpy as np
import hvplot.pandas

from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import numpy as np
import hvplot.pandas
from pylab import mpl, plt
from scipy.optimize import minimize
plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'
np.set_printoptions(precision=5, suppress=True,
                   formatter={'float': lambda x: f'{x:6.3f}'})
import matplotlib.pyplot as plt
from pathlib import Path
from pylab import mpl, plt
import datetime
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam, RMSprop
import random


path = '../data/'

djia = pd.read_csv(path+'djia_.csv')
djia

djia.dropna(axis=0, how='all', inplace=True)
djia.dropna(axis=1, how='any', inplace=True)
djia.isna().sum().sum()

djia.set_index('Date', inplace=True)

djia.info()

djia_close = djia[['Close']].copy()

djia_close.rename(columns={'Close' : 'price'}, inplace=True)


djia_close['return'] = np.log(djia_close[['price']] / 
                            djia_close[['price']].shift(1))

djia_close['direction'] = np.where(djia_close['return']> 0, 1, 0)

lags = 5

cols = []

for lag in range(1, lags + 1):
    col = f'lag_{lag}'
    djia_close[col] = djia_close['return'].shift(lag)
    cols.append(col)
djia_close.dropna(inplace=True)

djia_close.round(4).tail()

optimizer = Adam(learning_rate=0.0001)

def set_seeds(seed=100):
    random.seed(seed)
    np.random.seed(seed)
    tf.set_random_seed(100)

set_seeds()
model = Sequential()
model.add(Dense(64, activation='relu',
               input_shape=(lags,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer=optimizer,
             loss='binary_crossentropy',
             metrics=['accuracy'])

cutoff = '2017-10-31'

training_data = djia_close[djia_close.index < cutoff].copy()

mu, std = training_data.mean(), training_data.std()

training_data_ = (training_data - mu) / std

test_data = djia_close[djia_close.index >= cutoff].copy()

test_data_ = (test_data - mu) / std

model.fit(training_data[cols],
          training_data['direction'],
          epochs=300, verbose=False,
          validation_split=0.2, shuffle=False)


res = pd.DataFrame(model.history.history)

res

res[['accuracy', 'val_accuracy']].hvplot(width=925, height=510, grid=True, line_width= 2.5, hover_line_color='gold')

model.evaluate(training_data_[cols], training_data['direction'])

pred = np.where(model.predict(training_data_[cols]) > 0.5, 1, 0)

pred[:30].flatten()

training_data['prediction'] = np.where(pred > 0, 1, -1)

training_data['strategy'] = (training_data['prediction'] * 
                            training_data['return'])

training_data[['return', 'strategy']].sum().apply(np.exp)

train_ret_stra =  training_data[['return', 'strategy']]
train_ret_stra

train_ret_stra.cumsum().apply(np.exp).hvplot.line(width=925, height=510, grid = True, line_width= 2.5, hover_line_color='gold')

model.evaluate(test_data_[cols], test_data['direction'])

pred = np.where(model.predict(test_data_[cols]) > 0.5, 1, 0 )

test_data['prediction'] = np.where(pred > 0, 1, -1)

test_data['prediction'] = np.where(pred > 0, 1, -1)

test_data['prediction'].value_counts()

test_data['strategy'] = (test_data['prediction'] * 
                        test_data['return'])

test_data[['return', 'strategy']].sum().apply(np.exp)

test_data[['return', 'strategy']].cumsum().apply(np.exp).hvplot(width=1000, height=500,line_width= 2.5, hover_line_color='gold', rot=90,xlabel="Date",xaxis=None)

# Adding Different Types of Fetures 
djia_close['momentum'] = djia_close['return'].rolling(5).mean().shift(1)

djia_close['volatility'] = djia_close['return'].rolling(20).std().shift(1)

djia_close['distance'] = (djia_close['price'] - 
                          djia_close['price'].rolling(50).mean()).shift(1)

djia_close.dropna(inplace=True)

cols.extend(['momentum', 'volatility', 'distance'])

print(djia_close.round(4).tail())

training_data_new = djia_close[djia_close.index < cutoff].copy()

mu, std = training_data_new.mean(), training_data_new.std()

new_training_data_ = (training_data_new - mu) / std

test_data = djia_close[djia_close.index >= cutoff].copy()

test_data_ = (test_data - mu) / std

set_seeds()
model = Sequential()
model.add(Dense(32, activation='relu',
                input_shape=(len(cols),)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer=optimizer,
             loss='binary_crossentropy',
             metrics=['accuracy'])

model.fit(new_training_data_[cols], training_data_new['direction'],
          verbose=False, epochs=25)

model.evaluate(new_training_data_[cols], training_data_new['direction'])

pred = np.where(model.predict(new_training_data_[cols]) > 0.5, 1, 0)

training_data_new['prediction'] = np.where(pred > 0, 1, -1)

training_data_new['strategy'] = (training_data_new['prediction'] *
                             training_data_new['return'])
                             
training_data_new[['return', 'strategy']].sum().apply(np.exp)

training_data_new[['return', 'strategy']].cumsum().apply(np.exp).hvplot( width=1000, height=700,line_width= 2.5, hover_line_color='gold', rot=90,xaxis=None)

training_data_new[['return', 'strategy']].cumsum().apply(np.exp).hvplot( width=925, height=510,line_width= 2.5, hover_line_color='gold')

model.evaluate(test_data_[cols], test_data_['direction'])

pred = np.where(model.predict(test_data_[cols]) > 0.5, 1 , 0)

test_data['prediction'] = np.where(pred > 0, 1, -1)

test_data['prediction'].value_counts()

test_data['strategy'] = (test_data['prediction'] * 
                        test_data['return'])



test_data[['return', 'strategy']].sum().apply(np.exp)

test_data[['return', 'strategy']].cumsum().apply(np.exp).hvplot(width=925, height=510,line_width= 2.5, hover_line_color='gold', xaxis=None)

