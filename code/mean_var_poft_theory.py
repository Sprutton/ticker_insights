import hvplot.pandas

import pandas as pd
import numpy as np
from pylab import mpl, plt
from scipy.optimize import minimize
plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'
np.set_printoptions(precision=5, suppress=True,
                   formatter={'float': lambda x: f'{x:6.3f}'})

import datetime

import statsmodels.api as sm
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

path = '../data/'
raw = pd.read_csv(path+'sp500_closefull.csv', index_col='Date', parse_dates=True)

symbols = ['CSCO', 'ISRG', 'TROW', 'BA', 'VRTX', 'M', 'CRM','BLK']
symbols

rets = np.log(raw[symbols] / raw[symbols].shift(1)).dropna()

rets.hvplot(groupby=['index.year', 'index.month'], widget_type='scrubber', widget_location='bottom',width=925, height=510, grid=True, line_width= 2.5, hover_line_color='gold')

(raw[symbols] / raw[symbols].iloc[0]).hvplot(width=925, height=510, grid=True, line_width= 2.5, hover_line_color='gold',ylim=(0, 8.7))

raw[symbols].hvplot(width=925, height=510, grid=True, line_width= 2.5, hover_line_color='gold',ylim=(10, 600))

weights = len(rets.columns) * [1 / len(rets.columns)]


def port_return(rets, weights):
    return np.dot(rets.mean(), weights) * 252

port_return(rets, weights)

def port_volatility(rets, weights):
    return np.dot(weights, np.dot(rets.cov() * 252, weights)) ** 0.5

port_volatility(rets, weights)

def port_sharpe(rets, weights):
    return port_return(rets, weights) / port_volatility(rets, weights)

port_sharpe(rets, weights)

w = np.random.random((1000, len(symbols)))

w = (w.T / w.sum(axis=1)).T

w[:5]

pvr = [(port_volatility(rets[symbols], weights), 
       port_return(rets[symbols], weights))
      for weights in w]
pvr = np.array(pvr)

psr = pvr[:, 1] / pvr[:, 0]

plt.figure(figsize=(10, 6))
fig = plt.scatter(pvr[:, 0], pvr[:, 1],
                 c=psr, cmap='coolwarm')
cb = plt.colorbar(fig)
cb.set_label('Sharpe ratio')
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.title(' | '.join(symbols))

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
 
# Creating dataset
z = pvr[:, 0]
x = pvr[:, 1]
y = psr
 
# Creating figure
fig = plt.figure(figsize = (25, 11))
ax = plt.axes(projection ="3d")
   
# Add x, y gridlines
ax.grid(b = True, color ='black',
        linestyle ='--', linewidth = 0.3,
        alpha = 0.8)
 
 
# Creating color map
my_cmap = plt.get_cmap('coolwarm')
 
# Creating plot
sctt = ax.scatter3D(x, y, z,
                    alpha = 1,
                    c = (x + y + z),
                    cmap = my_cmap,
                    marker ='*')
 
plt.title(' | '.join(symbols))
ax.set_xlabel('expected volatility', fontweight ='bold')
ax.set_ylabel('expected return', fontweight ='bold')
ax.set_zlabel('Sharpe ratio', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
 
# show plot
plt.show()

bnds = len(symbols) * [(0, 1),]
bnds

cons = {'type' : 'eq', 'fun' : lambda weights: weights.sum() - 1}

opt_weights = {}
for year in range(2010, 2018):
    rets_ = rets[symbols].loc[f'{year}-01-10':f'{year}-12-28']
    ow = minimize(lambda weights: -port_sharpe(rets_, weights),
                 len(symbols) * [1 / len(symbols)],
                 bounds=bnds,
                 constraints=cons)['x']
    opt_weights[year] = ow

opt_weights

res = pd.DataFrame()
for year in range(2010, 2018):
    rets_ = rets[symbols].loc[f'{year}-01-01':f'{year}-12-28']
    epv = port_volatility(rets_, opt_weights[year])
    epr = port_return(rets_, opt_weights[year])
    esr = epr / epv
    rets_ = rets[symbols].loc[f'{year + 1}-01-01':f'{year + 1}-12-28']
    rpv = port_volatility(rets_, opt_weights[year])
    rpr = port_return(rets_, opt_weights[year])
    rsr = rpr / rpv
    res = res.append(pd.DataFrame({'epv' : epv, 'epr' : epr, 'esr' : esr,
                                   'rpv' : rpv, 'rpr' : rpr, 'rsr' : rsr},
                                  index=[year + 1]))

res.mean()

res[['epv', 'rpv']].corr()

res[['epv', 'rpv']].hvplot.bar(width=925, height=510,fontscale=1.7, grid=True, hover_fill_color='gold',
                        title = 'Expected vs. Realized Portfolio Volatility')

res[['epr', 'rpr']].corr()

res[['epr', 'rpr']].hvplot.bar(width=925, height=510,fontscale=1.7, grid=True, hover_fill_color='gold',
                        title = 'Expected vs. Realized Portfolio Returns')

res[['esr', 'rsr']].corr()

res[['esr', 'rsr']].hvplot.bar(width=925, height=510,fontscale=1.7, grid=True, hover_fill_color='gold',
                        title = 'Expected vs. Realized Sharpe Ratios')

heat = res.corr()

f, ax = plt.subplots(figsize=(21, 14))
sns.heatmap(heat, annot=True, linewidths=1, ax=ax, robust=False, linecolor='silver',
)