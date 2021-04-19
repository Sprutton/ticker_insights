import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = '../data/'
df = pd.read_csv(data_path+'SPY.csv', index_col='Date', parse_dates=True)

# make features
df['FastSMA']  = df['Close'].rolling(16).mean()
df['SlowSMA']  = df['Close'].rolling(33).mean()
feats = ['FastSMA', 'SlowSMA']

df['LogReturn'] = np.log(df['Close']).diff()

# split into train and test
Ntest = 1000
train_data = df.iloc[:-Ntest].copy()
test_data = df.iloc[-Ntest:].copy()

class Env:
  def __init__(self, df):
    self.df = df
    self.n = len(df)
    self.current_idx = 0
    self.action_space = [0, 1, 2] # BUY, SELL, HOLD
    self.invested = 0

    self.states = self.df[feats].to_numpy()
    self.rewards = self.df['LogReturn'].to_numpy()
    self.total_buy_and_hold = 0

  def reset(self):
    self.current_idx = 0
    self.total_buy_and_hold = 0
    self.invested = 0
    return self.states[self.current_idx]

  def step(self, action):
    # need to return (next_state, reward, done)
    self.current_idx += 1
    if self.current_idx >= self.n:
      raise Exception("Episode already done")

    if action == 0: # BUY
      self.invested = 1
    elif action == 1: # SELL
      self.invested = 0
    
    # compute reward
    if self.invested:
      reward = self.rewards[self.current_idx]
    else:
      reward = 0

    # state transition
    next_state = self.states[self.current_idx]

    # baseline
    self.total_buy_and_hold += self.rewards[self.current_idx]

    # done flag
    done = (self.current_idx == self.n - 1)
    return next_state, reward, done

class Agent:
  def __init__(self):
    self.is_invested = False

  def act(self, state):
    assert(len(state) == 2)
    # (fast, slow)

    if state[0] > state[1] and not self.is_invested:
      self.is_invested = True
      return 0 # Buy

    if state[0] < state[1] and self.is_invested:
      self.is_invested = False
      return 1 # sell

    return 2 # Do nothing

def play_one_episode(agent, env):
  state = env.reset()
  done = False
  total_reward = 0
  agent.is_invested = False

  while not done:
    action = agent.act(state)
    next_state, reward, done = env.step(action)
    total_reward += reward
    state = next_state

  return total_reward

#create 2 environments (training and testing)
train_env = Env(train_data)
test_env = Env(test_data)

#instanciate agent
agent = Agent()

train_reward = play_one_episode(agent, train_env)
test_reward = play_one_episode(agent, test_env)
train_reward, train_env.total_buy_and_hold
test_reward, test_env.total_buy_and_hold






