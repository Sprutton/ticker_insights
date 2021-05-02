{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "interim-square",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from pathlib import Path\n",
    "%matplotlib inline\n",
    "from pylab import mpl, plt\n",
    "import datetime\n",
    "import tensorflow as tf\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n",
    "from keras.optimizers import Adam, RMSprop\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "alien-huntington",
   "metadata": {},
   "outputs": [],
   "source": [
    "path = '../data/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "tired-partner",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2010-01-04</td>\n",
       "      <td>10430.690430</td>\n",
       "      <td>10641.620117</td>\n",
       "      <td>10430.690430</td>\n",
       "      <td>10583.959961</td>\n",
       "      <td>10583.959961</td>\n",
       "      <td>3991400000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2010-01-05</td>\n",
       "      <td>10584.559570</td>\n",
       "      <td>10647.139648</td>\n",
       "      <td>10468.860352</td>\n",
       "      <td>10572.019531</td>\n",
       "      <td>10572.019531</td>\n",
       "      <td>2491020000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2010-01-06</td>\n",
       "      <td>10564.719727</td>\n",
       "      <td>10655.219727</td>\n",
       "      <td>10488.280273</td>\n",
       "      <td>10573.679688</td>\n",
       "      <td>10573.679688</td>\n",
       "      <td>4972660000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2010-01-07</td>\n",
       "      <td>10571.110352</td>\n",
       "      <td>10655.599609</td>\n",
       "      <td>10471.730469</td>\n",
       "      <td>10606.860352</td>\n",
       "      <td>10606.860352</td>\n",
       "      <td>5270680000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2010-01-08</td>\n",
       "      <td>10606.400391</td>\n",
       "      <td>10653.110352</td>\n",
       "      <td>10509.740234</td>\n",
       "      <td>10618.190430</td>\n",
       "      <td>10618.190430</td>\n",
       "      <td>4389590000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2258</th>\n",
       "      <td>2018-12-21</td>\n",
       "      <td>22871.740234</td>\n",
       "      <td>23285.759766</td>\n",
       "      <td>22356.619141</td>\n",
       "      <td>22445.369141</td>\n",
       "      <td>22445.369141</td>\n",
       "      <td>7609010000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2259</th>\n",
       "      <td>2018-12-24</td>\n",
       "      <td>22317.279297</td>\n",
       "      <td>22438.759766</td>\n",
       "      <td>21751.589844</td>\n",
       "      <td>21792.199219</td>\n",
       "      <td>21792.199219</td>\n",
       "      <td>2613930000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2260</th>\n",
       "      <td>2018-12-26</td>\n",
       "      <td>21857.730469</td>\n",
       "      <td>22887.060547</td>\n",
       "      <td>21668.529297</td>\n",
       "      <td>22878.449219</td>\n",
       "      <td>22878.449219</td>\n",
       "      <td>4233990000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2261</th>\n",
       "      <td>2018-12-27</td>\n",
       "      <td>22629.060547</td>\n",
       "      <td>23144.720703</td>\n",
       "      <td>22233.449219</td>\n",
       "      <td>23138.820313</td>\n",
       "      <td>23138.820313</td>\n",
       "      <td>4096610000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2262</th>\n",
       "      <td>2018-12-28</td>\n",
       "      <td>23213.609375</td>\n",
       "      <td>23426.169922</td>\n",
       "      <td>22928.179688</td>\n",
       "      <td>23062.400391</td>\n",
       "      <td>23062.400391</td>\n",
       "      <td>3702620000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2263 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Date          Open          High           Low         Close  \\\n",
       "0     2010-01-04  10430.690430  10641.620117  10430.690430  10583.959961   \n",
       "1     2010-01-05  10584.559570  10647.139648  10468.860352  10572.019531   \n",
       "2     2010-01-06  10564.719727  10655.219727  10488.280273  10573.679688   \n",
       "3     2010-01-07  10571.110352  10655.599609  10471.730469  10606.860352   \n",
       "4     2010-01-08  10606.400391  10653.110352  10509.740234  10618.190430   \n",
       "...          ...           ...           ...           ...           ...   \n",
       "2258  2018-12-21  22871.740234  23285.759766  22356.619141  22445.369141   \n",
       "2259  2018-12-24  22317.279297  22438.759766  21751.589844  21792.199219   \n",
       "2260  2018-12-26  21857.730469  22887.060547  21668.529297  22878.449219   \n",
       "2261  2018-12-27  22629.060547  23144.720703  22233.449219  23138.820313   \n",
       "2262  2018-12-28  23213.609375  23426.169922  22928.179688  23062.400391   \n",
       "\n",
       "         Adj Close      Volume  \n",
       "0     10583.959961  3991400000  \n",
       "1     10572.019531  2491020000  \n",
       "2     10573.679688  4972660000  \n",
       "3     10606.860352  5270680000  \n",
       "4     10618.190430  4389590000  \n",
       "...            ...         ...  \n",
       "2258  22445.369141  7609010000  \n",
       "2259  21792.199219  2613930000  \n",
       "2260  22878.449219  4233990000  \n",
       "2261  23138.820313  4096610000  \n",
       "2262  23062.400391  3702620000  \n",
       "\n",
       "[2263 rows x 7 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "djia = pd.read_csv(path+'djia_.csv')\n",
    "djia"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "prospective-dutch",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "djia.dropna(axis=0, how='all', inplace=True)\n",
    "djia.dropna(axis=1, how='any', inplace=True)\n",
    "djia.isna().sum().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "african-process",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia.set_index('Date', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "steady-korea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 2263 entries, 2010-01-04 to 2018-12-28\n",
      "Data columns (total 6 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   Open       2263 non-null   float64\n",
      " 1   High       2263 non-null   float64\n",
      " 2   Low        2263 non-null   float64\n",
      " 3   Close      2263 non-null   float64\n",
      " 4   Adj Close  2263 non-null   float64\n",
      " 5   Volume     2263 non-null   int64  \n",
      "dtypes: float64(5), int64(1)\n",
      "memory usage: 123.8+ KB\n"
     ]
    }
   ],
   "source": [
    "djia.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "corrected-comment",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aquatic-raising",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "configured-month",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close = djia[['Close']].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "hollow-deposit",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close.rename(columns={'Close' : 'price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "union-duplicate",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "living-coating",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close['return'] = np.log(djia_close[['price']] / \n",
    "                            djia_close[['price']].shift(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "consistent-local",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close['direction'] = np.where(djia_close['return']> 0, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "diagnostic-bahamas",
   "metadata": {},
   "outputs": [],
   "source": [
    "lags = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cardiovascular-priest",
   "metadata": {},
   "outputs": [],
   "source": [
    "cols = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "explicit-resident",
   "metadata": {},
   "outputs": [],
   "source": [
    "for lag in range(1, lags + 1):\n",
    "    col = f'lag_{lag}'\n",
    "    djia_close[col] = djia_close['return'].shift(lag)\n",
    "    cols.append(col)\n",
    "djia_close.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "damaged-notebook",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>return</th>\n",
       "      <th>direction</th>\n",
       "      <th>lag_1</th>\n",
       "      <th>lag_2</th>\n",
       "      <th>lag_3</th>\n",
       "      <th>lag_4</th>\n",
       "      <th>lag_5</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2018-12-21</th>\n",
       "      <td>22445.3691</td>\n",
       "      <td>-0.0183</td>\n",
       "      <td>0</td>\n",
       "      <td>-0.0201</td>\n",
       "      <td>-0.0150</td>\n",
       "      <td>0.0035</td>\n",
       "      <td>-0.0213</td>\n",
       "      <td>-0.0204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-24</th>\n",
       "      <td>21792.1992</td>\n",
       "      <td>-0.0295</td>\n",
       "      <td>0</td>\n",
       "      <td>-0.0183</td>\n",
       "      <td>-0.0201</td>\n",
       "      <td>-0.0150</td>\n",
       "      <td>0.0035</td>\n",
       "      <td>-0.0213</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-26</th>\n",
       "      <td>22878.4492</td>\n",
       "      <td>0.0486</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.0295</td>\n",
       "      <td>-0.0183</td>\n",
       "      <td>-0.0201</td>\n",
       "      <td>-0.0150</td>\n",
       "      <td>0.0035</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-27</th>\n",
       "      <td>23138.8203</td>\n",
       "      <td>0.0113</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0486</td>\n",
       "      <td>-0.0295</td>\n",
       "      <td>-0.0183</td>\n",
       "      <td>-0.0201</td>\n",
       "      <td>-0.0150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-28</th>\n",
       "      <td>23062.4004</td>\n",
       "      <td>-0.0033</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0113</td>\n",
       "      <td>0.0486</td>\n",
       "      <td>-0.0295</td>\n",
       "      <td>-0.0183</td>\n",
       "      <td>-0.0201</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 price  return  direction   lag_1   lag_2   lag_3   lag_4  \\\n",
       "Date                                                                        \n",
       "2018-12-21  22445.3691 -0.0183          0 -0.0201 -0.0150  0.0035 -0.0213   \n",
       "2018-12-24  21792.1992 -0.0295          0 -0.0183 -0.0201 -0.0150  0.0035   \n",
       "2018-12-26  22878.4492  0.0486          1 -0.0295 -0.0183 -0.0201 -0.0150   \n",
       "2018-12-27  23138.8203  0.0113          1  0.0486 -0.0295 -0.0183 -0.0201   \n",
       "2018-12-28  23062.4004 -0.0033          0  0.0113  0.0486 -0.0295 -0.0183   \n",
       "\n",
       "             lag_5  \n",
       "Date                \n",
       "2018-12-21 -0.0204  \n",
       "2018-12-24 -0.0213  \n",
       "2018-12-26  0.0035  \n",
       "2018-12-27 -0.0150  \n",
       "2018-12-28 -0.0201  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "djia_close.round(4).tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "loving-defense",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tensorflow in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (2.0.0)\n",
      "Requirement already satisfied: keras-preprocessing>=1.0.5 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.1.2)\n",
      "Requirement already satisfied: absl-py>=0.7.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.12.0)\n",
      "Requirement already satisfied: opt-einsum>=2.3.2 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (3.3.0)\n",
      "Requirement already satisfied: tensorboard<2.1.0,>=2.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (2.0.2)\n",
      "Requirement already satisfied: tensorflow-estimator<2.1.0,>=2.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (2.0.1)\n",
      "Requirement already satisfied: six>=1.10.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.12.0)\n",
      "Requirement already satisfied: wheel>=0.26 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.36.2)\n",
      "Requirement already satisfied: keras-applications>=1.0.8 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.0.8)\n",
      "Requirement already satisfied: gast==0.2.2 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.2.2)\n",
      "Requirement already satisfied: google-pasta>=0.1.6 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.2.0)\n",
      "Requirement already satisfied: wrapt>=1.11.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.12.1)\n",
      "Requirement already satisfied: numpy<2.0,>=1.16.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.19.5)\n",
      "Requirement already satisfied: termcolor>=1.1.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.1.0)\n",
      "Requirement already satisfied: grpcio>=1.8.6 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.36.1)\n",
      "Requirement already satisfied: protobuf>=3.6.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (3.14.0)\n",
      "Requirement already satisfied: astor>=0.6.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.8.1)\n",
      "Requirement already satisfied: h5py in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from keras-applications>=1.0.8->tensorflow) (3.1.0)\n",
      "Requirement already satisfied: google-auth<2,>=1.6.3 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (1.24.0)\n",
      "Requirement already satisfied: setuptools>=41.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (52.0.0.post20210125)\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (2.25.1)\n",
      "Requirement already satisfied: markdown>=2.6.8 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (3.3.4)\n",
      "Requirement already satisfied: werkzeug>=0.11.15 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (1.0.1)\n",
      "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (0.4.2)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (4.6)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (0.2.8)\n",
      "Requirement already satisfied: cachetools<5.0,>=2.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (4.2.0)\n",
      "Requirement already satisfied: requests-oauthlib>=0.7.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.1.0,>=2.0.0->tensorflow) (1.3.0)\n",
      "Requirement already satisfied: importlib-metadata in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow) (2.0.0)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (0.4.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (1.26.3)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (3.0.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (2.10)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (2020.12.5)\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.1.0,>=2.0.0->tensorflow) (3.1.0)\n",
      "Requirement already satisfied: cached-property in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from h5py->keras-applications>=1.0.8->tensorflow) (1.5.2)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from importlib-metadata->markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow) (3.4.0)\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "charming-invasion",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:516: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint8 = np.dtype([(\"qint8\", np.int8, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:517: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint8 = np.dtype([(\"quint8\", np.uint8, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:518: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint16 = np.dtype([(\"qint16\", np.int16, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:519: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint16 = np.dtype([(\"quint16\", np.uint16, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:520: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint32 = np.dtype([(\"qint32\", np.int32, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\framework\\dtypes.py:525: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  np_resource = np.dtype([(\"resource\", np.ubyte, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:541: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint8 = np.dtype([(\"qint8\", np.int8, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:542: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint8 = np.dtype([(\"quint8\", np.uint8, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:543: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint16 = np.dtype([(\"qint16\", np.int16, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:544: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_quint16 = np.dtype([(\"quint16\", np.uint16, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:545: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  _np_qint32 = np.dtype([(\"qint32\", np.int32, 1)])\n",
      "C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorboard\\compat\\tensorflow_stub\\dtypes.py:550: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.\n",
      "  np_resource = np.dtype([(\"resource\", np.ubyte, 1)])\n",
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "humanitarian-webcam",
   "metadata": {},
   "outputs": [],
   "source": [
    "optimizer = Adam(learning_rate=0.0001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "complete-thomas",
   "metadata": {},
   "outputs": [],
   "source": [
    "def set_seeds(seed=100):\n",
    "    random.seed(seed)\n",
    "    np.random.seed(seed)\n",
    "    tf.set_random_seed(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "incident-indonesian",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "associate-tours",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\tensorflow\\python\\ops\\nn_impl.py:180: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use tf.where in 2.0, which has the same broadcast rule as np.where\n"
     ]
    }
   ],
   "source": [
    "set_seeds()\n",
    "model = Sequential()\n",
    "model.add(Dense(64, activation='relu',\n",
    "               input_shape=(lags,)))\n",
    "model.add(Dense(64, activation='relu'))\n",
    "model.add(Dense(1, activation='sigmoid'))\n",
    "model.compile(optimizer=optimizer,\n",
    "             loss='binary_crossentropy',\n",
    "             metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "forbidden-sweden",
   "metadata": {},
   "outputs": [],
   "source": [
    "cutoff = '2017-10-31'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "weird-touch",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data = djia_close[djia_close.index < cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "deluxe-session",
   "metadata": {},
   "outputs": [],
   "source": [
    "mu, std = training_data.mean(), training_data.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "appointed-invasion",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_ = (training_data - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "dirty-status",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data = djia_close[djia_close.index >= cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "neural-gauge",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data_ = (test_data - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "champion-crossing",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\keras\\backend\\tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.\n",
      "\n",
      "Wall time: 9.41 s\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.callbacks.History at 0x26a7eb20148>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%time\n",
    "model.fit(training_data[cols],\n",
    "          training_data['direction'],\n",
    "          epochs=300, verbose=False,\n",
    "          validation_split=0.2, shuffle=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "advance-administrator",
   "metadata": {},
   "outputs": [],
   "source": [
    "res = pd.DataFrame(model.history.history)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "printable-answer",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>val_loss</th>\n",
       "      <th>val_accuracy</th>\n",
       "      <th>loss</th>\n",
       "      <th>accuracy</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.692557</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.692976</td>\n",
       "      <td>0.526718</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.692011</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.692505</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.691474</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.692070</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.690982</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.691670</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.690559</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.691328</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>295</th>\n",
       "      <td>0.687805</td>\n",
       "      <td>0.534351</td>\n",
       "      <td>0.687077</td>\n",
       "      <td>0.549618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>296</th>\n",
       "      <td>0.687803</td>\n",
       "      <td>0.534351</td>\n",
       "      <td>0.687064</td>\n",
       "      <td>0.549618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>297</th>\n",
       "      <td>0.687803</td>\n",
       "      <td>0.534351</td>\n",
       "      <td>0.687051</td>\n",
       "      <td>0.549618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>298</th>\n",
       "      <td>0.687799</td>\n",
       "      <td>0.534351</td>\n",
       "      <td>0.687040</td>\n",
       "      <td>0.549618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>299</th>\n",
       "      <td>0.687796</td>\n",
       "      <td>0.534351</td>\n",
       "      <td>0.687027</td>\n",
       "      <td>0.550254</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>300 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     val_loss  val_accuracy      loss  accuracy\n",
       "0    0.692557      0.547074  0.692976  0.526718\n",
       "1    0.692011      0.547074  0.692505  0.538168\n",
       "2    0.691474      0.547074  0.692070  0.538168\n",
       "3    0.690982      0.547074  0.691670  0.538168\n",
       "4    0.690559      0.547074  0.691328  0.538168\n",
       "..        ...           ...       ...       ...\n",
       "295  0.687805      0.534351  0.687077  0.549618\n",
       "296  0.687803      0.534351  0.687064  0.549618\n",
       "297  0.687803      0.534351  0.687051  0.549618\n",
       "298  0.687799      0.534351  0.687040  0.549618\n",
       "299  0.687796      0.534351  0.687027  0.550254\n",
       "\n",
       "[300 rows x 4 columns]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "hindu-irish",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3cAAAGbCAYAAABnKmnGAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABl90lEQVR4nO3dd3xb1f3/8dexvPdM4myH7EkGgQQySCCMAil8oUD5AYXSlrbQQRddlG/poP3SQYGW1TJaKKVQKFDKCBCHESAJJGQ7znaWZ7yXpPP7Q7JjxzuWdW3p/Xw88pB0z9W9H+lKzv3onHs+xlqLiIiIiIiIDGwRTgcgIiIiIiIivafkTkREREREJAQouRMREREREQkBSu5ERERERERCgJI7ERERERGREBDpdAA9kZmZaUePHu10GCIiIiIiIo5Yt25dsbU2q722AZXcjR49mrVr1zodhoiIiIiIiCOMMXs7atOwTBERERERkRCg5E5ERERERCQEKLkTEREREREJAQPqmrv2NDY2UlBQQF1dndOhCBAbG8vw4cOJiopyOhQRERERkbAy4JO7goICkpKSGD16NMYYp8MJa9ZaSkpKKCgoICcnx+lwRERERETCyoAflllXV0dGRoYSu37AGENGRoZ6UUVEREREHDDgkztAiV0/omMhIiIiIuKMkEjuREREREREwp2SOxERERERkRCg5G4AcbvdTocgIiIiIiL9lJK7APn0pz/N7NmzmTJlCg8++CAAr7zyCrNmzWLGjBksXboUgKqqKq677jqmTZvG9OnTefbZZwFITExs3tYzzzzD5z73OQA+97nPccstt3DmmWfyve99jw8//JD58+czc+ZM5s+fz/bt2wHweDx8+9vfbt7uPffcwxtvvMHFF1/cvN3XX3+dSy65JBhvh4iIiIiIBNmAL4VwvMsfWN1m2QXTs7l63mhqGzx87pEP27RfOns4l80ZQWl1A1/+27pWbf/40rxu7fcvf/kL6enp1NbWcsopp7B8+XK+8IUvsGrVKnJycigtLQXgjjvuICUlhY0bNwJQVlbW5bbz8vJYsWIFLpeLiooKVq1aRWRkJCtWrOAHP/gBzz77LA8++CC7d+/m448/JjIyktLSUtLS0vjqV79KUVERWVlZPPLII1x33XXdej0iIiIiIjKwhFxy55Q//OEPPPfccwDs37+fBx98kIUL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AREt5ok0BkwniVlv2/sxzZYZAB6vZssUERERERFnKbkLALfHl9yp505ERERERJyi5C4AmnvuXEruRERERETEGbrmLgCGpsbx+jcXMihZde5ERERERMQZSu4CIDoyQiUQRERERETEURqWGQDFVfX8+Z3d7CupcToUEREREREJU0ruAuDg0VrueGkLOwornQ5FRERERETClJK7AHB7NVumiIiIiIg4S8ldAByrc6e3U0REREREnKFsJABU505ERERERJym5C4AVOdOREREREScplIIATBndBrv3bqE9IRop0MREREREZEwpeQuAGKjXAxNjXM6DBERERERCWMalhkA+YVV3PPGDooq650ORUREREREwpSSuwDYcaSS37yeR0m1kjsREREREXGGkrsAcKsUgoiIiIiIOEzZSAAcq3On2TJFRERERMQZSu4CoKnnTnXuRERERETEKUruAsDj9QKqcyciIiIiIs5RKYQAuHjmcM6dmk1SjN5OERERERFxhrKRAIiOjCA6Up2gIiIiIiLiHGUkAfDBrhJ++d+t1DV6nA5FRERERETClJK7ANhQcJQHcnc1z5opIiIiIiISbEruAkCzZYqIiIiIiNOU3AWAx6PkTkREREREnKXkLgCae+6MkjsREREREXGGkrsA8HgtEQYi1HMnIiIiIiIOUSmEAPjWsvF846xxTochIiIiIiJhTMldABhjiHSp105ERERERJyjYZkB8NInB/n5f7Y4HYaIiIiIiIQxJXcB8OHuUp5ZV+B0GCIiIiIiEsaU3AWA22txReitFBERERER5ygjCQCPxxKpmTJFRERERMRBSu4CwNdzp+RORERERESco+QuACIjDPHRLqfDEBERERGRMKZSCAHwq0unOx2CiIiIiIiEOfXciYiIiIiIhAAldwHw8Nu7uOvV7U6HISIiIiIiYUzJXQCs3lnCyrxCp8MQEREREZEwpuQuAFTnTkREREREnKaMJAA8XtW5ExERERERZym5CwC316s6dyIiIiIi4iiVQgiApNgolNuJiIiIiIiTlNwFwEPXzHE6BBERERERCXMalikiIiIiIhIClNwFwP++uJn73sp3OgwREREREQljGpYZAO/ll5CTmeB0GCIiIiIiEsbUcxcAbq8Xl0szqoiIiIiIiHOU3AWA6tyJiIiIiIjTlNwFgNtrVedOREREREQcpeQuAIamxJGVFON0GCIiIiIiEsY0oUoAPH3jPKdDEBERERGRMKeeOxERERERkRCg5C4AbnhsDY+v3uN0GCIiIiIiEsaU3AXA6p0l7CupcToMEREREREJY0ruAsDttapzJyIiIiIijupWcmeMOdcYs90Yk2+MubWd9sXGmHJjzHr/v9v8y2ONMR8aYzYYYzYbY/63xXPSjTGvG2N2+G/TAveygkt17kRERERExGldJnfGGBdwH3AeMBm40hgzuZ1V37bWnuz/91P/snpgibV2BnAycK4x5jR/263AG9baccAb/scDjrXWX+dOnaAiIiIiIuKc7mQkc4F8a+0ua20D8BSwvDsbtz5V/odR/n/W/3g58Jj//mPAp7sbdH9iLUwZmszgZNW5ExERERER53Snzt0wYH+LxwXAqe2sN88YswE4CHzbWrsZmnv+1gFjgfustR/41x9srT0EYK09ZIwZdIKvwVEREYb/fG2B02GIiIiIiEiY607PXXsXk9njHn8EjPIPv7wHeL55RWs91tqTgeHAXGPM1J4EaIz5ojFmrTFmbVFRUU+eKiIiIiIiEja6k9wVACNaPB6Or3eumbW2omn4pbX2ZSDKGJN53DpHgZXAuf5FR4wx2QD+28L2dm6tfdBaO8daOycrK6sb4QZXVb2bi+59h3+vP+B0KCIiIiIiEsa6k9ytAcYZY3KMMdHAFcALLVcwxgwxxhj//bn+7ZYYY7KMMan+5XHAWcA2/9NeAK71378W+HcvX4sjGt1ePikop6y6welQREREREQkjHV5zZ211m2MuQl4FXABf7HWbjbG3Ohvvx+4FPiyMcYN1AJXWGutv0fuMf91dxHA09bal/ybvhN42hjzeWAfcFmgX1wwuL2+Eaoul2bLFBERERER53RnQpWmoZYvH7fs/hb37wXubed5nwAzO9hmCbC0J8H2R56m5M6ozp2IiIiIiDhH3U295PZ6AVTEXEREREREHKXkrpeiXBHMzUknS3XuRERERETEQd0alikdG5wcy9Nfmud0GCIiIiIiEubUcyciIiIiIhIClNz1Un5hJUvuWsk7O4qdDkVERERERMKYkrteqm3wsqu4mrpGj9OhiIiIiIhIGFNy10tNs2W6XJotU0REREREnKPkrpea6typFIKIiIiIiDhJyV0vuZuKmCu5ExERERERBym566Xk2CjOnJBFekK0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\n",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "res[['accuracy', 'val_accuracy']].plot(figsize=(15,7), style='--')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "brave-function",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1965/1965 [==============================] - 0s 8us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[2.2884131854423737, 0.5180661678314209]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(training_data_[cols], training_data['direction'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "subjective-brown",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(training_data_[cols]) > 0.5, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "dated-promise",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1,\n",
       "       0, 1, 0, 1, 0, 1, 1, 1])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred[:30].flatten()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "material-microphone",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "flush-fleet",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data['strategy'] = (training_data['prediction'] * \n",
    "                            training_data['return'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "previous-aggregate",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "return      2.189494\n",
       "strategy    2.204221\n",
       "dtype: float64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " training_data[['return', 'strategy']].sum().apply(np.exp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "stunning-easter",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Date'>"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    " training_data[['return', 'strategy']].cumsum().apply(np.exp).plot(figsize=(15,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "accurate-illness",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "292/292 [==============================] - 0s 17us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[3.1507001641678483, 0.44863012433052063]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(test_data_[cols], test_data['direction'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "painful-workshop",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(test_data_[cols]) > 0.5, 1, 0 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "advised-worry",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "detailed-monitor",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " 1    172\n",
       "-1    120\n",
       "Name: prediction, dtype: int64"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_data['prediction'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "faced-driving",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['strategy'] = (test_data['prediction'] * \n",
    "                        test_data['return'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "floppy-butterfly",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "return      0.987736\n",
       "strategy    0.806534\n",
       "dtype: float64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_data[['return', 'strategy']].sum().apply(np.exp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "competent-andorra",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Date'>"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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REQkZSiAExERERERSREK4ERERERERFKEAjgREREREZEUoQBOREREREQkRSiAExERERERSREK4ERERERERFKEAjgREREREZEUoQBOREREREQkRSiAExERERERSREK4ERERERERFKEAjgREREREZEUoQBOREREREQkRSiAExERERERSREK4ERERERERFKE8zwv0W0owzm3GVid6HZE0AbYkuhGSMLpOBCfjgXx6VgQn44FAR0HElSdY6Gr53ltw1cmZQCXrJxzszzPG57odkhi6TgQn44F8elYEJ+OBQEdBxJUE8eChlCKiIiIiIikCAVwIiIiIiIiKUIBXOU8mOgGSFLQcSA+HQvi07EgPh0LAjoOJCjux4LmwImIiIiIiKQI9cCJiIiIiIikCAVwIiIiIiIiKSJlAzjnXK5zbpJzbpFzboFz7qeB9VnOuY+cc0sDy9aB9dmB1+92zk0M2U+6c25OyNcW59xdUd7zL865Nc653WHrmzjnXnDOLXPOzXDOdYuy/fXOuXmB95nsnOsf8tz7zrkdzrm3q//bqV/idSwEnrso8DeaG/ibtInynsMCr1vmnLvHOecC6491zs12zhU5584tp80RX+ecG+Kcmxb4OeY65y6Ix++ovkiyYyHq/3vY9r9wzi0MvM8nzrmugfUnhH027XfOnR3HX1edlUzHQeC58wN/4wXOuWejbB/xPKLjoHqS6VhwznUJ7PubwD5Oj7J9tPODjoVqSNCxUN3rxojnh8Bztzvn5ge+dK1Q33iel5JfQEdgaOD7dGAJ0B/4B/CbwPrfALcHvm8BHA1cD0wsZ79fA8dGeW5U4H13h63/MXB/4PsLgReibJ8R8v1ZwPshj08CzgTeTvTvNtW+4nUsAA2BTUCbwON/AH+I8p4zgSMBB7wHnBZY3w0YBDwJnFtOmyO+DugN5AW+7wRsAFol+necKl9JdixE/X8P2/4EoHng+xsifX4AWcA2/3X6SqnjIA/4BmgdeNwuyvYVnkd0HKT8sfAgcEPg+/7Aqijbd6OC84iOhZQ5Fqp73Rjx/ACMAz4KtKUFMIuQc46+6v5XyvbAeZ63wfO82YHvC4FFQA4wHngi8LIngLMDr9njed5kYH+0fTrn8oB2wJdR3nO653kbIjwV+p4vAyeF3n0N2X5XyMMWgBfy3CdAYbS2SXRxPBZc4KtF4O+XAawPfz/nXEfsg3Ka53kedpL1973K87y5QEkFbY74Os/zlnietzTw/XrsJNE2hl+DkHTHQtT/97A2T/I8b2/g4XSgc4SXnQu8F/I6KUcyHQfANcC9nudtD7zXpijNjuU8ouOgkpLsWPAC2wFkRto+0IZYziM6Fiqpto+FwD6qe90Y7fzQH/jc87wiz/P2AN8CY8v58aWOSdkALlSg6/lwYAbQ3v9nCSzbVWJXF2F3NyqbmjMHWBN4zyJgJ5Adpa03OueWY3dsbq7k+0gFqnMseJ53CLvDNQ/7MO4PPBLhpTnA2pDHawPr4so5NwJoDCyP977rg2Q4Fqrw/34Vdsc+3IXAczFsL2GS4DjoDfR2zk1xzk13zkW7yIrlPKLjoBqS4Fj4A3CJc24t8C7wkyr+KKBjoVpq6VgoT8zXjSFCzw/fAqc555oHhm+eAORWsg2SwlI+gHPOtQReAX4Wdse7Kqr6gVjmrgnR77bf63leT+DXwP9W4b0kiuoeC865RtiH8uHY8MW5wG8jvTTCurjW4wjcxX0KuNLzvHJ786SsZDkWKvP/7py7BBgO3BG2viMwEPigEj+CkDTHQUNsGOXx2E3Ch51zrSq5Dx0H1ZQkx8JFwOOe53UGTgeecs5V+jpMx0L11OKxUO5uIqyLeh0Rfn7wPO9D7CbAVOy6dRpQVMk2SApL6QAu8E/0CvCM53mvBlZvDHy4+R9y0YarhO9rMNDQ87yvA4/TQiYK/7GCzdcSuPPhnGuIDY3YFpi8Osc5NyfCNs8THFYh1RSnY2EIgOd5ywO9sC8CoyMcC2spPcytM1GGT4S0r7xjIfy1GcA7wP96nje9otdLaUl6LHz//x7pWHDOjQF+B5zled6BsG3PB14L3PWVGCXRcbAWeMPzvEOe560EFgN5EY6DiOeRkH3qOKiiJDoWrgpsh+d504CmQJvKnB8CdCxUUS0fC+WJ+box2vnB87y/eJ43xPO8k7GAcGkMvwKpI1I2gAuMFX4EWOR53r9DnnoTuDzw/eXAGzHu8iJCet88zysO/GMM8Tzvtgq2DX3Pc4FPPfM7fx+BNueFbDMO/bPFRRyPhXVAf+ecP+fs5MA+Sx0LgSEWhc65UYH3vqyifYcfC+X8LI2B14AnPc97qYL2SphkOhai/b9H+Fw4HHgAOzlHunAo9dkkFUum4wB4HRveRGCoU29gRYTPhIjnkZC26DiogiQ7FvKxhGU45/phAdzmWM8PIXQsVEFtHwsV7CPW68aI54dAsJgd+H4QlvTmwwreU+oSLwkyqVTlC8sM5GFd13MCX6djY4g/wS6WPgGyQrZZhd3R3I3d/egf8twKoG8F7/mPwHYlgeUfAuubAi8By7DsUz2ibH83sCDQ1knAgJDnvgQ2A/sC+z410b/jVPmK57GAZZtaFNjXW0B2lPccDszH5qdNBFxg/RGB/e0BtgILomwf8XXAJcChkJ9jDjAk0b/jVPlKsmMh6v972PYfAxtD2vtmyHPdsIuFBon+3abSV5IdBw74N7AQmzNzYZTto55HdBzUmWOhPzAFm780BzglyvZRzyM6FlLuWKjudWPE80Ng+4WBr+noOqHeffkfKiIiIiIiIpLkUnYIpYiIiIiISH2jAE5ERERERCRFKIATERERERFJEQrgREREREREUoQCOBERERERkRShAE5EROoF51xxoEjuAufct865Xzjnyj0POue6Oecurq02ioiIVEQBnIiI1Bf7PCuSOwArvns68PsKtukGKIATEZGkoTpwIiJSLzjndnue1zLkcQ/gK6AN0BV4CmgRePomz/OmOuemA/2AlcATwD3A34HjgSbAvZ7nPVBrP4SIiNR7CuBERKReCA/gAuu2A32BQqDE87z9zrk84DnP84Y7544Hful53hmB118LtPM878/OuSbAFOA8z/NW1ubPIiIi9VfDRDdAREQkgVxg2QiY6JwbAhQDvaO8/hRgkHPu3MDjTCAP66ETERGpcQrgRESkXgoMoSwGNmFz4TYCg7H54fujbQb8xPO8D2qlkSIiImGUxEREROod51xb4H5gomdzCTKBDZ7nlQCXAmmBlxYC6SGbfgDc4JxrFNhPb+dcC0RERGqJeuBERKS+aOacm4MNlyzCkpb8O/Dcf4FXnHPnAZOAPYH1c4Ei59y3wOPA3VhmytnOOQdsBs6uneaLiIgoiYmIiIiIiEjK0BBKERERERGRFKEATkREREREJEUogBMREREREUkRCuBERERERERShAI4ERERERGRFKEATkREREREJEUogBMREREREUkR/x+CtaTnC2WE6gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "test_data[['return', 'strategy']].cumsum().apply(np.exp).plot(figsize=(15,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "chicken-reflection",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "technological-cuisine",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "unlike-technique",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Adding Different Types of Fetures \n",
    "djia_close['momentum'] = djia_close['return'].rolling(5).mean().shift(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "protective-store",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close['volatility'] = djia_close['return'].rolling(20).std().shift(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "accompanied-maintenance",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close['distance'] = (djia_close['price'] - \n",
    "                          djia_close['price'].rolling(50).mean()).shift(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "international-nepal",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close.dropna(inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "assumed-writer",
   "metadata": {},
   "outputs": [],
   "source": [
    "cols.extend(['momentum', 'volatility', 'distance'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "guilty-occurrence",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "bottom-proxy",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 price  return  direction   lag_1   lag_2   lag_3   lag_4  \\\n",
      "Date                                                                        \n",
      "2018-12-21  22445.3691 -0.0183          0 -0.0201 -0.0150  0.0035 -0.0213   \n",
      "2018-12-24  21792.1992 -0.0295          0 -0.0183 -0.0201 -0.0150  0.0035   \n",
      "2018-12-26  22878.4492  0.0486          1 -0.0295 -0.0183 -0.0201 -0.0150   \n",
      "2018-12-27  23138.8203  0.0113          1  0.0486 -0.0295 -0.0183 -0.0201   \n",
      "2018-12-28  23062.4004 -0.0033          0  0.0113  0.0486 -0.0295 -0.0183   \n",
      "\n",
      "             lag_5  momentum  volatility   distance  \n",
      "Date                                                 \n",
      "2018-12-21 -0.0204   -0.0147      0.0144 -2124.1907  \n",
      "2018-12-24 -0.0213   -0.0142      0.0147 -2475.3537  \n",
      "2018-12-26  0.0035   -0.0159      0.0158 -3063.3110  \n",
      "2018-12-27 -0.0150   -0.0069      0.0195 -1927.8302  \n",
      "2018-12-28 -0.0201   -0.0016      0.0197 -1625.2245  \n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(djia_close\n",
    "      .round(4).tail())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "signed-adjustment",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_new = djia_close[djia_close.index < cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "graduate-heath",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "sublime-armstrong",
   "metadata": {},
   "outputs": [],
   "source": [
    "mu, std = training_data_new.mean(), training_data_new.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "enormous-lindsay",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_training_data_ = (training_data_new - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "maritime-locator",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data = djia_close[djia_close.index >= cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "typical-hammer",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>return</th>\n",
       "      <th>direction</th>\n",
       "      <th>lag_1</th>\n",
       "      <th>lag_2</th>\n",
       "      <th>lag_3</th>\n",
       "      <th>lag_4</th>\n",
       "      <th>lag_5</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-10-31</th>\n",
       "      <td>2.413964</td>\n",
       "      <td>0.094139</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>-0.465030</td>\n",
       "      <td>0.117020</td>\n",
       "      <td>0.304188</td>\n",
       "      <td>-0.597103</td>\n",
       "      <td>0.777878</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-01</th>\n",
       "      <td>2.431477</td>\n",
       "      <td>0.237259</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>0.093676</td>\n",
       "      <td>-0.465010</td>\n",
       "      <td>0.117015</td>\n",
       "      <td>0.303926</td>\n",
       "      <td>-0.596705</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-02</th>\n",
       "      <td>2.460693</td>\n",
       "      <td>0.424801</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>0.236796</td>\n",
       "      <td>0.093696</td>\n",
       "      <td>-0.465014</td>\n",
       "      <td>0.116736</td>\n",
       "      <td>0.304455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-03</th>\n",
       "      <td>2.463060</td>\n",
       "      <td>-0.007686</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>0.424339</td>\n",
       "      <td>0.236817</td>\n",
       "      <td>0.093692</td>\n",
       "      <td>-0.465346</td>\n",
       "      <td>0.117238</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-06</th>\n",
       "      <td>2.465859</td>\n",
       "      <td>-0.000775</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>-0.008150</td>\n",
       "      <td>0.424360</td>\n",
       "      <td>0.236812</td>\n",
       "      <td>0.093411</td>\n",
       "      <td>-0.464929</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-21</th>\n",
       "      <td>2.131456</td>\n",
       "      <td>-2.142411</td>\n",
       "      <td>-1.083086</td>\n",
       "      <td>-2.350449</td>\n",
       "      <td>-1.763535</td>\n",
       "      <td>0.354831</td>\n",
       "      <td>-2.487000</td>\n",
       "      <td>-2.386325</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-24</th>\n",
       "      <td>1.933439</td>\n",
       "      <td>-3.431760</td>\n",
       "      <td>-1.083086</td>\n",
       "      <td>-2.142884</td>\n",
       "      <td>-2.350433</td>\n",
       "      <td>-1.763537</td>\n",
       "      <td>0.354574</td>\n",
       "      <td>-2.486878</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-26</th>\n",
       "      <td>2.262749</td>\n",
       "      <td>5.531495</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>-3.432238</td>\n",
       "      <td>-2.142867</td>\n",
       "      <td>-2.350434</td>\n",
       "      <td>-1.763986</td>\n",
       "      <td>0.355111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-27</th>\n",
       "      <td>2.341684</td>\n",
       "      <td>1.251756</td>\n",
       "      <td>0.922818</td>\n",
       "      <td>5.531053</td>\n",
       "      <td>-3.432224</td>\n",
       "      <td>-2.142869</td>\n",
       "      <td>-2.350936</td>\n",
       "      <td>-1.763759</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-28</th>\n",
       "      <td>2.318516</td>\n",
       "      <td>-0.425022</td>\n",
       "      <td>-1.083086</td>\n",
       "      <td>1.251296</td>\n",
       "      <td>5.531085</td>\n",
       "      <td>-3.432224</td>\n",
       "      <td>-2.143352</td>\n",
       "      <td>-2.350795</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>292 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               price    return  direction     lag_1     lag_2     lag_3  \\\n",
       "Date                                                                      \n",
       "2017-10-31  2.413964  0.094139   0.922818 -0.465030  0.117020  0.304188   \n",
       "2017-11-01  2.431477  0.237259   0.922818  0.093676 -0.465010  0.117015   \n",
       "2017-11-02  2.460693  0.424801   0.922818  0.236796  0.093696 -0.465014   \n",
       "2017-11-03  2.463060 -0.007686   0.922818  0.424339  0.236817  0.093692   \n",
       "2017-11-06  2.465859 -0.000775   0.922818 -0.008150  0.424360  0.236812   \n",
       "...              ...       ...        ...       ...       ...       ...   \n",
       "2018-12-21  2.131456 -2.142411  -1.083086 -2.350449 -1.763535  0.354831   \n",
       "2018-12-24  1.933439 -3.431760  -1.083086 -2.142884 -2.350433 -1.763537   \n",
       "2018-12-26  2.262749  5.531495   0.922818 -3.432238 -2.142867 -2.350434   \n",
       "2018-12-27  2.341684  1.251756   0.922818  5.531053 -3.432224 -2.142869   \n",
       "2018-12-28  2.318516 -0.425022  -1.083086  1.251296  5.531085 -3.432224   \n",
       "\n",
       "               lag_4     lag_5  \n",
       "Date                            \n",
       "2017-10-31 -0.597103  0.777878  \n",
       "2017-11-01  0.303926 -0.596705  \n",
       "2017-11-02  0.116736  0.304455  \n",
       "2017-11-03 -0.465346  0.117238  \n",
       "2017-11-06  0.093411 -0.464929  \n",
       "...              ...       ...  \n",
       "2018-12-21 -2.487000 -2.386325  \n",
       "2018-12-24  0.354574 -2.486878  \n",
       "2018-12-26 -1.763986  0.355111  \n",
       "2018-12-27 -2.350936 -1.763759  \n",
       "2018-12-28 -2.143352 -2.350795  \n",
       "\n",
       "[292 rows x 8 columns]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_data_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "documented-steps",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data_ = (test_data - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "appointed-blank",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "perfect-thailand",
   "metadata": {},
   "outputs": [],
   "source": [
    "set_seeds()\n",
    "model = Sequential()\n",
    "model.add(Dense(32, activation='relu',\n",
    "                input_shape=(len(cols),)))\n",
    "model.add(Dense(32, activation='relu'))\n",
    "model.add(Dense(1, activation='sigmoid'))\n",
    "model.compile(optimizer=optimizer,\n",
    "             loss='binary_crossentropy',\n",
    "             metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "commercial-joseph",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "pacific-biotechnology",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wall time: 1.13 s\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.callbacks.History at 0x26a7eb1b748>"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%time\n",
    "model.fit(new_training_data_[cols], training_data_new['direction'],\n",
    "          verbose=False, epochs=25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "seasonal-counter",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1915/1915 [==============================] - 0s 21us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.6799437691897698, 0.567624032497406]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(new_training_data_[cols], training_data_new['direction'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "sitting-binary",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(new_training_data_[cols]) > 0.5, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "monthly-prescription",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_new['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "molecular-southwest",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_new['strategy'] = (training_data_new['prediction'] *\n",
    "                             training_data_new['return'])\n",
    "                             \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "accomplished-interaction",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "return      2.154708\n",
       "strategy    4.628474\n",
       "dtype: float64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "training_data_new[['return', 'strategy']].sum().apply(np.exp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "inside-investment",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Date'>"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Qpbqp0RNRERERMSZ5r9otgfXQ68rIXy46Tk71pSrITXWFA4Z8wy0Ox16X3FqY5VTpsxVHy3LcgUigf22bU845poFvAWcBRwFrrVte1VVBioiIiIiUufYNmSnO47HPAP7V5rqjgAP7YGtf8DOubB+ijnXfSL4hsCV0059vHLKlKdH7R5g83GujQPa5//cDLxXybhEREREROq+fcshLxv8m8Ndq8AnCDqMNccevuAdCL0ug9OfdNzjG+K0cOXUKVOPmmVZLYDxwPPAf0ppci7wpW3bNrDMsqxAy7Ka2rYdU3WhioiIiIjUIbYNn59l9q//CwJbOq7duQJysx3HAS1g8N3QatCpjVGcpqxDH98EHgT8jnO9ObCvyHF0/rliiZplWTdjetxo1apVeeIUEREREalb0g5DXo7Z9z+memNp5fbHPlv9MUmNcdKhj5ZlTQDibNteeaJmpZyzS5yw7Q9t246wbTsiJERdtiIiIiJSj6UnOPZdVONPiivL34ghwDmWZUUB3wOnWZb19TFtooEifbW0AA5USYQiIiIiInVRQaKmoiBSipMmarZtP2LbdgvbtsOAS4G5tm1feUyzX4GrLWMgkKT5aSIiIiIiJ1CQqHk3dG4cUiOVuTz/sSzLuhXAtu33gZmY0vw7MOX5r6uS6ERERERE6iolanIC5UrUbNueD8zP33+/yHkbuKMqAxMRERERqdPid5htgyDnxiE1UoV71EREREREpALid8La72HRq9DhTPAKcHZEUgMpURMREREROVV2zIavL3Qcn/6U00KRmk11QEVERERETpVN0x37186Axp2dF4vUaOpRExERERE5FfJyYesf0HooXPYdePk7OyKpwdSjJiIiIiJyKsSsgbRD0PdaJWlyUupRExERERGpTjlZ8OlYOLDaHLcZ6dRwpHZQj5qIiIiISHVa9YUjSQPwDXFeLFJrqEdNRERERKSq7JwHKz6G0O6m9D42zHoSXNyheV8Y+ZCzI5RaQomaiIiIiEhl5OWBiwtkHYWvzjPntvwO8190tLnyJ2g32inhSe2koY8iIiIiIhU19Xp4p7dZH+2TMeZcl3NLtvNremrjklpPiZqIiIiI1E9xm+G1TrD4DchILv/9udmwYRokRJlFrGM3mPMXfgrtxhRv69u40uFK/aJETURERETqp4/HQEoMzH4K3hsCiXvN8MWYdWW7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\n",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "training_data_new[['return', 'strategy']].cumsum().apply(np.exp).plot(figsize=(15,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "downtown-documentary",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>price</th>\n",
       "      <th>return</th>\n",
       "      <th>direction</th>\n",
       "      <th>lag_1</th>\n",
       "      <th>lag_2</th>\n",
       "      <th>lag_3</th>\n",
       "      <th>lag_4</th>\n",
       "      <th>lag_5</th>\n",
       "      <th>momentum</th>\n",
       "      <th>volatility</th>\n",
       "      <th>distance</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-10-31</th>\n",
       "      <td>23377.240234</td>\n",
       "      <td>0.001220</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.003653</td>\n",
       "      <td>0.001423</td>\n",
       "      <td>0.003056</td>\n",
       "      <td>-0.004802</td>\n",
       "      <td>0.007184</td>\n",
       "      <td>0.000642</td>\n",
       "      <td>0.003386</td>\n",
       "      <td>880.433007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-01</th>\n",
       "      <td>23435.009766</td>\n",
       "      <td>0.002468</td>\n",
       "      <td>1</td>\n",
       "      <td>0.001220</td>\n",
       "      <td>-0.003653</td>\n",
       "      <td>0.001423</td>\n",
       "      <td>0.003056</td>\n",
       "      <td>-0.004802</td>\n",
       "      <td>-0.000551</td>\n",
       "      <td>0.003355</td>\n",
       "      <td>875.463203</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-02</th>\n",
       "      <td>23531.380859</td>\n",
       "      <td>0.004104</td>\n",
       "      <td>1</td>\n",
       "      <td>0.002468</td>\n",
       "      <td>0.001220</td>\n",
       "      <td>-0.003653</td>\n",
       "      <td>0.001423</td>\n",
       "      <td>0.003056</td>\n",
       "      <td>0.000903</td>\n",
       "      <td>0.003356</td>\n",
       "      <td>902.530352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-03</th>\n",
       "      <td>23539.189453</td>\n",
       "      <td>0.000332</td>\n",
       "      <td>1</td>\n",
       "      <td>0.004104</td>\n",
       "      <td>0.002468</td>\n",
       "      <td>0.001220</td>\n",
       "      <td>-0.003653</td>\n",
       "      <td>0.001423</td>\n",
       "      <td>0.001112</td>\n",
       "      <td>0.003314</td>\n",
       "      <td>964.515624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-06</th>\n",
       "      <td>23548.419922</td>\n",
       "      <td>0.000392</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000332</td>\n",
       "      <td>0.004104</td>\n",
       "      <td>0.002468</td>\n",
       "      <td>0.001220</td>\n",
       "      <td>-0.003653</td>\n",
       "      <td>0.000894</td>\n",
       "      <td>0.003304</td>\n",
       "      <td>937.208437</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-21</th>\n",
       "      <td>22445.369141</td>\n",
       "      <td>-0.018287</td>\n",
       "      <td>0</td>\n",
       "      <td>-0.020097</td>\n",
       "      <td>-0.014978</td>\n",
       "      <td>0.003497</td>\n",
       "      <td>-0.021284</td>\n",
       "      <td>-0.020407</td>\n",
       "      <td>-0.014654</td>\n",
       "      <td>0.014375</td>\n",
       "      <td>-2124.190664</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-24</th>\n",
       "      <td>21792.199219</td>\n",
       "      <td>-0.029532</td>\n",
       "      <td>0</td>\n",
       "      <td>-0.018287</td>\n",
       "      <td>-0.020097</td>\n",
       "      <td>-0.014978</td>\n",
       "      <td>0.003497</td>\n",
       "      <td>-0.021284</td>\n",
       "      <td>-0.014230</td>\n",
       "      <td>0.014726</td>\n",
       "      <td>-2475.353711</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-26</th>\n",
       "      <td>22878.449219</td>\n",
       "      <td>0.048643</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.029532</td>\n",
       "      <td>-0.018287</td>\n",
       "      <td>-0.020097</td>\n",
       "      <td>-0.014978</td>\n",
       "      <td>0.003497</td>\n",
       "      <td>-0.015879</td>\n",
       "      <td>0.015766</td>\n",
       "      <td>-3063.311015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-27</th>\n",
       "      <td>23138.820313</td>\n",
       "      <td>0.011316</td>\n",
       "      <td>1</td>\n",
       "      <td>0.048643</td>\n",
       "      <td>-0.029532</td>\n",
       "      <td>-0.018287</td>\n",
       "      <td>-0.020097</td>\n",
       "      <td>-0.014978</td>\n",
       "      <td>-0.006850</td>\n",
       "      <td>0.019454</td>\n",
       "      <td>-1927.830195</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-28</th>\n",
       "      <td>23062.400391</td>\n",
       "      <td>-0.003308</td>\n",
       "      <td>0</td>\n",
       "      <td>0.011316</td>\n",
       "      <td>0.048643</td>\n",
       "      <td>-0.029532</td>\n",
       "      <td>-0.018287</td>\n",
       "      <td>-0.020097</td>\n",
       "      <td>-0.001591</td>\n",
       "      <td>0.019666</td>\n",
       "      <td>-1625.224492</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>292 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                   price    return  direction     lag_1     lag_2     lag_3  \\\n",
       "Date                                                                          \n",
       "2017-10-31  23377.240234  0.001220          1 -0.003653  0.001423  0.003056   \n",
       "2017-11-01  23435.009766  0.002468          1  0.001220 -0.003653  0.001423   \n",
       "2017-11-02  23531.380859  0.004104          1  0.002468  0.001220 -0.003653   \n",
       "2017-11-03  23539.189453  0.000332          1  0.004104  0.002468  0.001220   \n",
       "2017-11-06  23548.419922  0.000392          1  0.000332  0.004104  0.002468   \n",
       "...                  ...       ...        ...       ...       ...       ...   \n",
       "2018-12-21  22445.369141 -0.018287          0 -0.020097 -0.014978  0.003497   \n",
       "2018-12-24  21792.199219 -0.029532          0 -0.018287 -0.020097 -0.014978   \n",
       "2018-12-26  22878.449219  0.048643          1 -0.029532 -0.018287 -0.020097   \n",
       "2018-12-27  23138.820313  0.011316          1  0.048643 -0.029532 -0.018287   \n",
       "2018-12-28  23062.400391 -0.003308          0  0.011316  0.048643 -0.029532   \n",
       "\n",
       "               lag_4     lag_5  momentum  volatility     distance  \n",
       "Date                                                               \n",
       "2017-10-31 -0.004802  0.007184  0.000642    0.003386   880.433007  \n",
       "2017-11-01  0.003056 -0.004802 -0.000551    0.003355   875.463203  \n",
       "2017-11-02  0.001423  0.003056  0.000903    0.003356   902.530352  \n",
       "2017-11-03 -0.003653  0.001423  0.001112    0.003314   964.515624  \n",
       "2017-11-06  0.001220 -0.003653  0.000894    0.003304   937.208437  \n",
       "...              ...       ...       ...         ...          ...  \n",
       "2018-12-21 -0.021284 -0.020407 -0.014654    0.014375 -2124.190664  \n",
       "2018-12-24  0.003497 -0.021284 -0.014230    0.014726 -2475.353711  \n",
       "2018-12-26 -0.014978  0.003497 -0.015879    0.015766 -3063.311015  \n",
       "2018-12-27 -0.020097 -0.014978 -0.006850    0.019454 -1927.830195  \n",
       "2018-12-28 -0.018287 -0.020097 -0.001591    0.019666 -1625.224492  \n",
       "\n",
       "[292 rows x 11 columns]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "complimentary-plane",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "liked-transportation",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "292/292 [==============================] - 0s 10us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.818775327238318, 0.0]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.evaluate(test_data_[cols], test_data_['direction'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "stunning-nation",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(test_data_[cols]) > 0.5, 1 , 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "asian-massage",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "willing-knife",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " 1    240\n",
       "-1     52\n",
       "Name: prediction, dtype: int64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_data['prediction'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "hearing-equilibrium",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['strategy'] = (test_data['prediction'] * \n",
    "                        test_data['return'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "signed-gibson",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "return      0.987736\n",
       "strategy    1.064827\n",
       "dtype: float64"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " test_data[['return', 'strategy']].sum().apply(np.exp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "aggregate-boundary",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Date'>"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Eg08CTxgrf1HP+2VHkKpLwT6f/fzurAY+BPOm7O/Dw7dXpukf6HUD4B/4Uxvwp3qNBPY4ec1we/7iE9b1A+OQIj1hT04CcswxszBCeAqBvr+4EN94QiMdF/o5z4G+rnR7/uDGyxmuD8vwEl681I/jyljiQ2BTCpH8oWTGcjiDF2vdb/Ox5lD/CrOh6VXgXSfc3bhXNGsx7n6Mddn3w5gdj+P+Wv3vE73+4/d7bHAP4AinOxT0wOcfzuw0W3r68A8n31vAxVAk3vf54z27zhcvoLZF3CyTW127+sZICPAYy4BNuCsT7sTMO72Y937awCqgI0Bzvd7HPApoM3neawFFo327zhcvkKsLwT8f+9x/itAmU97n/bZNxXnw4JntH+34fQVYv3AAL8DNuGsmbkqwPkB30fUD8ZMX5gLLMdZv7QWODvA+QHfR9QXwq4vDPVzo9/3B/f8Te7Xe+hzwrj78r6oiIiIiIiISIgL2ymUIiIiIiIi440COBERERERkTChAE5ERERERCRMKIATEREREREJEwrgREREREREwoQCOBERGReMMR1ukdyNxph1xphvGGP6fB80xkw1xlwzUm0UERHpjwI4EREZL5qsUyR3Hk7x3fOBH/VzzlRAAZyIiIQM1YETEZFxwRhTb61N9Lk9HfgAyASmAA8CCe7ur1hr3zXGvAfMAXYC9wN3AL8ETgNigLustX8asSchIiLjngI4EREZF3oGcO62Q8BsoA7otNY2G2MKgUestUuMMacB37LWXugefwOQba39uTEmBlgOXGmt3TmSz0VERMavyNFugIiIyCgy7vco4E5jzCKgA5gZ4PizgQXGmCvc2ylAIc4InYiIyLBTACciIuOSO4WyAyjHWQtXBizEWR/eHOg04GZr7Ysj0kgREZEelMRERETGHWNMFnA3cKd11hKkAPuttZ3Ap4EI99A6IMnn1BeBLxtjotz7mWmMSUBERGSEaARORETGizhjzFqc6ZLtOElLfufu+wPwhDHmSuB1oMHdvh5oN8asA/4K3I6TmfJDY4wBKoBLR6b5IiIiSmIiIiIiIiISNjSFUkREREREJEwogBMREREREQkTCuBERERERETChAI4ERERERGRMKEATkREREREJEwogBMREREREQkTCuBERERERETCxP8Hz0N9/0d6l7kAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    " test_data[['return', 'strategy']].cumsum().apply(np.exp).plot(figsize=(15,7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "promising-formation",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "occupied-explanation",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "dev",
   "language": "python",
   "name": "dev"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
