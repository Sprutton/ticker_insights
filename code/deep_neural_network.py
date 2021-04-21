{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "hollow-contents",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from pathlib import Path\n",
    "%matplotlib inline\n",
    "from pylab import mpl, plt\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "incorporate-beatles",
   "metadata": {},
   "outputs": [],
   "source": [
    "path = '../data/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "opponent-horse",
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
   "id": "indian-humanity",
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
   "id": "capital-census",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia.set_index('Date', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "killing-profit",
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
   "id": "deadly-tension",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "common-perfume",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "saving-conjunction",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close = djia[['Close']].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "supreme-banana",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close.rename(columns={'Close' : 'price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "introductory-albania",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "beginning-inspiration",
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
   "id": "settled-johnston",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close['direction'] = np.where(djia_close['return']> 0, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "seeing-equipment",
   "metadata": {},
   "outputs": [],
   "source": [
    "lags = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ultimate-equipment",
   "metadata": {},
   "outputs": [],
   "source": [
    "cols = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "appropriate-gilbert",
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
   "id": "bright-measurement",
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
   "id": "proved-solid",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tensorflow in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (2.0.0)\n",
      "Requirement already satisfied: astor>=0.6.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.8.1)\n",
      "Requirement already satisfied: absl-py>=0.7.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.12.0)\n",
      "Requirement already satisfied: google-pasta>=0.1.6 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.2.0)\n",
      "Requirement already satisfied: numpy<2.0,>=1.16.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.19.5)\n",
      "Requirement already satisfied: grpcio>=1.8.6 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.36.1)\n",
      "Requirement already satisfied: tensorflow-estimator<2.1.0,>=2.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (2.0.1)\n",
      "Requirement already satisfied: wheel>=0.26 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.36.2)\n",
      "Requirement already satisfied: tensorboard<2.1.0,>=2.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (2.0.2)\n",
      "Requirement already satisfied: opt-einsum>=2.3.2 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (3.3.0)\n",
      "Requirement already satisfied: keras-applications>=1.0.8 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.0.8)\n",
      "Requirement already satisfied: gast==0.2.2 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (0.2.2)\n",
      "Requirement already satisfied: wrapt>=1.11.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.12.1)\n",
      "Requirement already satisfied: termcolor>=1.1.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.1.0)\n",
      "Requirement already satisfied: protobuf>=3.6.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (3.14.0)\n",
      "Requirement already satisfied: keras-preprocessing>=1.0.5 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.1.2)\n",
      "Requirement already satisfied: six>=1.10.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorflow) (1.12.0)\n",
      "Requirement already satisfied: h5py in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from keras-applications>=1.0.8->tensorflow) (3.1.0)\n",
      "Requirement already satisfied: google-auth<2,>=1.6.3 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (1.24.0)\n",
      "Requirement already satisfied: setuptools>=41.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (52.0.0.post20210125)\n",
      "Requirement already satisfied: werkzeug>=0.11.15 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (1.0.1)\n",
      "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (0.4.2)\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (2.25.1)\n",
      "Requirement already satisfied: markdown>=2.6.8 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from tensorboard<2.1.0,>=2.0.0->tensorflow) (3.3.4)\n",
      "Requirement already satisfied: cachetools<5.0,>=2.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (4.2.0)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (0.2.8)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (4.6)\n",
      "Requirement already satisfied: requests-oauthlib>=0.7.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.1.0,>=2.0.0->tensorflow) (1.3.0)\n",
      "Requirement already satisfied: importlib-metadata in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow) (2.0.0)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<2,>=1.6.3->tensorboard<2.1.0,>=2.0.0->tensorflow) (0.4.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (1.26.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (2020.12.5)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (3.0.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.1.0,>=2.0.0->tensorflow) (2.10)\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.1.0,>=2.0.0->tensorflow) (3.1.0)\n",
      "Requirement already satisfied: cached-property in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from h5py->keras-applications>=1.0.8->tensorflow) (1.5.2)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\jbarr\\anaconda3\\envs\\dev\\lib\\site-packages (from importlib-metadata->markdown>=2.6.8->tensorboard<2.1.0,>=2.0.0->tensorflow) (3.4.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install tensorflow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "british-likelihood",
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
   "source": [
    "import tensorflow as tf\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n",
    "from keras.optimizers import Adam, RMSprop\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "standard-bronze",
   "metadata": {},
   "outputs": [],
   "source": [
    "optimizer = Adam(learning_rate=0.0001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "celtic-offer",
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
   "id": "protected-cleveland",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "flush-savings",
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
   "id": "substantial-individual",
   "metadata": {},
   "outputs": [],
   "source": [
    "cutoff = '2017-10-31'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "north-experiment",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data = djia_close[djia_close.index < cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "finished-uncle",
   "metadata": {},
   "outputs": [],
   "source": [
    "mu, std = training_data.mean(), training_data.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "acting-centre",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_ = (training_data - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "divine-change",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data = djia_close[djia_close.index >= cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "clear-comfort",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data_ = (test_data - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "peripheral-absolute",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From C:\\Users\\JBarr\\anaconda3\\envs\\dev\\lib\\site-packages\\keras\\backend\\tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.\n",
      "\n",
      "Wall time: 9.75 s\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.callbacks.History at 0x146f43ae308>"
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
   "id": "southeast-boutique",
   "metadata": {},
   "outputs": [],
   "source": [
    "res = pd.DataFrame(model.history.history)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "unsigned-south",
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
       "      <td>0.692014</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.692506</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.691484</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.692071</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.690997</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.691677</td>\n",
       "      <td>0.538168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.690578</td>\n",
       "      <td>0.547074</td>\n",
       "      <td>0.691337</td>\n",
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
       "      <td>0.687797</td>\n",
       "      <td>0.539440</td>\n",
       "      <td>0.687139</td>\n",
       "      <td>0.552163</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>296</th>\n",
       "      <td>0.687797</td>\n",
       "      <td>0.539440</td>\n",
       "      <td>0.687125</td>\n",
       "      <td>0.552163</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>297</th>\n",
       "      <td>0.687792</td>\n",
       "      <td>0.539440</td>\n",
       "      <td>0.687115</td>\n",
       "      <td>0.550891</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>298</th>\n",
       "      <td>0.687791</td>\n",
       "      <td>0.539440</td>\n",
       "      <td>0.687101</td>\n",
       "      <td>0.550254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>299</th>\n",
       "      <td>0.687790</td>\n",
       "      <td>0.539440</td>\n",
       "      <td>0.687091</td>\n",
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
       "1    0.692014      0.547074  0.692506  0.538168\n",
       "2    0.691484      0.547074  0.692071  0.538168\n",
       "3    0.690997      0.547074  0.691677  0.538168\n",
       "4    0.690578      0.547074  0.691337  0.538168\n",
       "..        ...           ...       ...       ...\n",
       "295  0.687797      0.539440  0.687139  0.552163\n",
       "296  0.687797      0.539440  0.687125  0.552163\n",
       "297  0.687792      0.539440  0.687115  0.550891\n",
       "298  0.687791      0.539440  0.687101  0.550254\n",
       "299  0.687790      0.539440  0.687091  0.550254\n",
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
   "id": "residential-serve",
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
      "image/png": "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D7+/lYzEWL4zd3Sn7c+ZPJhzJg92IlRHKLkTEREREZEBYW3pXnbsaeT6U49qX3fcqEwWriljd23TAfd78dOdPPXRtk7rhmUk8uvzJ2JM+AzXVHLXz5KSkqirq3M6DBERERGRAWfBav/kKHPG5bSvmzd9KJ+W1PDtOUd1u8+yrdU89v5WfB3qe1fWt3DCUdl4fBa3S8mdDHAej4foaF1+ERERERk4duxpZOrQNHJS4trXpSa4+dOl0w64z/Th6Tx93XH9EZ7jwu/T/UOf67puwhdgxjXQ0gCPz+vaPvVLMO0yqK+Ep7/Sue2qlw96uh/96EcMHz6cb37zmwDceuutGGN46623qK6uprW1ldtvv53zzjvvkKHX1dVx3nnndbvfI488wl133YUxhsmTJ/Poo49SWlrKddddx6ZNmwD4y1/+wuDBgznnnHNYuXIlAHfddRd1dXXceuutzJ49m1mzZvHuu+/y+c9/njFjxnD77bfT0tJCZmYmjz/+OLm5udTV1XHDDTewdOlSjDH8/Oc/Z8+ePaxcuZI//OEPAPztb3+juLiY3//+94d8XiIiIiIiwfCbCybT4vH1+jjWWrZUNhATHcWQtPggRBYawi+562eXXHIJ3/3ud9uTu6effprXXnuN733ve6SkpFBRUcHMmTP5/Oc/f8jxvHFxcTz33HNd9lu9ejW/+tWvePfdd8nKyqKqqgqAb3/725x88sk899xzeL1e6urqqK6uPug59uzZw5tvvglAdXU1S5YswRjD3//+d+68805+97vfcdttt5GamsqKFSvat4uJiWHy5MnceeeduN1uHnroIf7617/29s8nIiIiItIj1lqMMe117Xp3LDjr7re47Njh3HLO+CBEFxrCL7k7WE9bTMLB2xMzD9lTt79p06ZRVlbGzp07KS8vJz09nby8PL73ve/x1ltvERUVxY4dOygtLWXQoEEHPZa1lp/85Cdd9lu0aBEXXXQRWVlZAGRkZACwaNEiHnnkEQBcLhepqamHTO4uvvji9uWSkhIuvvhidu3aRUtLCwUFBQAsWLCAJ598sn279PR0AE499VReeuklCgsLaW1tZdKkSYf1txIREREROVLffnI58e4o7rxoSq+PFRVlGJGZyOaK+iBEFjpU5y4ILrroIp555hmeeuopLrnkEh5//HHKy8tZtmwZy5cvJzc3l6amA8/e0+ZA+7V9S9ET0dHR+Hz7uqr3P29iYmL78g033MD111/PihUr+Otf/9q+7YHOd/XVV/PPf/6Thx56iKuuuqpH8YiIiIiI9FZTq5cFq0uD0mvXZlR2EpvKw2uiQyV3QXDJJZfw5JNP8swzz3DRRRdRU1NDTk4ObrebxYsXs3Xr1h4d50D7zZkzh6effprKykqA9mGZc+bM4S9/+QsAXq+X2tpacnNzKSsro7KykubmZl566aWDnm/IkCEAPPzww+3rTz/9dO699972x229gcceeyzbt2/niSee4NJLL+3pn0dEREREpFfe31RJY6uXuYW5QTvmyOxEtlc3BuUevlCh5C4IJkyYwN69exkyZAh5eXlcdtllLF26lKKiIh5//HHGjRvXo+McaL8JEybw05/+lJNPPpkpU6bw/e9/H4C7776bxYsXM2nSJKZPn86qVatwu9387Gc/49hjj+Wcc8456LlvvfVW5s2bx4knntg+5BPg5ptvprq6mokTJzJlyhQWL17c3vbFL36R448/vn2opoiIiIhIX1uwupSEGBczR2YG7ZgFWYl4fZZtVQ1BO6bTjO1Q7yHUFRUV2aVLl3ZaV1xcTGFhoUMRRZ5zzjmH733ve8yZM+eA2+iaiIiIiEiwWGuZdcciJuen8tfLi4J23N01TSzfXs2so7JIiXMH7bh9zRizzFrb7R9CPXfSI3v27GHMmDHEx8cfNLETEREREQmmFq+Py44dxsXHDA3qcQelxnHmxLwBldgdSvjNljkArFixgssvv7zTutjYWD744AOHIjq0tLQ01q1b53QYIiIiIhJhYqNdXH/q6D459tItVbR6LceNCt5wTyeFRXJ3OLNJhoJJkyaxfPlyp8PoEwNpmK+IiIiIhL53N1QwdWgaibHBT13+97U1GAzHjTou6Md2woAflhkXF0dlZaWSihBgraWyspK4uDinQxERERGRMFBa28Rlf/+Af763pU+OPzIriU0V4VMOYcD33OXn51NSUkJ5ebnToQj+ZDs/P9/pMEREREQkDCwsLgMIagmEjgqyE6lY2kJNYyup8QP/3rsBn9y53W4KCgqcDkNERERERIJsQXEp+enxjMlN6pPjj8xKBGBzRT1Th6b1yTn604AflikiIiIiIuGnscXLuxsqmFuY22fza4zM9ieNm8rDY2jmgO+5ExERERGR8LNkcyXNHl+f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jpK7XkqMjebUcTlkJ8c6HYqIiIiIiESwQ9a5k4MblZ3Eg1ce43QYIiIiIiIS4dRzJyIiIiIiEgaU3PXSkk2VHPvrBXy6fY/ToYiIiIiISARTctdLjS1eSmub8VnrdCgiIiIiIhLBlNz1kicwW6bbpT+liIiIiIg4RxlJL3kDde5cKoUgIiIiIiIOUnLXS61e1bkTERERERHnKbnrpbzUOM6ZnEdKvNvpUEREREREJIKpzl0vFY3IoGhEhtNhiIiIiIhIhFPPnYiIiIiISBhQctdLT320jYk/f53yvc1OhyIiIiIiIhFMyV0vNbX6qGv2aLZMERERERFxlJK7Xmqrc6fkTkREREREnKTkrpc8Xn+dO5VCEBERERERJym566W2nrtol5I7ERERERFxjpK7Xhqfl8IlxwwlOkp/ShERERERcY7q3PXSKeNyOGVcjtNhiIiIiIhIhFN3Uy9Za50OQURERERERMldb93x6hoKb3nN6TBERERERCTCKbnrJY/PqgyCiIiIiIg4TsldL3m8PiV3IiIiIiLiOCV3veTxWdW4ExERERERxym56yWvz6rGnYiIiIiIOE6lEHrp+KOyGJQa53QYIiIiIiIS4ZTc9dK5UwY7HYKIiIiIiIiGZfZWU6uXplav02GIiIiIiEiEU3LXS997ajmfv/cdp8MQEREREZEIp+Sul/x17vRnFBERERERZykr6SWP16dSCCIiIiIi4jgld73kUSkEEREREREJAUruesmrIuYiIiIiIhICVAqhl86fNgRrnY5CREREREQinZK7XppXNNTpEERERERERDQsU0REREREJBwouRMREREREQkDSu5ERERERETCgJI7ERERERGRMKDkTkREREREJAwouRMREREREQkDSu5ERERERETCgJI7ERERERGRMKDkTkREREREJAwouRMREREREQkDSu5ERERERETCgJI7ERERERGRMKDkTkREREREJAwouRMREREREQkDSu5ERERERETCgJI7ERERERGRMGCstU7H0GPGmHJgq9NxdCMLqHA6CHGErn3k0rWPbLr+kUvXPnLp2keuULv2w6212d01DKjkLlQZY5Zaa4ucjkP6n6595NK1j2y6/pFL1z5y6dpHroF07TUsU0REREREJAwouRMREREREQkDSu6C4wGnAxDH6NpHLl37yKbrH7l07SOXrn3kGjDXXvfciYiIiIiIhAH13ImIiIiIiIQBJXciIiIiIiJhQMldLxhjzjTGrDXGbDDG/NjpeKTvGWO2GGNWGGOWG2OWBtZlGGPmG2PWB36nOx2n9J4x5kFjTJkxZmWHdQe81saYmwL/Fqw1xpzhTNQSDAe49rcaY3YE3vvLjTFnd2jTtQ8TxpihxpjFxphiY8wqY8x3Auv13g9zB7n2eu9HAGNMnDHmQ2PMp4Hr/4vA+gH33tc9d0fIGOMC1gGnASXAR8Cl1trVjgYmfcoYswUostZWdFh3J1Blrb0jkOSnW2t/5FSMEhzGmJOAOuARa+3EwLpur7UxZjzwL2AGMBhYAIyx1nodCl964QDX/lagzlp7137b6tqHEWNMHpBnrf3YGJMMLAO+AFyJ3vth7SDX/ovovR/2jDEGSLTW1hlj3MA7wHeACxhg73313B25GcAGa+0ma20L8CRwnsMxiTPOAx4OLD+M/z8DGeCstW8BVfutPtC1Pg940lrbbK3dDGzA/2+EDEAHuPYHomsfRqy1u6y1HweW9wLFwBD03g97B7n2B6JrH0asX13goTvwYxmA730ld0duCLC9w+MSDv6PgIQHC/zXGLPMGHNtYF2utXYX+P9zAHIci0762oGutf49iAzXG2M+CwzbbBuao2sfpowxI4BpwAfovR9R9rv2oPd+RDDGuIwxy4EyYL61dkC+95XcHTnTzTqNcQ1/x1trjwbOAr4VGL4lon8Pwt9fgFHAVGAX8LvAel37MGSMSQKeBb5rra092KbdrNP1H8C6ufZ670cIa63XWjsVyAdmGGMmHmTzkL3+Su6OXAkwtMPjfGCnQ7FIP7HW7gz8LgOew98FXxoYq982Zr/MuQiljx3oWuvfgzBnrS0N/MfvA/7GvuE3uvZhJnC/zbPA49bafwdW670fAbq79nrvRx5r7R7gDeBMBuB7X8ndkfsIGG2MKTDGxACXAC86HJP0IWNMYuAma4wxicDpwEr81/2KwGZXAC84E6H0gwNd6xeBS4wxscaYAmA08KED8UkfafvPPeB8/O990LUPK4FJFf4BFFtrf9+hSe/9MHega6/3fmQwxmQbY9ICy/HAXGANA/C9H+10AAOVtdZjjLkeeB1wAQ9aa1c5HJb0rVzgOf+//0QDT1hrXzPGfAQ8bYz5GrANmOdgjBIkxph/AbOBLGNMCfBz4A66udbW2lXGmKeB1YAH+FYozJglR+YA1362MWYq/mE3W4Cvg659GDoeuBxYEbj3BuAn6L0fCQ507S/Vez8i5AEPB2bDjwKetta+ZIx5nwH23lcpBBERERERkTCgYZkiIiIiIiJhQMmdiIiIiIhIGFByJyIiIiIiEgaU3ImIiIiIiIQBJXciIiIiIiJhQMmdiIiIiIhIGFByJyIiIiIiEgb+H+6GhmlEiMx7AAAAAElFTkSuQmCC\n",
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
   "id": "affecting-wagon",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1965/1965 [==============================] - 0s 10us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[2.2349253379358287, 0.5155216455459595]"
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
   "id": "administrative-joint",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(training_data_[cols]) > 0.5, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "compressed-forum",
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
   "id": "hawaiian-python",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "reliable-carolina",
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
   "id": "governmental-attendance",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "return      2.189494\n",
       "strategy    1.804275\n",
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
   "id": "empty-macintosh",
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
   "id": "received-mercury",
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
       "[3.0849641643158376, 0.4452054798603058]"
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
   "id": "remarkable-discretion",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(test_data_[cols]) > 0.5, 1, 0 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "atomic-comedy",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "federal-caribbean",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " 1    161\n",
       "-1    131\n",
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
   "id": "sweet-motion",
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
   "id": "sapphire-engine",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "return      0.987736\n",
       "strategy    0.767778\n",
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
   "id": "normal-language",
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
      "image/png": "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q1H+dTOqw4m3QbWaFde+OFAAJyIiIiIilUNaGrTob+Pggr4P4Bompk1xpgBOREREREQqj0ZdbEJv7+3x/m1QvR5kZCa2XXGiAE5ERERERCqP7HZwaG+o+uS+bTYHXCWhAE5ERERERCqPBu3sdvsqu923VQGciIiIiIhIUspub7fbV9rt/m8LFzBJYQrgRERERESk8qjf2ibq3hHsgVMKpYiIiIiISHLKyIS6La0HLi/PeuAUwImIiIiIiCSp7HY2Bu7ATvBHlEIpIiIiIiKStLLbWQplcA449cCJiIiIiIgkqez2ljoZLGRS1QI459wI59wS59xy59ztEZ6/zTk3O/Az3zl3xDmXHXhutXNuXuC56fF+AyIiIiIiIvkEpxJY97XdVqIUyoziVnDOpQMPA6cA64CvnXPjvPcLg+t47+8D7gusfzbwS+/99rDdDPXeb4try0VERERERCLJDgZw0+y2ivXADQSWe+9Xeu8PAS8D5xax/qXAmHg0TkREREREpMSCPXDrZ9ptJeqBiyWAawGsDXu8LrCsEOdcLWAE8HrYYg9MdM7NcM6NjvYizrnRzrnpzrnpW7dujaFZIiIiIiIiEVSvDVmN4dBeqF7PphaoJGIJ4FyEZT7KumcDnxdInzzee98POB24wTl3QqQNvfePe+8HeO8H5OTkxNAsERERERGRKLLb221Ww8S2I85iCeDWAa3CHrcENkRZdxQF0ie99xsCt1uAN7GUTBERERERkfITHAeXVbk6h2IJ4L4GOjnn2jnnMrEgbVzBlZxz9YATgbfClmU55+oE7wOnAvPj0XAREREREZGoguPgKtH4N4ihCqX3Ptc59zPgfSAdeNp7v8A5d13g+UcDq54PTPTe7wvbvAnwpnMu+Fovee/fi+cbEBERERERKaSSplAWG8ABeO8nABMKLHu0wONngGcKLFsJ9C5TC0VEREREREoqu3L2wMU0kbeIiIiIiEhKadgB0quHArlKIqYeOBERERERkZRSswHcOB3qNEt0S+JKAZyIiIiIiFRO9VsnugVxpxRKERERERGRFKEATkREREREJEUogBMREREREUkRCuBERERERERShAI4ERERERGRFKEATkREREREJEUogBMREREREUkRCuBERERERERShAI4ERERERGRFKEATkREREREJEUogBMREREREUkRCuBERERERERS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\n",
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
   "id": "difficult-magnitude",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "designed-sperm",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "favorite-companion",
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
   "id": "smaller-shelf",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close['volatility'] = djia_close['return'].rolling(20).std().shift(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "binary-yukon",
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
   "id": "stopped-species",
   "metadata": {},
   "outputs": [],
   "source": [
    "djia_close.dropna(inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "worst-grenada",
   "metadata": {},
   "outputs": [],
   "source": [
    "cols.extend(['momentum', 'volatility', 'distance'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "everyday-survival",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "vocational-fleece",
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
   "id": "unavailable-seafood",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_new = djia_close[djia_close.index < cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "interpreted-interim",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "sweet-hayes",
   "metadata": {},
   "outputs": [],
   "source": [
    "mu, std = training_data_new.mean(), training_data_new.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "complex-sustainability",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_training_data_ = (training_data_new - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "attempted-interface",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data = djia_close[djia_close.index >= cutoff].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "united-regulation",
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
     "execution_count": 76,
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
   "execution_count": 77,
   "id": "favorite-anger",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data_ = (test_data - mu) / std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "outdoor-supplement",
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
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_tester_data_\n",
    "tester_data_new"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "ranking-driving",
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
   "id": "grand-short",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "nearby-disabled",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wall time: 1.25 s\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.callbacks.History at 0x146f9115688>"
      ]
     },
     "execution_count": 80,
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
   "execution_count": 81,
   "id": "focused-knowing",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1915/1915 [==============================] - 0s 26us/step\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0.6799437711817788, 0.567624032497406]"
      ]
     },
     "execution_count": 81,
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
   "execution_count": 82,
   "id": "proof-motorcycle",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(new_training_data_[cols]) > 0.5, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "thousand-adoption",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data_new['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "overall-groove",
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
   "execution_count": 85,
   "id": "civilian-austria",
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
     "execution_count": 85,
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
   "execution_count": 86,
   "id": "driving-authorization",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Date'>"
      ]
     },
     "execution_count": 86,
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
   "execution_count": 87,
   "id": "designed-bhutan",
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
     "execution_count": 87,
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
   "execution_count": 88,
   "id": "massive-match",
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
       "      <th>direction</th>\n",
       "      <th>distance</th>\n",
       "      <th>lag_1</th>\n",
       "      <th>lag_2</th>\n",
       "      <th>lag_3</th>\n",
       "      <th>lag_4</th>\n",
       "      <th>lag_5</th>\n",
       "      <th>momentum</th>\n",
       "      <th>prediction</th>\n",
       "      <th>price</th>\n",
       "      <th>return</th>\n",
       "      <th>strategy</th>\n",
       "      <th>volatility</th>\n",
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
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-10-31</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.464780</td>\n",
       "      <td>0.116796</td>\n",
       "      <td>0.303868</td>\n",
       "      <td>-0.597008</td>\n",
       "      <td>0.777299</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.417876</td>\n",
       "      <td>0.093919</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-01</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.093987</td>\n",
       "      <td>-0.465133</td>\n",
       "      <td>0.116732</td>\n",
       "      <td>0.303800</td>\n",
       "      <td>-0.596896</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.435710</td>\n",
       "      <td>0.237060</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-02</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.237123</td>\n",
       "      <td>0.093477</td>\n",
       "      <td>-0.465184</td>\n",
       "      <td>0.116656</td>\n",
       "      <td>0.304010</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.465462</td>\n",
       "      <td>0.424630</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-03</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.424686</td>\n",
       "      <td>0.236573</td>\n",
       "      <td>0.093414</td>\n",
       "      <td>-0.465284</td>\n",
       "      <td>0.116846</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.467872</td>\n",
       "      <td>-0.007922</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-06</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.007850</td>\n",
       "      <td>0.424083</td>\n",
       "      <td>0.236506</td>\n",
       "      <td>0.093337</td>\n",
       "      <td>-0.465157</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.470722</td>\n",
       "      <td>-0.001010</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
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
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-21</th>\n",
       "      <td>-1.079667</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.350403</td>\n",
       "      <td>-1.763431</td>\n",
       "      <td>0.354502</td>\n",
       "      <td>-2.486446</td>\n",
       "      <td>-2.386012</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.130192</td>\n",
       "      <td>-2.142969</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-24</th>\n",
       "      <td>-1.079667</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.142815</td>\n",
       "      <td>-2.350227</td>\n",
       "      <td>-1.763454</td>\n",
       "      <td>0.354436</td>\n",
       "      <td>-2.486536</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.928547</td>\n",
       "      <td>-3.432512</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-26</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-3.432309</td>\n",
       "      <td>-2.142697</td>\n",
       "      <td>-2.350236</td>\n",
       "      <td>-1.763608</td>\n",
       "      <td>0.354651</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.263891</td>\n",
       "      <td>5.532094</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-27</th>\n",
       "      <td>0.925728</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.531954</td>\n",
       "      <td>-3.431830</td>\n",
       "      <td>-2.142711</td>\n",
       "      <td>-2.350415</td>\n",
       "      <td>-1.763621</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.344272</td>\n",
       "      <td>1.251709</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-12-28</th>\n",
       "      <td>-1.079667</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.251733</td>\n",
       "      <td>5.529919</td>\n",
       "      <td>-3.431815</td>\n",
       "      <td>-2.142881</td>\n",
       "      <td>-2.350491</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.320680</td>\n",
       "      <td>-0.425321</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>292 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            direction  distance     lag_1     lag_2     lag_3     lag_4  \\\n",
       "Date                                                                      \n",
       "2017-10-31   0.925728       NaN -0.464780  0.116796  0.303868 -0.597008   \n",
       "2017-11-01   0.925728       NaN  0.093987 -0.465133  0.116732  0.303800   \n",
       "2017-11-02   0.925728       NaN  0.237123  0.093477 -0.465184  0.116656   \n",
       "2017-11-03   0.925728       NaN  0.424686  0.236573  0.093414 -0.465284   \n",
       "2017-11-06   0.925728       NaN -0.007850  0.424083  0.236506  0.093337   \n",
       "...               ...       ...       ...       ...       ...       ...   \n",
       "2018-12-21  -1.079667       NaN -2.350403 -1.763431  0.354502 -2.486446   \n",
       "2018-12-24  -1.079667       NaN -2.142815 -2.350227 -1.763454  0.354436   \n",
       "2018-12-26   0.925728       NaN -3.432309 -2.142697 -2.350236 -1.763608   \n",
       "2018-12-27   0.925728       NaN  5.531954 -3.431830 -2.142711 -2.350415   \n",
       "2018-12-28  -1.079667       NaN  1.251733  5.529919 -3.431815 -2.142881   \n",
       "\n",
       "               lag_5  momentum  prediction     price    return  strategy  \\\n",
       "Date                                                                       \n",
       "2017-10-31  0.777299       NaN         NaN  2.417876  0.093919       NaN   \n",
       "2017-11-01 -0.596896       NaN         NaN  2.435710  0.237060       NaN   \n",
       "2017-11-02  0.304010       NaN         NaN  2.465462  0.424630       NaN   \n",
       "2017-11-03  0.116846       NaN         NaN  2.467872 -0.007922       NaN   \n",
       "2017-11-06 -0.465157       NaN         NaN  2.470722 -0.001010       NaN   \n",
       "...              ...       ...         ...       ...       ...       ...   \n",
       "2018-12-21 -2.386012       NaN         NaN  2.130192 -2.142969       NaN   \n",
       "2018-12-24 -2.486536       NaN         NaN  1.928547 -3.432512       NaN   \n",
       "2018-12-26  0.354651       NaN         NaN  2.263891  5.532094       NaN   \n",
       "2018-12-27 -1.763621       NaN         NaN  2.344272  1.251709       NaN   \n",
       "2018-12-28 -2.350491       NaN         NaN  2.320680 -0.425321       NaN   \n",
       "\n",
       "            volatility  \n",
       "Date                    \n",
       "2017-10-31         NaN  \n",
       "2017-11-01         NaN  \n",
       "2017-11-02         NaN  \n",
       "2017-11-03         NaN  \n",
       "2017-11-06         NaN  \n",
       "...                ...  \n",
       "2018-12-21         NaN  \n",
       "2018-12-24         NaN  \n",
       "2018-12-26         NaN  \n",
       "2018-12-27         NaN  \n",
       "2018-12-28         NaN  \n",
       "\n",
       "[292 rows x 13 columns]"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "patient-favorite",
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
       "[0.818775327238318, 0.0]"
      ]
     },
     "execution_count": 91,
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
   "execution_count": 92,
   "id": "forty-consciousness",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = np.where(model.predict(test_data_[cols]) > 0.5, 1 , 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "impaired-invention",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['prediction'] = np.where(pred > 0, 1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "comfortable-thesaurus",
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
     "execution_count": 94,
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
   "execution_count": 95,
   "id": "animated-cleaning",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data['strategy'] = (test_data['prediction'] * \n",
    "                        test_data['return'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "wooden-portuguese",
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
     "execution_count": 96,
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
   "execution_count": 100,
   "id": "brutal-three",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Date'>"
      ]
     },
     "execution_count": 100,
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
   "id": "wanted-nancy",
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
