import gym
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.processors import MultiInputProcessor
from CardGameEnv import CardGameEnv
from tensorflow import keras
from keras.optimizers import Adam
from keras.layers import Dense, Activation, Flatten, Input, concatenate
from keras.models import Sequential,Model
from keras.utils import plot_model
import numpy as np
import sys

from rl.callbacks import (
    TrainEpisodeLogger,
    TrainIntervalLogger,
    FileLogger
)


# 環境の生成
env = CardGameEnv()
action_history = []
reward_history = []
nb_actions = env.action_space.n
#print(nb_actions)
print(env.observation_space)
observation_value_list = list(env.observation_space.values())
#bservation_arr = np.empty(1,len(observation_value_list))
#for i in observation_value_list:
#    observation_arr.append(i)
#print(observation_arr)
'''
for _ in range(200):
    action = env.action_space.sample()
    action_history.append(action)
    print("action.history: ")
    print(action_history)
    obs, re, done, info = env.step(action)
    reward_history.append(re)
    if done:
        action_history = []
        env.reset()
print(reward_history)
'''



# モデルの定義
model_x = Sequential()
model_x.add(Flatten(input_shape=(1,1), name='x'))
model_x_input = Input(shape=(1,1), name='x')
model_x_encoded = model_x(model_x_input)


model_fx = Sequential()
model_fx.add(Flatten(input_shape=(1,1), name='fx'))
model_fx_input = Input(shape=(1,1), name='fx')
model_fx_encoded = model_fx(model_fx_input)


model_theta = Sequential()
model_theta.add(Flatten(input_shape=(1,1), name='theta'))
model_theta_input = Input(shape=(1,1), name='theta')
model_theta_encoded = model_theta(model_theta_input)


model_ftheta = Sequential() 
model_ftheta.add(Flatten(input_shape=(1,1), name='ftheta'))
model_ftheta_input = Input(shape=(1,1), name='ftheta')
model_ftheta_encoded = model_ftheta(model_ftheta_input)

con = concatenate([model_x_encoded, model_fx_encoded, model_ftheta_encoded, model_theta_encoded])

hidden = Dense(16, activation='relu')(con)
for _ in range(2): 
	hidden = Dense(16, activation='relu')(hidden)
output = Dense(nb_actions, activation='linear')(hidden)
model_final = Model(inputs=[model_x_input, model_fx_input, model_theta_input, model_ftheta_input], outputs=output)
# print(model.summary())
#plot_model(model_final, to_file='model.png')

# エージェントの設定
memory = SequentialMemory(limit=50000, window_length=1)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model_final, nb_actions=nb_actions, memory=memory, nb_steps_warmup=2000,
               target_model_update=1e-2, policy=policy)
dqn.processor = MultiInputProcessor(17)
dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])

#学習
dqn.fit(env, nb_steps=int(1e5), visualize=False, verbose=1, callbacks=[ TrainEpisodeLogger()])
